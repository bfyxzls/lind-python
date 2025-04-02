# 测试
from utils.tool import crc16

data = b"123456789"  # 测试数据
result = crc16(data)
print(f"CRC16 校验码: {result}")

print(f"CRC16 校验码: {hex(result)}")
