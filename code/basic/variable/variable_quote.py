#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : variable_output.py
@author     : zgf
@brief      : python变量引用
@attention  : life is short,I need python
"""


# =========================================  变量的引用 =========================================
# 函数的参数传递以及返回值都是靠引用传递的
# is比较id,判断的是两个变量的id值是否相同。是判断两个标识符是不是引用同一个对象
# is not 是判断两个标识符是不是引用不同对象
# ==比较值
# 在内存中id都是唯一的，如果两个变量指向的值的id相同，就证明他们在内存中是同一个。
# 与None值比较 判断某个变量是否为None时，请使用is 而不是==
# 如果is是True, == 一定是True。
# flag = True
flag = False
if flag:
    a = "sdasdsadasdasdasdasdasdddddddddddddddddddddddddddfsafdafaag.62952a9fadggagag"
    b = "sdasdsadasdasdasdasdasdddddddddddddddddddddddddddfsafdafaag.62952a9fadggagag"
    print(a is b)  #  用于判断 两个变量 引用对象是否为同一个
    print(a is None)
    print(a == b)  # 用于判断引用变量的值 是否相等
    print(a is not b)
