import utils.tool # 导入外部包
from utils.tool import load_text # 导入load_text方法，可直接使用方法名调用
from utils.tool import exec_cmd

def printName(name):
    print("Hello, " + name + "!")


if __name__ == '__main__':  # 如果被其它模块引用了，那这行就不会执行了
    printName("测试print方法")
    utils.tool.exec_cmd("echo 'ok'")
    exec_cmd("ls")