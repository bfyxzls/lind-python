my_bytes = b'Hello, World!'  # 创建字节对象
first_byte = my_bytes[0]  # 访问第一个字节
print("first_byte",first_byte)

my_bytearray = bytearray(b'Hello')  # 创建字节数组
my_bytearray[0] = 72 # 将数组的第1个位置改为H
print("my_bytearray",my_bytearray);