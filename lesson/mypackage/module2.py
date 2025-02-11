__all__ = ['Calculator'] # 定义一个模块或包中可以被 from module import * 语句导入的公共接口。

class Calculator:
    # 实例一个实例方法
    def add(self, a, b):
        return a + b

    # 定义一个静态方法
    @staticmethod
    def do(a,b):
        return a+b