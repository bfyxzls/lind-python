import mypackage  # 导入包，根据__init__.py文件的内容，导入了mypackage下的所有模坫
from mypackage.module2 import Calculator  # 导入某个模块里的某个资源

print(mypackage.greet("Alice"))  # "Hello, Alice!"
Calculator().add(1, 2)  # 使用类中的实例方法

Calculator.do(1,2)
