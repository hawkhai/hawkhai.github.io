# =============================================================================
# Import required libraries
# =============================================================================
import torch


class EvaluationMetrics():
    def __init__(self):
        self.epsilon = 1e-07

    def per_class_precision(self, targets, outputs):
        tp = torch.sum(targets * outputs, 0)
        predicted = torch.sum(outputs, 0)
        return torch.mean(tp / (predicted + self.epsilon))

    def per_class_recall(self, targets, outputs):
        tp = torch.sum(targets * outputs, 0)
        grand_truth = torch.sum(targets, 0)
        return torch.mean(tp / (grand_truth + self.epsilon))

    def per_image_precision(self, targets, outputs):
        tp = torch.sum(targets * outputs)
        predicted = torch.sum(outputs)
        return tp / (predicted + self.epsilon)

    def per_image_recall(self, targets, outputs):
        tp = torch.sum(targets * outputs)
        grand_truth = torch.sum(targets)
        return tp / (grand_truth + self.epsilon)

    def f1_score(self, precision, recall):
        return 2 * ((precision * recall) / (precision + recall + self.epsilon))

    def N_plus(self, targets, outputs):
        tp = torch.sum(targets * outputs, 0)
        return torch.sum(torch.gt(tp, 0).int())

    def calculate_metrics(self, targets, outputs, thresholds, num_classes):
        if thresholds == 0.5:
            outputs = torch.gt(outputs, thresholds).float()
        else:
            for i in range(num_classes):
                outputs[:, i] = torch.gt(
                    outputs[:, i], thresholds[i]).float()
        pcp = self.per_class_precision(targets, outputs)
        pcr = self.per_class_recall(targets, outputs)
        pip = self.per_image_precision(targets, outputs)
        pir = self.per_image_recall(targets, outputs)
        pcf = self.f1_score(pcp, pcr)
        pif = self.f1_score(pip, pir)
        n_plus = self.N_plus(targets, outputs)
        return {'per_class/precision': pcp,
                'per_class/recall': pcr,
                'per_class/f1': pcf,
                'per_image/precision': pip,
                'per_image/recall': pir,
                'per_image/f1': pif,
                'N+': n_plus,
                }
