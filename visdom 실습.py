import visdom
import torch
import torchvision.datasets as dsets
import torchvision

vis = visdom.Visdom()

cifar10 = dsets.CIFAR10(root='./cifar10', train=True, transform=torchvision.transforms.ToTensor(), download=True)
MNIST = dsets.MNIST(root='./MNIST_data', train=True, transform=torchivision.transforms.ToTensor(), download=True)

data = cifar10.__getitem__(0)
print(data[0].shape)
