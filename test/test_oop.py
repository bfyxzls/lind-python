class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("This animal makes a sound.", self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类的__init__方法
        self.breed = breed

    def speak(self):
        super().speak()  # 调用父类的speak方法
        print("Woof!", self.breed)


dog = Dog("Buddy", "Golden Retriever")
dog.speak()
# 输出：
# This animal makes a sound. Buddy
# Woof! Golden Retriever
