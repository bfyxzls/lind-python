# -*- coding: utf-8 -*-
# 梯度下降
import sys
import io

# 设置标准输出编码为UTF-8，避免Windows控制台编码问题
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import numpy as np
import torch
import torch.nn as nn

# 尝试导入matplotlib，如果失败则跳过绘图部分
try:
    import matplotlib
    matplotlib.use('Agg')  # 使用非交互式后端，避免GUI相关错误
    import matplotlib.pyplot as plt
    # 设置中文字体，避免中文显示警告
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题
    try:
        from matplotlib.animation import FuncAnimation
        ANIMATION_AVAILABLE = True
    except ImportError:
        ANIMATION_AVAILABLE = False
    MATPLOTLIB_AVAILABLE = True
except (ImportError, ModuleNotFoundError) as e:
    print(f"警告: matplotlib导入失败 ({e})，将跳过绘图部分")
    MATPLOTLIB_AVAILABLE = False
    plt = None
    ANIMATION_AVAILABLE = False

# IPython 相关导入（仅在 Jupyter 环境中需要）
try:
    from IPython.display import HTML
    IPYTHON_AVAILABLE = True
except ImportError:
    IPYTHON_AVAILABLE = False

print("=== 梯度下降：神经网络如何学习 ===\n")

# 1. 从最简单的问题开始：找到函数最小值
print("=== 1. 问题：找到函数 y = x² 的最小值 ===")


# 定义函数 y = x²
def f(x):
    return x ** 2


# 定义导数 dy/dx = 2x
def df(x):
    return 2 * x


# 可视化函数
x_vals = np.linspace(-3, 3, 100)
y_vals = f(x_vals)

if MATPLOTLIB_AVAILABLE:
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.plot(x_vals, y_vals, 'b-', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y = x²')
    plt.grid(True, alpha=0.3)
    plt.title('目标函数：y = x²')

    # 在几个点上画切线（梯度）
    points = [-2, -1, 0, 1, 2]
    for point in points:
        plt.scatter(point, f(point), color='red', s=50)
        # 切线方程：y = f'(x0)(x - x0) + f(x0)
        tangent_x = np.array([point - 0.5, point + 0.5])
        tangent_y = df(point) * (tangent_x - point) + f(point)
        plt.plot(tangent_x, tangent_y, 'r--', alpha=0.5)
        plt.text(point, f(point) + 0.5, f"斜率={df(point):.1f}",
                 ha='center', fontsize=10)

print(f"函数 y = x² 的导数 dy/dx = 2x")
print(f"在 x=2 处，导数 = {df(2)}，表示x增加时y增加")
print(f"在 x=-2 处，导数 = {df(-2)}，表示x增加时y减少")
print(f"在 x=0 处，导数 = 0，这是最小值点！")

# 2. 什么是梯度(Gradient)？
print("\n=== 2. 什么是梯度？ ===")
print("梯度是多元函数的导数")
print("对于 f(x₁, x₂) = x₁² + x₂²:")


# 二维函数示例
def f2d(x1, x2):
    return x1 ** 2 + x2 ** 2


def gradient_f2d(x1, x2):
    """返回梯度向量 [∂f/∂x1, ∂f/∂x2]"""
    return np.array([2 * x1, 2 * x2])


# 可视化二维函数的梯度
if MATPLOTLIB_AVAILABLE:
    x1 = np.linspace(-2, 2, 20)
    x2 = np.linspace(-2, 2, 20)
    X1, X2 = np.meshgrid(x1, x2)
    Z = f2d(X1, X2)

    plt.subplot(2, 2, 2)
    plt.contour(X1, X2, Z, levels=20, cmap='RdYlBu_r')
    plt.colorbar(label='f(x1, x2)')
    # 在几个点上画梯度向量

    points_2d = [(1.5, 1.5), (0, 1.5), (-1.5, 0), (0, 0)]
    colors = ['red', 'green', 'blue', 'black']

    for (px1, px2), color in zip(points_2d, colors):
        grad = gradient_f2d(px1, px2)
        plt.quiver(px1, px2, -grad[0], -grad[1],  # 负梯度方向
                   color=color, scale=20, width=0.005,
                   label=f'({px1},{px2})')
        plt.scatter(px1, px2, color=color, s=50)

    plt.xlabel('x₁')
    plt.ylabel('x₂')
    plt.title('梯度指向最陡上升方向\n负梯度指向最陡下降方向')
    plt.legend()
    plt.grid(True, alpha=0.3)

print("\n梯度性质:")
print("1. 梯度指向函数值增加最快的方向")
print("2. 负梯度指向函数值减少最快的方向")
print("3. 在最小值点，梯度 = 0")

# 3. 梯度下降算法
print("\n=== 3. 梯度下降算法 ===")
print("核心思想：沿着负梯度方向更新参数")


def gradient_descent_1d(start_x, learning_rate, n_iterations):
    """一维梯度下降"""
    x = start_x
    history = [x]

    for i in range(n_iterations):
        grad = df(x)  # 计算梯度
        x = x - learning_rate * grad  # 更新：x = x - η * ∇f(x)
        history.append(x)

        if i < 3:  # 显示前3次更新
            print(f"第{i + 1}次迭代:")
            print(f"  x = {history[-2]:.4f}, 梯度 = {grad:.4f}")
            print(f"  更新: x = {history[-2]:.4f} - {learning_rate} * {grad:.4f} = {x:.4f}")
            print(f"  y = {f(x):.4f}")

    return np.array(history)


# 不同学习率的效果
print("\n尝试不同学习率:")
learning_rates = [0.1, 0.5, 1.0, 1.1]

if MATPLOTLIB_AVAILABLE:
    plt.subplot(2, 2, 3)
    plt.plot(x_vals, y_vals, 'b-', linewidth=2, alpha=0.5)

    for lr in learning_rates:
        history = gradient_descent_1d(start_x=2.0, learning_rate=lr, n_iterations=20)
        plt.plot(history, f(history), 'o-', label=f'lr={lr}', alpha=0.7, markersize=4)
        if lr == 1.1:
            plt.text(history[-1], f(history[-1]), f'lr={lr}', fontsize=8)

    plt.xlabel('x')
    plt.ylabel('y = x²')
    plt.title('不同学习率的效果')
    plt.legend()
    plt.grid(True, alpha=0.3)

print("\n学习率的影响:")
print("- 学习率太小 → 收敛慢")
print("- 学习率合适 → 快速收敛")
print("- 学习率太大 → 在最小值附近震荡")
print("- 学习率极大 → 发散！")

# 4. 神经网络中的梯度下降
print("\n=== 4. 神经网络中的梯度下降 ===")
print("在神经网络中，我们要最小化损失函数 L(θ)")

# 模拟一个简单的线性回归问题
np.random.seed(42)
n_samples = 20
X = np.random.randn(n_samples, 1)  # 输入
true_w, true_b = 2.0, 1.0
y = true_w * X + true_b + 0.1 * np.random.randn(n_samples, 1)  # 加噪声

# 转换为PyTorch张量
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32)


# 定义模型
class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.w = nn.Parameter(torch.randn(1))  # 权重参数
        self.b = nn.Parameter(torch.randn(1))  # 偏置参数

    def forward(self, x):
        return self.w * x + self.b


model = LinearModel()
print(f"初始参数: w={model.w.item():.4f}, b={model.b.item():.4f}")

# 定义损失函数（均方误差）
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# 训练过程
losses = []
params_history = []

n_epochs = 50
for epoch in range(n_epochs):
    # 前向传播
    y_pred = model(X_tensor)
    loss = criterion(y_pred, y_tensor)

    # 反向传播（计算梯度）
    optimizer.zero_grad()  # 清空之前的梯度
    loss.backward()  # 计算梯度

    # 保存梯度信息
    if epoch < 3:
        print(f"\n第{epoch + 1}次迭代:")
        print(f"  损失: {loss.item():.4f}")
        print(f"  梯度w: {model.w.grad.item():.4f}")
        print(f"  梯度b: {model.b.grad.item():.4f}")
        print(f"  更新前w: {model.w.item():.4f}, b: {model.b.item():.4f}")

    # 梯度下降更新参数
    optimizer.step()  # w = w - lr * ∇w, b = b - lr * ∇b

    if epoch < 3:
        print(f"  更新后w: {model.w.item():.4f}, b: {model.b.item():.4f}")

    losses.append(loss.item())
    params_history.append([model.w.item(), model.b.item()])

params_history = np.array(params_history)

# 可视化训练过程
if MATPLOTLIB_AVAILABLE:
    plt.subplot(2, 2, 4)
    plt.plot(losses, 'b-', linewidth=2)
    plt.xlabel('迭代次数')
    plt.ylabel('损失值')
    plt.title('损失函数下降过程')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('gradient_descent_basic.png', dpi=150, bbox_inches='tight')
    print("图形已保存为 gradient_descent_basic.png")
    # plt.show()  # 注释掉show()，因为使用Agg后端时无法显示窗口

# 5. 梯度下降的类型
print("\n=== 5. 梯度下降的类型 ===")
print("1. 批量梯度下降 (Batch Gradient Descent)")
print("   - 使用所有样本计算梯度")
print("   - 梯度准确，但计算慢")
print("   - 适合小数据集")

print("\n2. 随机梯度下降 (Stochastic Gradient Descent, SGD)")
print("   - 每次使用一个样本计算梯度")
print("   - 更新快，但有噪声")
print("   - 可能震荡")

print("\n3. 小批量梯度下降 (Mini-batch Gradient Descent)")
print("   - 折中方案：使用一个小批量样本")
print("   - 深度学习的标准选择")
print("   - batch_size是重要超参数")

# 6. 梯度下降的变体
print("\n=== 6. 梯度下降的优化变体 ===")
print("1. 带动量的SGD:")
print("   v = β*v + (1-β)*∇θ")
print("   θ = θ - η*v")
print("   可以加速收敛，减少震荡")

print("\n2. Adam (最常用):")
print("   结合了动量和自适应学习率")
print("   为每个参数计算一阶矩和二阶矩")
print("   自动调整学习率")

# 7. 实际例子：训练一个小网络
print("\n=== 7. 实际例子：训练一个简单网络 ===")

# 创建一个更复杂的问题
X = np.linspace(-3, 3, 100).reshape(-1, 1)
y = np.sin(X) + 0.1 * np.random.randn(100, 1)

# 转换为PyTorch张量
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32)


# 定义网络
class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(1, 10),
            nn.ReLU(),
            nn.Linear(10, 10),
            nn.ReLU(),
            nn.Linear(10, 1)
        )

    def forward(self, x):
        return self.net(x)


model = SimpleNN()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)  # 使用Adam优化器

# 训练
n_epochs = 500
train_losses = []

for epoch in range(n_epochs):
    # 前向传播
    y_pred = model(X_tensor)
    loss = criterion(y_pred, y_tensor)

    # 反向传播
    optimizer.zero_grad()
    loss.backward()

    # 梯度下降更新
    optimizer.step()

    train_losses.append(loss.item())

    if epoch % 100 == 0:
        print(f"Epoch {epoch:3d}, Loss: {loss.item():.4f}")

# 可视化结果
if MATPLOTLIB_AVAILABLE:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # 损失曲线
    axes[0].plot(train_losses)
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Loss')
    axes[0].set_title('训练损失下降曲线')
    axes[0].grid(True, alpha=0.3)
    axes[0].set_yscale('log')  # 对数坐标更清楚

    # 拟合结果
    with torch.no_grad():
        y_pred = model(X_tensor)

    axes[1].scatter(X, y, alpha=0.5, label='真实数据')
    axes[1].plot(X, y_pred.numpy(), 'r-', linewidth=2, label='模型预测')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('y')
    axes[1].set_title('梯度下降学到的函数')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('gradient_descent_training.png', dpi=150, bbox_inches='tight')
    print("图形已保存为 gradient_descent_training.png")
    # plt.show()  # 注释掉show()，因为使用Agg后端时无法显示窗口

# 8. 梯度下降的数学公式
print("\n=== 8. 梯度下降数学公式 ===")
print("1. 初始化参数: θ₀")
print("2. 迭代更新: θₜ₊₁ = θₜ - η * ∇L(θₜ)")
print("其中:")
print("  θ: 模型参数 (权重和偏置)")
print("  η: 学习率 (learning rate)")
print("  ∇L(θ): 损失函数在θ处的梯度")
print("  t: 迭代次数")

print("\n对于神经网络:")
print("1. 前向传播: 计算预测值 ŷ 和损失 L")
print("2. 反向传播: 通过链式法则计算梯度 ∂L/∂θ")
print("3. 参数更新: θ = θ - η * ∂L/∂θ")

# 9. 注意事项
print("\n=== 9. 梯度下降注意事项 ===")
print("1. 学习率选择: 太大发散，太小收敛慢")
print("2. 局部最小值: 可能陷入局部最优")
print("3. 鞍点问题: 梯度为0但不是最优点")
print("4. 梯度消失/爆炸: 深度网络常见问题")
print("5. 过拟合: 需要在训练集和验证集上监控")

print("\n=== 一句话总结 ===")
print("梯度下降：通过计算损失函数的梯度，")
print("沿着最陡下降方向更新参数，")
print("从而让模型逐渐学习到最优解。")
print("\n核心：参数 = 参数 - 学习率 × 梯度")