def printName(name):
    print("Hello, " + name + "!")

if __name__ == '__main__': #如果被其它模块引用了，那这行就不会执行了
    printName("测试print方法")