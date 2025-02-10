age = 18

if age < 18:
    print("未成年人")
elif age == 18:
    print("刚成年")
else:
    print("成年人")

result = "成人" if age >= 18 else "未成年人"
print(result)

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 1  # 增加计数

for i in range(10):
    if i == 5:
        break  # 当 i 等于 5 时退出循环
    print(i)

for i in range(5):
    if i == 2:
        continue  # 跳过 i 等于 2 的情况
    print(i)

for i in range(3):
    print(i)
else:
    print("循环正常结束")  # 当 for 循环没有被 break 终止时执行

