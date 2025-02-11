FILE_NAME = "../resources/json.txt"
FILE_NAME_JSON = "../resources/json.json"

with open(FILE_NAME, 'r') as file:
    content = file.read()
    print(content)

with open(FILE_NAME, 'r') as file:
    part = file.read(10)  # 读取前10个字符
    print(part)

# with open(FILE_NAME, 'a') as file:
#     file.write("Appending a new line.\n")

import json

# 打开并读取 JSON 文件
with open(FILE_NAME_JSON, 'r', encoding='utf-8') as file:
    data = json.load(file)  # 将 JSON 数据解析为 Python 对象

# 输出解析后的数据
print(data['0'])  # 访问特定字段
print(data['0']['name'])  # 输出课程列表


# 使用编码的方法手动赋值
# 定义地址类（可选）
class Address:
    def __init__(self, city, zip_code):
        self.city = city
        self.zip_code = zip_code

    def __repr__(self):
        return f"Address(city={self.city}, zip_code={self.zip_code})"


# 定义人员类
class Person:
    def __init__(self, name, age, is_student, courses, address):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.courses = courses
        self.address = address

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, is_student={self.is_student}, courses={self.courses}, address={self.address})"


# 读取 JSON 文件并解析内容
try:
    with open('../resources/person.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  # 将 JSON 数据解析为 Python 对象

        # 创建地址对象
        address = Address(city=data['address']['city'], zip_code=data['address']['zip_code'])

        # 创建人员对象
        person = Person(
            name=data['name'],
            age=data['age'],
            is_student=data['is_student'],
            courses=data['courses'],
            address=address
        )

        # 输出结果
        print(person)

except FileNotFoundError:
    print("文件未找到！")
except json.JSONDecodeError:
    print("文件不是有效的 JSON 格式！")
except Exception as e:
    print(f"发生了其他错误: {e}")

# 使用dataclasses模块自动解析
from dataclasses import dataclass


@dataclass
class Address2:
    city: str
    zip_code: str


@dataclass
class Person2:
    name: str
    age: int
    is_student: bool
    courses: list
    address: Address2


with open('../resources/person.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    # 创建地址对象
    address = Address2(**data['address'])

    # 创建人员对象
    person = Person2(
        name=data['name'],
        age=data['age'],
        is_student=data['is_student'],
        courses=data['courses'],
        address=address
    )

    # 输出结果
    print(person)

# 使用Pydantic模块自动解析
from pydantic import BaseModel
from typing import List


class Address3(BaseModel):
    city: str
    zip_code: str


class Person3(BaseModel):
    name: str
    age: int
    is_student: bool
    courses: List[str]
    address: Address3


with open('../resources/person.json', 'r', encoding='utf-8') as file:
    # 加载内容转为json对象
    data = json.load(file)
    # 将字典转换为 JSON 字符串
    str=json.dumps(data)
    person3 = Person3.model_validate_json(str)
    # 输出结果
    print(person3)
