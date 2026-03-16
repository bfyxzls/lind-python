# NumPy库的使用
import torch

X = torch.arange(4, dtype=torch.float32).reshape((2, 2))
A = X.numpy() # <class 'numpy.ndarray'>
B = torch.tensor(A) # <class 'torch.Tensor'>
a=torch.tensor([3.5]) #标量，一个浮点数
print(type(A), type(B))
print(a,a.item(),float(a),int(a))
