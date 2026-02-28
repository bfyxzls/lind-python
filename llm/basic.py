import torch
import torch.nn as nn

print("=== 1. 神经网络本质：矩阵x向量（基础运算）===")
# 模拟单个神经元：y = Wx + b
input_size = 3   # 输入维度
output_size = 2  # 输出维度

# 权重矩阵 W: output_size x input_size
W = torch.tensor([[0.1, 0.2, 0.3],
                  [0.4, 0.5, 0.6]], dtype=torch.float32)

# 输入向量 x: input_size
x = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# 偏置 b: output_size
b = torch.tensor([0.1, 0.2], dtype=torch.float32)

# 线性变换：y = Wx + b
y = torch.matmul(W, x) + b  # 矩阵x向量
print(f"权重矩阵 W: \n{W}")
print(f"输入向量 x: {x}")
print(f"偏置 b: {b}")
print(f"输出 y = Wx + b: {y}")

# 使用PyTorch的Linear层（内部就是矩阵x向量）
linear_layer = nn.Linear(input_size, output_size)
with torch.no_grad():  # 不计算梯度
    linear_layer.weight.data = W
    linear_layer.bias.data = b
    y_pytorch = linear_layer(x)
print(f"PyTorch Linear层输出: {y_pytorch}")
print(f"验证是否相等: {torch.allclose(y, y_pytorch)}")

print("\n=== 2. 模型训练：标量x矩阵（梯度更新）===")
# 模拟梯度下降更新
lr = 0.01  # 学习率（标量）

# 模型参数矩阵（例如权重）
params = torch.tensor([[1.0, 2.0],
                       [3.0, 4.0]], dtype=torch.float32)

# 梯度矩阵（反向传播计算得到）
grads = torch.tensor([[0.1, -0.2],
                      [0.3, -0.4]], dtype=torch.float32)

print(f"原始参数: \n{params}")
print(f"梯度: \n{grads}")
print(f"学习率: {lr}")
# 梯度下降更新：params = params - lr * grads
# 标量x矩阵：学习率乘以梯度矩阵
params_updated = params - lr * grads
print(f"更新后的参数: \n{params_updated}")
# 实际PyTorch优化器就是这样工作的
optimizer = torch.optim.SGD([torch.nn.Parameter(params)], lr=lr)
print("实际优化器内部就是通过标量缩放梯度矩阵来更新参数")

print("\n=== 3. 模型架构：矩阵x矩阵（网络堆叠）===")
# 模拟一个简单的2层MLP
batch_size = 2
input_dim = 3
hidden_dim = 4
output_dim = 2

# 输入矩阵 X: batch_size x input_dim
X = torch.tensor([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]], dtype=torch.float32)

# 权重矩阵 W1: hidden_dim x input_dim
W1 = torch.randn(hidden_dim, input_dim, dtype=torch.float32)

# 权重矩阵 W2: output_dim x hidden_dim
W2 = torch.randn(output_dim, hidden_dim, dtype=torch.float32)

print(f"输入矩阵 X (batch_size={batch_size}, input_dim={input_dim}):\n{X}")
print(f"第一层权重 W1 (hidden_dim={hidden_dim}, input_dim={input_dim}):\n{W1}")
print(f"第二层权重 W2 (output_dim={output_dim}, hidden_dim={hidden_dim}):\n{W2}")

# 前向传播：矩阵x矩阵
# 第一层：H = X @ W1^T （注意：PyTorch Linear层是 x @ W^T + b）
H = torch.matmul(X, W1.T)  # 矩阵乘法：XW1^T
print(f"\n第一层输出 H = X @ W1^T (batch_size={batch_size}, hidden_dim={hidden_dim}):\n{H}")

# 激活函数（ReLU）
H_relu = torch.relu(H)
print(f"激活后: \n{H_relu}")
# 第二层：Y = H_relu @ W2^T
Y = torch.matmul(H_relu, W2.T)  # 矩阵乘法：H_relu @ W2^T
print(f"第二层输出 Y = H_relu @ W2^T (batch_size={batch_size}, output_dim={output_dim}):\n{Y}")

# 使用PyTorch Sequential（本质是一堆矩阵乘法的堆叠）
print("\n=== 使用PyTorch Sequential（矩阵堆叠的封装）===")
model = nn.Sequential(
    nn.Linear(input_dim, hidden_dim),  # W1: hidden_dim x input_dim
    nn.ReLU(),  # 激活函数
    nn.Linear(hidden_dim, output_dim)  # W2: output_dim x hidden_dim
)

# 设置与上面相同的权重
with torch.no_grad():
    model[0].weight.data = W1
    model[2].weight.data = W2

    # 也可以设置偏置
    model[0].bias.data.zero_()
    model[2].bias.data.zero_()

output = model(X)
print(f"PyTorch模型输出: \n{output}")
print(f"手动计算与PyTorch是否相等: {torch.allclose(Y, output)}")

print("\n=== 总结 ===")
print("1. 基础=矩阵x向量: 神经元的线性变换 y = Wx + b")
print("2. 训练=标量x矩阵: 梯度下降 params = params - lr * grads")
print("3. 架构=矩阵x矩阵: 神经网络前向传播 = 矩阵乘法的堆叠")
print("\n深度学习本质: 通过矩阵运算的堆叠来近似复杂的函数映射")
print("所有大模型(LLM)都是这些基本操作的组合和扩展:")
print("- Attention机制: Q @ K^T  (矩阵x矩阵)")
print("- FFN层: 多个Linear层的堆叠")
print("- 训练过程: 反向传播计算梯度，标量缩放更新参数")