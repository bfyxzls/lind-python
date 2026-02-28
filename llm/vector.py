import torch

# 一维向量（张量）操作
print("===== 一维向量操作 =====")
# 创建一维张量
vector_1d = torch.tensor([1, 2, 3, 4, 5])
print(f"一维向量: {vector_1d}")
print(f"形状: {vector_1d.shape}")
print(f"数据类型: {vector_1d.dtype}")

# 基本运算
vector_a = torch.tensor([1, 2, 3, 4, 5])
vector_b = torch.tensor([5, 4, 3, 2, 1])

print(f"\n向量A: {vector_a}")
print(f"向量B: {vector_b}")
print(f"加法: {vector_a + vector_b}")
print(f"减法: {vector_a - vector_b}")
print(f"逐元素乘法: {vector_a * vector_b}")
print(f"点积: {torch.dot(vector_a, vector_b)}")
# print(f"范数: {torch.norm(vector_a)}") # 这行出错了

# 二维矩阵（张量）操作
print("\n===== 二维矩阵操作 =====")
# 创建二维张量
matrix_2d = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"二维矩阵:\n{matrix_2d}")
print(f"形状: {matrix_2d.shape}")

# 矩阵运算
matrix_a = torch.tensor([[1, 2], [3, 4]])
matrix_b = torch.tensor([[5, 6], [7, 8]])

print(f"\n矩阵A:\n{matrix_a}")
print(f"矩阵B:\n{matrix_b}")
print(f"矩阵相加:\n{matrix_a + matrix_b}")
print(f"矩阵相乘（逐元素）:\n{matrix_a * matrix_b}")
print(f"矩阵乘法（点积）:\n{torch.matmul(matrix_a, matrix_b)}")
print(f"转置:\n{matrix_a.T}")

# 三维张量操作
print("\n===== 三维张量操作 =====")
tensor_3d = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"三维张量:\n{tensor_3d}")
print(f"形状: {tensor_3d.shape}")

# 批量矩阵运算
batch_size = 3
batch_matrices = torch.randn(batch_size, 2, 3)  # 3个2x3矩阵
batch_weights = torch.randn(batch_size, 3, 4)   # 3个3x4矩阵
batch_result = torch.bmm(batch_matrices, batch_weights)  # 批量矩阵乘法
print(f"\n批量矩阵形状: {batch_matrices.shape}")
print(f"批量权重形状: {batch_weights.shape}")
print(f"批量乘法结果形状: {batch_result.shape}")

# 更高维度张量
print("\n===== 更高维度张量 =====")
tensor_4d = torch.randn(2, 3, 4, 5)  # 4维张量
print(f"四维张量形状: {tensor_4d.shape}")

# 张量重塑和维度操作
print("\n===== 张量重塑 =====")
original = torch.arange(12)
print(f"原始张量: {original}, 形状: {original.shape}")

# 重塑为不同维度
reshaped_2x6 = original.view(2, 6)
reshaped_3x4 = original.view(3, 4)
reshaped_2x3x2 = original.view(2, 3, 2)

print(f"重塑为2x6:\n{reshaped_2x6}")
print(f"重塑为3x4:\n{reshaped_3x4}")
print(f"重塑为2x3x2:\n{reshaped_2x3x2}")

# 维度操作
tensor = torch.randn(2, 3, 4)
print(f"\n原始张量形状: {tensor.shape}")
print(f"交换维度(0和1): {tensor.transpose(0, 1).shape}")
print(f"交换维度(0和2): {tensor.transpose(0, 2).shape}")
print(f"压缩维度: {tensor.squeeze().shape}")
print(f"扩展维度: {tensor.unsqueeze(0).shape}")

# 广播机制
print("\n===== 广播机制 =====")
tensor_a = torch.ones(3, 4, 5)
tensor_b = torch.ones(5)
result = tensor_a + tensor_b  # 广播
print(f"张量A形状: {tensor_a.shape}")
print(f"张量B形状: {tensor_b.shape}")
print(f"广播加法结果形状: {result.shape}")

# 归约操作
print("\n===== 归约操作 =====")
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
print(f"张量:\n{tensor}")
print(f"沿维度0求和: {tensor.sum(dim=0)}")  # 按列求和
print(f"沿维度1求和: {tensor.sum(dim=1)}")  # 按行求和
print(f"均值: {tensor.mean()}")
print(f"标准差: {tensor.std()}")

# 张量索引和切片
print("\n===== 张量索引和切片 =====")
tensor = torch.arange(24).reshape(2, 3, 4)
print(f"张量形状: {tensor.shape}")
print(f"第一个元素: {tensor[0, 0, 0]}")
print(f"第一层: {tensor[0]}")
print(f"第一层的第二行: {tensor[0, 1]}")
print(f"所有层的第二行: {tensor[:, 1, :]}")
print(f"第二列: {tensor[:, :, 1]}")

# 张量拼接
print("\n===== 张量拼接 =====")
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])
print(f"沿维度0拼接: {torch.cat([a, b], dim=0)}")
print(f"沿维度1拼接: {torch.cat([a, b], dim=1)}")

# 内存布局
print("\n===== 内存布局 =====")
x = torch.tensor([[1, 2], [3, 4]])
x_contiguous = x.contiguous()  # 确保内存连续
print(f"是否连续: {x.is_contiguous()}")
print(f"转置后是否连续: {x.T.is_contiguous()}")