import mypackage  # 导入包，根据__init__.py文件的内容，导入了mypackage下的所有模坫

print(mypackage.greet("Alice"))  # "Hello, Alice!"

mypackage.Calculator().add(1, 2)  # 使用类中的实例方法

mypackage.Calculator.do(1, 2)
