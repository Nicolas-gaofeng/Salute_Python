#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : base_conversion.py
@author     : zgf
@brief      : 进制转换
@attention  : life is short,I need python
"""


# =========================================  进制转换 =========================================
# 数据类型之间的转化。 int ---> str str (int) int(str)
# int----bool:非零及True,零即为False,True--->1 False--->0
# flag = True
flag = False
if flag:
    print(16 == 0b10000 == 0o20 == 0x10)  # 默认输入十进制 二进制0b、八进制0o、十六进制0x
    # 十进制与其他进制的转换
    # bin：将十进制转换成二进制并返回。
    a = bin(16)  # 转二进制 注意：上述转换后结果为字符串类型
    # oct：将十进制转化成八进制字符串并返回。
    b = oct(16)  # 转八进制 注意：上述转换后结果为字符串类型
    # hex：将十进制转化成十六进制字符串并返回。
    c = hex(16)  # 转十六进制 注意：上述转换后结果为字符串类型
    print(
        a,
        b,
        c,
        type(a),
        type(b),
        type(c),
    )  # 0b10000 0o20 0x10
    print(a == b == c)  # False
    # 其他进制转换十进制
    d = int(a, 2)  # 二进制转十进制
    e = int(b, 8)  # 八进制转十进制
    f = int(c, 16)  # 十六进制转十进制
    print(d, e, f)  # 16 16 16

    i = 4
    print(i.bit_length())  # 查询十进制转化成二进制占用的最小位数
