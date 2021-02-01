#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : comparison_operator.py
@author     : zgf
@brief      : python比较运算符
@attention  : life is short,I need python
"""


# =========================================  比较运算符 =========================================
#
# flag = True
flag = False
if flag:
    a = 10
    b = 20
    print(a == b)
    print(a != b)
    print(a > b)
    print(a < b)
    print(a >= b)
    print(a <= b)
    # 非空
    ls = [1]
    if ls:  # 数据结构不为空、变量不为0、None、False 则条件成立
        print("非空")
    else:
        print("空的")
