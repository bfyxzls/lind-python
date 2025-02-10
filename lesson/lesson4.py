def add(a, b):
    """
    返回两个数的和。
    """
    return a + b

print(add(1, 2))  # 3

def greet(name="世界"):
    print(f"你好, {name}!")

greet()          # 输出: 你好, 世界!
greet("Alice")  # 输出: 你好, Alice!

def my_function(*args, **kwargs):
    print(args)     # 元组
    print(kwargs)   # 字典

my_function(1, 2, 3, name="Alice", age=25)
# 输出:
# (1, 2, 3)
# {'name': 'Alice', 'age': 25}

class People:
    def __init__(self, name):
        self.name = name  # 属性

    def __str__(self):  # 当类以字符串返回时，执行这个魔法方法
        return f"dog string {self.name}"

    def bark(self):  # 方法
        print(f"{self.name} says chinese!")

people = People("Buddy")  # 创建对象
people.bark()          # 输出: Buddy says chinese!

print("dog string",people)

class Animal:
    def speak(self):
        print("动物发声")

class Dog(Animal):  # Dog 继承 Animal
    def bark(self):
        print("汪汪!")
    def speak(self):  # 重写父类方法
        print("动物发声,汪汪!")

class Cat(Animal):  # Cat 也继承 Animal
    def meow(self):
        print("喵喵!")

my_dog = Dog()
my_dog.speak()  # 输出: 动物发声
my_dog.bark()   # 输出: 汪汪!

