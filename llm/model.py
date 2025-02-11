# hyperparameters for the model
import torch

d_model = 512
context_length = 16
num_heads = 8
header_size = d_model // num_heads
dropout = 0.1
device = 'cuda' if torch.cuda.is_available() else 'cpu'  # torch是一个深度学习框架


class Test():
    def __init__(self):
        self.d_model = d_model
        self.context_length = context_length
        self.num_heads = num_heads
        self.header_size = header_size
        self.dropout = dropout
        self.device = device

    def print(self):
        print("d_model: ", self.d_model)
        print("context_length: ", self.context_length)
        print("num_heads: ", self.num_heads)
        print("header_size: ", self.header_size)
        print("dropout: ", self.dropout)
        print("device: ", self.device)
