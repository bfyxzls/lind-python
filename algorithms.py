# 斐波那契数列
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print("fibonacci=%d"  %(fibonacci(6)))
