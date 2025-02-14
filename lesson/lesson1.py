from enum import Enum
from typing import List, Tuple, Set, Dict, Optional, Union, Any

my_bytes = b'Hello, World!'  # 创建字节对象
first_byte = my_bytes[0]  # 访问第一个字节
print("first_byte",first_byte)

my_bytearray = bytearray(b'Hello')  # 创建字节数组
my_bytearray[0] = 72 # 将数组的第1个位置改为H
print("my_bytearray",my_bytearray);

age: int = 25 # 整数
height: float = 1.75 # 浮点数
name: str = "Alice" # 字符串
is_active: bool = True # 布尔值
numbers: List[int] = [1, 2, 3] # 列表
point: Tuple[int, int] = (1, 2) # 元组
unique_numbers: Set[int] = {1, 2, 3} # 集合
user: Dict[str, str] = {"name": "Alice", "email": "alice@example.com"}
maybe_name: Optional[str] = None # 可选类型
value: Union[int, str] = 42 # 联合类型
value = "hello"
class Color(Enum): # 枚举类型
    RED = 1
    GREEN = 2
    BLUE = 3
color: Color = Color.RED

value_any: Any = 42 # 任意类型
value_any = "hello"

print("age",age)
print("height",height)
print("name",name)
print("is_active",is_active)
print("numbers",numbers)
print("point",point)
print("unique_numbers",unique_numbers)
print("user",user)
print("maybe_name",maybe_name)
print("value",value)
print("color",color)
print("value_any",value_any)