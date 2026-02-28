import torch
import numpy as np

# 尝试导入matplotlib，如果失败则跳过绘图部分
try:
    import matplotlib
    matplotlib.use('Agg')  # 使用非交互式后端，避免GUI相关错误
    import matplotlib.pyplot as plt
    # 设置中文字体，避免中文显示警告
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 使用黑体或微软雅黑
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题
    MATPLOTLIB_AVAILABLE = True
except (ImportError, ModuleNotFoundError) as e:
    print(f"警告: matplotlib导入失败 ({e})，将跳过绘图部分")
    MATPLOTLIB_AVAILABLE = False
    plt = None

print("=== 用最简单例子解释神经网络核心概念 ===\n")

# 1. 从最简单的线性回归说起
print("=== 1. 线性回归例子: y = wx + b ===")
# 假设我们要拟合 y = 2x + 1
x = torch.tensor([1.0, 2.0, 3.0, 4.0])
y_true = 2 * x + 1
print(f"输入x: {x}")
print(f"真实y: {y_true}")
print("公式: y = wx + b")
print("其中: w是权重(weight), b是偏置(bias)")

# 2. 什么是权重(Weight)?
print("\n=== 2. 权重(Weight)是什么? ===")
print("权重决定了输入对输出的影响程度")
print("在 y = wx + b 中:")
print("- 如果 w=2: x增加1 → y增加2")
print("- 如果 w=0.5: x增加1 → y增加0.5")
print("- 如果 w=-1: x增加1 → y减少1")

# 可视化权重的意义
if MATPLOTLIB_AVAILABLE:
    x_range = np.linspace(0, 5, 100)
    w_values = [0.5, 2, -1]
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    for w in w_values:
        y = w * x_range
        plt.plot(x_range, y, label=f'w={w}, y={w}x')
    plt.xlabel('输入 x')
    plt.ylabel('输出 y')
    plt.title('不同权重w的影响 (y=wx)')
    plt.legend()
    plt.grid(True)

# 3. 什么是偏置(Bias)?
print("\n=== 3. 偏置(Bias)是什么? ===")
print("偏置决定了输出线的起始位置")
print("在 y = wx + b 中:")
print("- 如果 b=0: 直线通过原点")
print("- 如果 b=1: 整体上移1单位")
print("- 如果 b=-1: 整体下移1单位")

# 可视化偏置的意义
if MATPLOTLIB_AVAILABLE:
    plt.subplot(1, 2, 2)
    w = 2
    b_values = [-2, 0, 2]
    for b in b_values:
        y = w * x_range + b
        plt.plot(x_range, y, label=f'b={b}, y=2x+{b}')
    plt.xlabel('输入 x')
    plt.ylabel('输出 y')
    plt.title('不同偏置b的影响 (y=2x+b)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('weight_bias_visualization.png', dpi=150, bbox_inches='tight')
    print("图形已保存为 weight_bias_visualization.png")
    # plt.show()  # 注释掉show()，因为使用Agg后端时无法显示窗口

# 4. 从一维到多维：权重矩阵
print("\n=== 4. 权重矩阵(Weight Matrix) ===")
print("当有多个输入和多个输出时，权重变成矩阵")

# 例子：3个输入特征，2个输出
input_size = 3
output_size = 2

# 权重矩阵 W: 形状为 (output_size, input_size)
# 每一行对应一个输出的权重
W = torch.tensor([[0.1, 0.2, 0.3],  # 第一个输出的权重
                  [0.4, 0.5, 0.6]], dtype=torch.float32)  # 第二个输出的权重

# 输入向量 x: 形状为 (input_size,)
x = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# 偏置向量 b: 形状为 (output_size,)
b = torch.tensor([0.1, 0.2], dtype=torch.float32)

print(f"权重矩阵 W (形状: {W.shape}):")
print(f"第一行 [0.1, 0.2, 0.3] → 控制第一个输出")
print(f"第二行 [0.4, 0.5, 0.6] → 控制第二个输出")
print(f"\n输入向量 x (3个特征): {x}")
print(f"偏置向量 b (2个偏置): {b}")

# 5. 什么是线性变换(Linear Transformation)?
print("\n=== 5. 线性变换(Linear Transformation) ===")
print("线性变换 = 权重矩阵 × 输入向量 + 偏置")
print("公式: y = Wx + b")

# 手动计算线性变换
y1 = W[0, 0] * x[0] + W[0, 1] * x[1] + W[0, 2] * x[2] + b[0]
y2 = W[1, 0] * x[0] + W[1, 1] * x[1] + W[1, 2] * x[2] + b[1]

print(f"\n手动计算:")
print(f"y1 = 0.1 * 1.0 + 0.2 * 2.0 + 0.3 * 3.0 + 0.1 = {y1:.2f}")
print(f"y2 = 0.4 * 1.0 + 0.5 * 2.0 + 0.6 * 3.0 + 0.2 = {y2:.2f}")

# 使用矩阵乘法计算
y_matrix = torch.matmul(W, x) + b
print(f"\n矩阵计算: y = Wx + b")
print(f"y = {y_matrix}")

# 6. 直观理解：神经元比喻
print("\n=== 6. 神经元比喻 ===")
print("可以把每个输出看作一个神经元:")
print("\n神经元1:")
print("  - 接收3个输入: x1=1.0, x2=2.0, x3=3.0")
print("  - 有自己的权重: w1=0.1, w2=0.2, w3=0.3")
print("  - 有自己的偏置: b1=0.1")
print("  - 计算: 0.1 * 1.0 + 0.2 * 2.0 + 0.3 * 3.0 + 0.1 = 1.5")

print("\n神经元2:")
print("  - 接收3个输入: x1=1.0, x2=2.0, x3=3.0")
print("  - 有自己的权重: w1=0.4, w2=0.5, w3=0.6")
print("  - 有自己的偏置: b2=0.2")
print("  - 计算: 0.4 * 1.0 + 0.5 * 2.0 + 0.6 * 3.0 + 0.2 = 3.4")

# 7. 线性变换的性质
print("\n=== 7. 线性变换的性质 ===")
print("性质1: 可加性")
x1 = torch.tensor([1.0, 2.0])
x2 = torch.tensor([3.0, 4.0])
W_simple = torch.tensor([[0.5, 0.5]], dtype=torch.float32)
b_simple = torch.tensor([0.1], dtype=torch.float32)

result1 = torch.matmul(W_simple, x1) + b_simple
result2 = torch.matmul(W_simple, x2) + b_simple
result_sum = torch.matmul(W_simple, (x1 + x2)) + b_simple

print(f"f(x1) = {result1.item():.2f}")
print(f"f(x2) = {result2.item():.2f}")
print(f"f(x1+x2) = {result_sum.item():.2f}")
print(f"f(x1)+f(x2) = {(result1 + result2).item():.2f}")

print("\n性质2: 齐次性（乘以常数）")
alpha = 2.0
result_scaled = torch.matmul(W_simple, alpha * x1) + b_simple
print(f"f({alpha}*x1) = {result_scaled.item():.2f}")
print(f"{alpha}*f(x1) = {(alpha * result1).item():.2f}")

# 8. 在神经网络中的作用
print("\n=== 8. 在神经网络中的作用 ===")


# 创建一个简单的神经网络
class SimpleNet(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # 这就是权重矩阵和偏置
        self.fc1 = torch.nn.Linear(3, 4)  # 输入3维，输出4维
        self.fc2 = torch.nn.Linear(4, 2)  # 输入4维，输出2维

    def forward(self, x):
        x = self.fc1(x)  # 第一次线性变换: y = W1x + b1
        x = torch.relu(x)  # 非线性激活
        x = self.fc2(x)  # 第二次线性变换: y = W2x + b2
        return x


# 创建网络实例
model = SimpleNet()
print(f"模型结构:")
print(model)
print(f"\n第一层权重形状: {model.fc1.weight.shape}")  # 4x3
print(f"第一层偏置形状: {model.fc1.bias.shape}")  # 4
print(f"第二层权重形状: {model.fc2.weight.shape}")  # 2x4
print(f"第二层偏置形状: {model.fc2.bias.shape}")  # 2

# 前向传播演示
input_data = torch.tensor([[1.0, 2.0, 3.0]])
output = model(input_data)
print(f"\n输入: {input_data}")
print(f"输出: {output}")

# 9. 总结表格
print("\n=== 9. 概念总结 ===")
summary = {
    "概念": ["权重(Weight)", "权重矩阵(W)", "偏置(Bias)", "线性变换", "输入向量(x)", "输出向量(y)"],
    "比喻": ["输入的重要性", "神经元的连接强度表", "基准线/门槛", "加权求和+平移", "特征值", "预测结果"],
    "形状": ["单个值", "(输出维度, 输入维度)", "(输出维度,)", "y=Wx+b", "(输入维度,)", "(输出维度,)"],
    "作用": ["控制输入影响力", "多对多映射", "调整输出零点", "线性特征组合", "输入数据", "计算结果"]
}

for i in range(len(summary["概念"])):
    print(f"{summary['概念'][i]:<10} | {summary['比喻'][i]:<20} | {summary['形状'][i]:<20} | {summary['作用'][i]}")

print("\n=== 一句话总结 ===")
print("权重矩阵决定每个输入对每个输出的影响程度")
print("偏置决定输出的基准位置")
print("线性变换 = 加权求和 + 平移")
print("神经网络 = 多个线性变换 + 非线性激活函数的堆叠")