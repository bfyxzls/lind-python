import matplotlib

matplotlib.use('Agg')  # 使用非交互式后端，避免GUI相关错误
import matplotlib.pyplot as plt

# 设置中文字体，避免中文显示警告
plt.rcParams['font.family'] = 'sans-serif'

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'Arial Unicode MS']  # 可以尝试多个字体选项
plt.rcParams['axes.unicode_minus'] = False  # 解决保存

import numpy as np


def f(x):
    return x ** 2


# 定义导数 dy/dx = 2x
def df(x):
    return 2 * x


# 可视化函数
x_vals = np.linspace(-3, 3, 100)
y_vals = f(x_vals)

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


# 二维函数示例，多元函数
def f2d(x1, x2):
    return x1 ** 2 + x2 ** 2


def gradient_f2d(x1, x2):
    """返回梯度向量 [∂f/∂x1, ∂f/∂x2]"""
    return np.array([2 * x1, 2 * x2])


# 可视化二维函数的梯度
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

# 生成图像
plt.tight_layout()
plt.savefig('gradient_descent_basic.png', dpi=150, bbox_inches='tight')
print("图形已保存为 gradient_descent_basic.png")
