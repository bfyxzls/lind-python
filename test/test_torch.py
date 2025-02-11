import torch

# 张量（Tensor）是数据的一种多维数组表示形式，它在数学上可以表示为向量、矩阵以及更高维度的数组。

# 创建一个 1D 张量
tensor_1d = torch.tensor([1, 2, 3, 4, 5]) # 1行5列
print("1D Tensor:", tensor_1d)

# 创建一个 2D 张量
tensor_2d = torch.tensor([[1, 2], [3, 4]]) # 2行2列
print("2D Tensor:\n", tensor_2d)

# 创建一个全零的张量
zero_tensor = torch.zeros((2, 3)) # 2行3列
print("Zero Tensor:\n", zero_tensor)

# 创建一个随机张量
random_tensor = torch.rand((5, 3)) # 5行3列
print("Random Tensor:\n", random_tensor)

# 张量相加
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
sum_tensor = a + b
print("Sum:", sum_tensor)

# 矩阵乘法
# [1,2     [5,6
# 3,4]     7,8]
#C 中第 i 行第 j 列的元素 c_{ij} 是由 A 的第 i 行和 B 的第 j 列对应元素乘积的和。
# c11=(1*5+2*7)=19
# c12=(1*6+2*8)=22
# c21=(3*5+4*7)=43
# c22=(3*6+4*8)=50
# [19, 22
# 43, 50]
matrix_a = torch.tensor([[1, 2], [3, 4]])
matrix_b = torch.tensor([[5, 6], [7, 8]])
product = torch.mm(matrix_a, matrix_b)
print("Matrix Product:\n", product)

# 创建一个需要计算梯度的张量
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2 + 3 * x + 1

# 反向传播
y.backward()

# 查看梯度
print("Gradient of y with respect to x:", x.grad)
