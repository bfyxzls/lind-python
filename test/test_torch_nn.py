import torch
import torch.nn as nn
import torch.optim as optim


# 定义一个简单的前馈神经网络
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 2)  # 输入层到隐藏层
        self.fc2 = nn.Linear(2, 1)  # 隐藏层到输出层

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # 使用 ReLU 激活函数
        x = self.fc2(x)
        return x


# 实例化模型
model = SimpleNN()

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 示例数据
inputs = torch.tensor([[1.0, 2.0], [2.0, 3.0]])
targets = torch.tensor([[1.0], [2.0]])

# 训练步骤
for epoch in range(100):
    optimizer.zero_grad()  # 清空梯度
    outputs = model(inputs)  # 前向传播
    loss = criterion(outputs, targets)  # 计算损失
    loss.backward()  # 反向传播
    optimizer.step()  # 更新参数

print("Final Outputs:\n", model(inputs).detach())
