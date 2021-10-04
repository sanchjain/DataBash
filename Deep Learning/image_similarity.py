from PIL import Image
from tqdm import tqdm
import os
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
import cv2
from torch.autograd import Variable
from torch.nn import Module

class Model(Module):
    def __init__(self, backbone):
        super(Model, self).__init__()
        self.base_model = models.inception_v3(pretrained=True)
        self.base_model.fc = nn.Identity()

    def forward(self, input): return self.base_model(input)
