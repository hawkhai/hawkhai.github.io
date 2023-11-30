# =============================================================================
# Import required libraries
# =============================================================================
import torch
from torch.nn.modules.loss import _Loss


class MultiLabelLoss(_Loss):
    def __init__(self,
                 gamma_neg=0,
                 gamma_pos=0,
                 pos_margin=0,
                 neg_margin=0,
                 threshold=0,
                 eps=1e-8):
        super(MultiLabelLoss, self).__init__()

        self.gamma_neg = gamma_neg
        self.gamma_pos = gamma_pos
        self.pos_margin = pos_margin
        self.neg_margin = neg_margin
        self.threshold = threshold
        self.eps = eps

    def forward(self, outputs, targets):
        if self.neg_margin is not None and self.neg_margin > 0:
            # probability margin
            p_m2 = (torch.sigmoid(outputs) - self.neg_margin).clamp(min=0)
            los_neg = (1 - targets) * torch.log((1 - p_m2).clamp(min=self.eps)) * (p_m2 ** self.gamma_neg)
        else:
            p = torch.sigmoid(outputs)
            los_neg = (1 - targets) * torch.log((1 - p).clamp(min=self.eps)) * (p ** self.gamma_neg)
        if self.pos_margin is not None and self.pos_margin > 0:
            # logit margin
            p_m1 = torch.sigmoid(outputs - self.pos_margin)
            # sub-function1 uses p_m1 in the positive part of the BCE loss
            p1 = p_m1.clone()
            p1[p1 < self.threshold] = 1
            l1 = targets * torch.log(p1.clamp(min=self.eps))
            # sub-function2 uses p_m1 in the positive part of the focal loss
            p2 = p_m1.clone()
            p2[p2 >= self.threshold] = 1
            l2 = targets * torch.log(p2.clamp(min=self.eps)) * ((1 - p2) ** self.gamma_pos)
            #
            los_pos = l1 + l2
        else:
            p = torch.sigmoid(outputs)
            los_pos = targets * torch.log(p.clamp(min=self.eps)) * ((1 - p) ** self.gamma_pos)
        loss = los_pos + los_neg
        return -loss.mean()
