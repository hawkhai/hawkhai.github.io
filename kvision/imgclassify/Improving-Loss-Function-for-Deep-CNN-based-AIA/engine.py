# =============================================================================
# Import required libraries
# =============================================================================
import timeit
import numpy as np
from tqdm import tqdm
from sklearn.metrics import matthews_corrcoef

import torch
from torch import optim
from torch.optim.lr_scheduler import OneCycleLR

from evaluation_metrics import EvaluationMetrics


class Engine():
    def __init__(self,
                 args,
                 model,
                 criterion,
                 train_loader,
                 validation_loader,
                 num_classes):
        self.args = args
        self.model = model
        self.criterion = criterion
        self.train_loader = train_loader
        self.validation_loader = validation_loader
        self.num_classes = num_classes

    def train_on_GPU(self):
        return torch.cuda.is_available()

    def learnabel_parameters(self):
        return [p for p in self.model.parameters() if p.requires_grad]

    def count_learnabel_parameters(self, parameters):
        return sum(p.numel() for p in parameters)

    def initialize_optimizer_and_scheduler(self):
        self.optimizer = optim.Adam(self.learnabel_parameters(),
                                    lr=self.args.learning_rate)
        #
        steps_per_epoch = len(self.train_loader)
        self.scheduler = OneCycleLR(self.optimizer,
                                    max_lr=self.args.learning_rate,
                                    steps_per_epoch=steps_per_epoch,
                                    epochs=self.args.epochs,
                                    pct_start=0.2)

    def initialization(self, is_train):
        if is_train:
            self.initialize_optimizer_and_scheduler()
            self.best_f1_score = 0

            print('Number of learnable parameters: ' +
                  str(self.count_learnabel_parameters(self.learnabel_parameters())))
            print('Optimizer: {}'.format(self.optimizer))

        self.metrics = EvaluationMetrics()

        if not self.train_on_GPU():
            print('CUDA is not available. Training on CPU ...')
        else:
            print('CUDA is available! Training on GPU ...')
            print(torch.cuda.get_device_properties('cuda'))
            #
            self.model.cuda()

    def PR_RC_F1_Nplus(self, results):
        N_plus = 'N+: {:.0f}'.format(results['N+'])
        per_class_metrics = 'per-class precision: {:.4f} \t per-class recall: {:.4f} \t per-class f1: {:.4f}'.format(
            results['per_class/precision'], results['per_class/recall'], results['per_class/f1'])
        per_image_metrics = 'per-image precision: {:.4f} \t per-image recall: {:.4f} \t per-image f1: {:.4f}'.format(
            results['per_image/precision'], results['per_image/recall'], results['per_image/f1'])
        return N_plus, per_class_metrics, per_image_metrics

    def load_model(self):
        self.model.load_state_dict(torch.load(self.model.path))
        if self.train_on_GPU():
            self.model.cuda()

    def save_model(self):
        torch.save(self.model.state_dict(), self.model.path)

    def train(self, dataloader, epoch=None, thresholds=0.5):
        train_loss = 0
        total_outputs = []
        total_targets = []
        self.model.train()

        for batch_idx, (images, targets) in enumerate(tqdm(dataloader)):

            if self.train_on_GPU():
                images, targets = images.cuda(), targets.cuda()

            # zero the gradients parameter
            self.optimizer.zero_grad()

            # forward pass: compute predicted outputs by passing inputs to
            # the model
            outputs = self.model(images)

            # calculate the batch loss
            loss = self.criterion(outputs, targets)

            # backward pass: compute gradient of the loss with respect to
            # the model parameters
            loss.backward()

            # parameters update
            self.optimizer.step()

            # learning rate update
            self.scheduler.step()

            train_loss += loss.item()
            total_outputs.append(torch.sigmoid(outputs))
            total_targets.append(targets)

        results = self.metrics.calculate_metrics(
            torch.cat(total_targets),
            torch.cat(total_outputs),
            thresholds,
            self.num_classes)
        print('Epoch: {}'.format(epoch+1))
        print('Train Loss: {:.5f}'.format(train_loss/(batch_idx+1)))
        #
        N_plus, per_class_metrics, per_image_metrics = self.PR_RC_F1_Nplus(
            results)
        print(N_plus)
        print(per_class_metrics)
        print(per_image_metrics)

    def validation(self,
                   dataloader,
                   epoch=None,
                   mcc=False,  # mcc: Matthews correlation coefficien
                   thresholds=0.5):
        if not mcc:
            valid_loss = 0
        total_outputs = []
        total_targets = []
        self.model.eval()

        with torch.no_grad():
            for batch_idx, (images, targets) in enumerate(tqdm(dataloader)):

                if self.train_on_GPU():
                    images, targets = images.cuda(), targets.cuda()

                outputs = self.model(images)

                if not mcc:
                    loss = self.criterion(outputs, targets)
                    valid_loss += loss.item()

                total_outputs.append(torch.sigmoid(outputs))
                total_targets.append(targets)

        results = self.metrics.calculate_metrics(
            torch.cat(total_targets),
            torch.cat(total_outputs),
            thresholds,
            self.num_classes)
        if not mcc:
            print('Validation Loss: {:.5f}'.format(valid_loss/(batch_idx+1)))
        #
        N_plus, per_class_metrics, per_image_metrics = self.PR_RC_F1_Nplus(
            results)
        print(N_plus)
        print(per_class_metrics)
        print(per_image_metrics)

        # save model when 'per-class f1-score' of the validation set improved
        if not mcc:
            if results['per_class/f1'] > self.best_f1_score:
                print('per-class f1 increased ({:.4f} --> {:.4f}). saving model ...'.format(
                    self.best_f1_score, results['per_class/f1']))
                # save the model's best result on the 'checkpoints' folder
                self.save_model()
                #
                lines = ['Epoch: ' + str(epoch+1),
                         N_plus,
                         per_class_metrics,
                         per_image_metrics]
                with open(self.args.save_dir + self.args.data + '_validation_results.txt', 'w') as f:
                    f.write('\n'.join(lines))
                f.close()
                #
                self.best_f1_score = results['per_class/f1']

    def train_iteration(self):
        print('==> Start of Training ...')
        for epoch in range(self.args.epochs):
            start = timeit.default_timer()
            self.train(self.train_loader, epoch)
            self.validation(self.validation_loader, epoch)
            print('LR {:.1e}'.format(self.scheduler.get_last_lr()[0]))
            stop = timeit.default_timer()
            print('time: {:.3f}'.format(stop - start))
        print('==> End of training ...')

    def matthew_corrcoef(self, dataloader):
        o = []
        t = []

        if self.train_on_GPU():
            self.model.cuda()
        self.model.eval()
        total_outputs = []
        total_targets = []
        with torch.no_grad():
            for batch_idx, (images, targets) in enumerate(dataloader):

                if self.train_on_GPU():
                    images, targets = images.cuda(), targets.cuda()

                outputs = self.model(images)

                total_outputs.append(torch.sigmoid(outputs))
                total_targets.append(targets)

        o.append(torch.cat(total_outputs))
        t.append(torch.cat(total_targets))
        t = np.array(t[0].cpu())
        o = np.array(o[0].cpu())

        best_thresholds = []
        thresholds = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3,
                      0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7]

        for i in range(self.num_classes):
            mcc = []
            for j in thresholds:
                hold = o[:, i].copy()
                hold[hold >= j] = 1
                hold[hold < j] = 0
                mcc.append(matthews_corrcoef(t[:, i], hold))
            best_thresholds.append(thresholds[np.argmax(mcc)])

        return best_thresholds
