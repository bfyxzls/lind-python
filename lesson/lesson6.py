try:
    # 可能会引发异常的代码
    result = 10 / 0  # 这里会引发ZeroDivisionError
except ZeroDivisionError:
    # 处理特定的异常
    print("不能除以零！")
except Exception as e:
    # 处理其他所有异常
    print(f"发生了一个异常: {e}")
else:
    # 如果没有异常发生，则执行这部分
    print("计算成功:", result)
finally:
    # 无论是否发生异常，都会执行这部分
    print("结束处理。")

# 自定义异常
class MyCustomError(Exception):
    pass

def check_value(x):
    if x < 0:
        raise MyCustomError("值不能为负数！")

try:
    check_value(-1)
except MyCustomError as e:
    print(e)