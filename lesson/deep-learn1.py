import torch
# torch的使用
# 二行二列的矩阵
X = torch.arange(4, dtype=torch.float32).reshape((2, 2))
# 这个也是二行二列的
Y = torch.tensor([[1, 2], [2, 3]])

print(torch.cat((X, Y), dim=0))  # 两个张量的拼接，4行2列

print(torch.cat((X, Y), dim=1))  # 两个张量的拼接，2行4列

print(X + Y)

# 纬度一样，但行列不一样的两个张量，进行相加，得到(3,2)的矩阵，这叫广播机制(broadcasting mechanism)
a = torch.arange(3).reshape(3, 1)
b = torch.arange(2).reshape(1, 2)
print(a + b)

c = torch.tensor([[1, 2], [2, 3], [4, 5], [6, 7], [8, 9]])
print("c[-1]")
print(c[-1])  # 最后一个元素
print("c[1:4]")
print(c[1:4])  # 第2,3,4号元素

c[1,1]=9 # 第二行第二列改成9
print(c)

before=id(Y) # Y的内存地址
Y=Y+X
print(before==id(Y)) #False

# 不申请新的内存开乐,X[:]=X+Y,X+=Y都是原地操作
before=id(X)
X+=Y
print(id(X)==before)