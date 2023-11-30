# =============================================================================
# Install necessary packages
# =============================================================================
# pip install inplace-abn
# pip install timm


# =============================================================================
# Import required libraries
# =============================================================================
from torch import nn
import timm


class TResNet(nn.Module):
    def __init__(self, args, num_classes, pretrained):
        super(TResNet, self).__init__()
        self.path = args.save_dir + 'TResNet_' + args.data + '.pth'

        tresnet = timm.create_model('tresnet_m', pretrained=pretrained)
        tresnet.head.fc = nn.Sequential(
            nn.Dropout(p=0.3),
            nn.Linear(in_features=2048, out_features=num_classes)
        )
        self.net = tresnet

    def forward(self, x):
        return self.net(x)
