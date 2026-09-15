import torch
import torch.nn as nn

def build_mlp(in_dim: int, hidden_dim: int, out_dim: int) -> nn.Sequential:
    # TODO: return a Sequential of Linear -> ReLU -> Linear
    model = nn.Sequential(
        nn.Linear(in_features= in_dim, out_features=hidden_dim),
        nn.ReLU(),
        nn.Linear(in_features = hidden_dim, out_features = out_dim)
    )
    return model