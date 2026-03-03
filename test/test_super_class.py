class Person:
    Des = "人类"  # 类（静态）属性

    def __init__(self, w: int, b: int) -> None:  # 表示返回 None,构造方法必须返回None
        super().__init__()
        self.w = w
        self.b = b

    # 实例方法,第一个参数是self
    def forward(self, x: int):
        return self.w * x + self.b

    # 类方法
    # 类方法，第一个参数是类本身（通常命名为cls），可以通过这个参数访问类属性，也可以修改类状态。它也可以被实例调用，但传入的第一个参数仍然是类。类方法常用于创建工厂方法，返回类的实例。
    @classmethod
    def class_method(cls):
        print(f"类: {cls.__name__}")
        return f"类方法，可访问类属性 {cls.Des}"

    # 静态方法
    @staticmethod
    def static_method():
        return "静态方法，无需实例或类参数" + Person.Des


class Male(Person):
    def __int__(self) -> None:  # 表示返回 None,构造方法必须返回None
        super().__init__(self, 1, 2)

    def do(self, x: int):
        print(super().forward(x))


male = Male(1, 2)
male.do(10)
Male.class_method()
print(Male.static_method())
