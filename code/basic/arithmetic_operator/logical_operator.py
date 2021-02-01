#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : logical_operator.py
@author     : zgf
@brief      : python逻辑运算符
@attention  : life is short,I need python
"""


# =========================================  逻辑运算 =========================================
# 与运算，True和False进行与运算结果应该为False
# 或运算，True和False进行或运算结果应该为True
# 非运算，将结果置非，即True变False,False变True
# 复合逻辑运算的优先级 非 > 与 > 或
# 优先级 （）> not >and>or
# 0对应的bool值为False,非0都为True
#  x or y if x is True,return x
#  求and与or相反
# flag = True
flag = False
if flag:
    a = 10
    b = 8
    c = 12
    print((a > b) and (b > c))  # 与
    print((a > b) or (b > c))  # 或
    print(not (a > b))  # 非
    print(a == b)  # 相等

    print(True and False)
    print(True or False)
    print(not (True and False))

    # bool ：用于将给定参数转换为布尔类型，如果没有参数，返回False。 ***
    print(bool(1 < 2 and 3 > 4 or 5 < 6 and 9 > 2 or 3 > 1))
    print(bool("fdsjkfl"))

    """数字逻辑运算"""
    #  x or y if x is True,return x
    #  x and y if x is True,return y
    print(1 or 2)  # 1
    print(1 and 2)  # 2
    print(5 or 2)  # 5
    print(5 and 2)  # 2
    print(0 or 3 and 5 or 4)  # 5


# =========================================  逻辑运算 =========================================
#
# flag = True
flag = False
if flag:

    """逻辑运算作为指示条件"""
    n = 2800
    while True:
        m = eval(input("请输入一个正整数："))
        if m == n:
            print("你猜对啦")
            break
        elif m > n:
            print("太大了")
        else:
            print("太小了")

    """逻辑运算作为掩码"""
    import numpy as np

    x = np.array([[1, 3, 2, 5, 7]])  # 定义 numpy数组
    print(x > 3)  # [[False False False  True  True]]
    print(x[x > 3])  # [5 7]
