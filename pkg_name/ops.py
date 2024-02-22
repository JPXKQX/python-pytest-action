import torch


def add_squared(x: torch.Tensor, y: torch.Tensor):
    return torch.pow(x, 2) + torch.pow(y, 2)
