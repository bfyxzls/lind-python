# 数据预处理，将数据读取进来，通过机器学习的方法对数据进行处理
# 创建一个人工数据集，csv文件，逗号分割内容
import os

import pandas as pd

os.makedirs(os.path.join('..', 'data'), exist_ok=True)  # 创建文件夹
data_file = os.path.join('..', 'data', 'house_tiny.csv')  # 创建文件
with open(data_file, 'w') as f:
    f.write('name,number,price\n')
    f.write('lind,1,3000\n')
    f.write('shop,2,5000\n')
    f.write('phone,3,Nan\n')
    f.write('NaN,NaN,100\n')

# 读取csv文件，将'Nan'和'NaN'识别为缺失值
data = pd.read_csv(data_file, na_values=['Nan', 'NaN', 'nan'])
print(data)

# 处理缺失的数据，是数据科学家要做的事，最常用的方法就是丢掉它；或者取一个差值，输入特征
# 对于数值类型：将nan的数值填充为均值
# 对于字符类型：可以用众数（mode）、前向填充（ffill）、后向填充（bfill）或固定值填充

# 处理数值列（number 和 price）
inputs, outputs = data.iloc[:, 1:3], data.iloc[:, 2] # data.iloc[:, 0:2]取前两列索引为0和1的； data.iloc[:, 2]取第3列索引为2的
# 确保数值列被转换为数值类型（字符串会被转换为NaN）
inputs = inputs.apply(pd.to_numeric, errors='coerce')
inputs = inputs.fillna(inputs.mean())
print("处理后的数值列：")
print(inputs)

# 处理字符类型列（name）
name_col = data.iloc[:, 0]  # 取第一列 name
print("\n原始 name 列：")
print(name_col)

# 方法1：用众数（mode）填充 - 最常见的方法
# 如果有多于一个众数，取第一个
name_col_mode = name_col.fillna(name_col.mode()[0] if len(name_col.mode()) > 0 else 'Unknown')
print("\n方法1 - 用众数填充 name 列：")
print(name_col_mode)

# 方法2：用前向填充（forward fill）- 用前一个非空值填充
name_col_ffill = name_col.ffill()  # 等同于 fillna(method='ffill')，但更推荐使用
print("\n方法2 - 用前向填充 name 列：")
print(name_col_ffill)

# 方法3：用固定值填充
name_col_fixed = name_col.fillna('Unknown')
print("\n方法3 - 用固定值 'Unknown' 填充 name 列：")
print(name_col_fixed)

# 将处理后的 name 列合并回数据
data['name'] = name_col_mode  # 这里使用众数填充的方法
print("\n最终处理后的完整数据：")
print(data)
