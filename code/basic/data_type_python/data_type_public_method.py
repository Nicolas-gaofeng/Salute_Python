#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : data_type_public_method.py
@author     : zgf
@brief      : 容器公共方法
@attention  : life is short,I need python
"""


# =========================================  存在运算 =========================================
# 元素 in 列表/字符串
# flag = True
flag = False
if flag:
    cars = ["BYD", "BMW", "AUDI", "TOYOTA"]
    print("BMW" in cars)
    print("BENZ" in cars)
    print("BMW" not in cars)
    print("BENZ" not in cars)
