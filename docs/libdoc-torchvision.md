---
title: "Torchvision Documentation"
package_name: "torchvision"
version: ">=0.25.0"
source: "https://pytorch.org/vision/"
last_updated: "2026-03-18 17:49:00"
description: "Torchvision is a PyTorch computer vision library providing datasets, models, and transformations for deep learning applications."
---

# Torchvision

Torchvision is a PyTorch computer vision library that provides popular datasets, model architectures, and common image transformations for computer vision tasks. It's part of the PyTorch ecosystem and is essential for deep learning applications involving images and videos.

## Version Information
- **Installed Version**: `>=0.25.0`
- **Documentation Source**: https://pytorch.org/vision/
- **Last Updated**: 2026-03-18 17:49:00

## Key Features
- 📊 Popular computer vision datasets (ImageNet, CIFAR, COCO, etc.)
- 🧠 Pre-trained model architectures (ResNet, VGG, AlexNet, etc.)
- 🔄 Image transformations and augmentation utilities
- 📹 Video processing capabilities
- 🎯 Object detection, segmentation, and classification models
- 🏗️ Building blocks for creating custom models
- 📱 Support for mobile deployment
- 🚀 GPU acceleration support

## Installation
```bash
pip install torchvision>=0.25.0
```

## Basic Usage
```python
import torchvision
import torchvision.transforms as transforms
from torchvision import datasets, models

# Load a pre-trained model
model = models.resnet18(pretrained=True)

# Define transformations
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                         std=[0.229, 0.224, 0.225])
])

# Load dataset
dataset = datasets.ImageNet(root='./data', train=False, 
                           download=True, transform=transform)
```

## Common Models
```python
from torchvision import models

# Classification models
resnet = models.resnet50(pretrained=True)
vgg = models.vgg16(pretrained=True)
alexnet = models.alexnet(pretrained=True)

# Object detection
detection = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

# Segmentation
segmentation = models.segmentation.deeplabv3_resnet50(pretrained=True)
```

## Data Augmentation
```python
import torchvision.transforms as T

# Common augmentations
transform = T.Compose([
    T.RandomHorizontalFlip(),
    T.RandomRotation(10),
    T.ColorJitter(brightness=0.2, contrast=0.2),
    T.RandomResizedCrop(224),
    T.ToTensor(),
])
```

## Additional Resources
- [Official Documentation](https://pytorch.org/vision/)
- [PyPI Package](https://pypi.org/project/torchvision/)
- [GitHub Repository](https://github.com/pytorch/vision)
- [Tutorials](https://pytorch.org/tutorials/)
- [Model Zoo](https://pytorch.org/vision/stable/models.html)

---

*This documentation was automatically generated using Tavily Remote MCP and the dependency-documenter skill.*
