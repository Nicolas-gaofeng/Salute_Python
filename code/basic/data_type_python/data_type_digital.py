#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : data_type_digital.py
@author     : zgf
@brief      : 数据类型- 数字型
@attention  : life is short,I need python
"""


# =========================================  数据类型 =========================================
# 数据类型可以分为 数字型 和 非数字型
# 数字型： 整型 (int) 浮点型（float） 布尔型（bool）真 True 非 0 数 —— 非零即真 假 False 0 复数型 (complex)
# 非数字型 -字符串 -列表 -元组 -字典
# flag = True
flag = False
if flag:
    pass


# =========================================  数字类型 - 字节（bytes） =========================================
# python的基础数据类型之一，他和str相当于双胞胎，str拥有的所有方法，bytes类型都适用
# 内部编码方式：非unicode
# 你想将一部分内容（字符串）写入文件，或者通过网络socket传输，这样这部分内容（字符串）必须转化成bytes才可以进行
# 平时你代码中，使用字符串。
# flag = True
flag = False
if flag:
    i = b"alex"
    print(i, type(i))  # 查询十进制转化成二进制占用的最小位数


# =========================================  数字类型 - 整型（int） =========================================
# 整型是不可变类型
# 数据类型之间的转化。 int ---> str str (int) int(str) - int----bool:非零及True,零即为False,True--->1 False--->0
# flag = True
flag = False
if flag:
    age = 18
    print(age, type(age))


# =========================================  1.数字类型 - 浮点型（float） =========================================
# 浮点型是不可变类型
# 计算机采用二进制小数来表示浮点数的小数部分
# 部分小数不能用二进制小数完全表示,通常情况下不会影响计算精度
# flag = True
flag = False
if flag:
    height = 1.83
    print(height, type(height))
    # 不确定小数问题
    print((0.1 + 0.2) == 0.3)  # False
    print(0.1 + 0.2)  # 0.30000000000000004
    print(0.1 + 0.7)  # 0.7999999999999999
    a = 3 * 0.1
    print(a)
    # round() 方法返回浮点数x的四舍五入值。
    b = round(a, 1)
    print(b, b == 0.3)


# =========================================  3.布尔类型 =========================================
# 主要用于逻辑运算
# 真 True 非 0 数 —— 非零即真 假 False 0
# 空字符串对应 bool False
# 非空即True
# flag = True
flag = False
if flag:
    y = 2 > 1
    print(y, type(y))
    l = ""
    print(l, type(bool(l)))


# =========================================  1.数字类型 - 复数（complex）a+bj =========================================
# 大写J或小写j均可
# 虚部系数为1时，需要显式写出
# 3是实部，4是虚部
# flag = True
flag = False
if flag:
    a = 3 + 4j
    print(a, type(a))
    print(3 + 4j, 2 + 5j, type(3 + 4j), type(2 + 5j))
    print(2 + 1j)  # 虚部系数为1时，需要显式写出
