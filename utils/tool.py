import json
import csv
import pathlib
import subprocess
import math
import time

import torch


def load_text(path):
    with open(path, "r") as f:
        return f.read()


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def load_csv(path):
    with open(path, "r") as f:
        fcsv = csv.DictReader(f)
        for row in fcsv:
            yield row


def iter_json(js):
    for k, v in js.items():
        if isinstance(v, str):
            yield v
        if isinstance(v, dict):
            yield iter_json(v)


def path_validate(path):
    """
    @desc: checkout
    :param path:
    :return:
    """
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    return path


def exec_cmd(cmd):
    proc = subprocess.call(
        [cmd],
        close_fds=True,  # here
        # ...
        shell=True,
        stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE,
        # encoding="utf-8",
        # timeout=1
    )
    return proc


def format_credit(value):
    if not value:
        return 0.0
    return math.ceil(value * 100) / 100


import time


def measure_runtime(func, *args, **kwargs):
    """
    测量函数的运行时间。

    参数:
        func: 要测量的函数。
        *args: 函数的参数。
        **kwargs: 函数的关键字参数。

    返回:
        runtime: 函数的运行时间（秒）。
        result: 函数的返回值。
    """
    start_time = time.time()  # 获取开始时间
    result = func(*args, **kwargs)  # 调用函数
    end_time = time.time()  # 获取结束时间
    runtime = end_time - start_time  # 计算运行时间
    return runtime, result  # 返回运行时间和函数的返回值 runtime, result = measure_runtime(example_function) print(f"运行时间: {runtime:.6f} 秒")

def crc16(data: bytes, poly: int = 0x1021, init_crc: int = 0xFFFF) -> int:
    """
    CRC16 算法实现
    :param data: 待校验的数据（字节序列）
    :param poly: 生成多项式，默认使用 0x1021
    :param init_crc: 初始 CRC 值，通常为 0xFFFF
    :return: 计算出的 CRC 校验码
    """
    crc = init_crc

    for byte in data:
        crc ^= (byte << 8)  # 将当前字节与 CRC 高位异或
        for _ in range(8):  # 对每一位进行处理
            if crc & 0x8000:  # 检查最高位是否为 1
                crc = (crc << 1) ^ poly  # 左移并与多项式异或
            else:
                crc <<= 1  # 左移
            crc &= 0xFFFF  # 保证 CRC 为 16 位
    return crc