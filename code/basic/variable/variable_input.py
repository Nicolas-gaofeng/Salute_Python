#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : variable_input.py
@author     : zgf
@brief      : python变量输入
@attention  : life is short,I need python
"""


# =========================================  变量的输入 =========================================
# 使用解释器执行，如果要输出变量的内容，必须要使用 print 函数
# 如果要获取用户在 键盘上的输入信息，需要使用到 input 函数
# input:函数接受一个标准输入数据，返回为 string 类型，即数据输出的是一个字符串 。
# 用户输入的 任何内容 Python 都认为是一个字符串
# 变量中存储的值，就是可以变的
# flag = True
flag = False
if flag:
    x = input("请输入一个数字：")
    print(x, type(x))

    # 1.输入苹果单价，并将苹果单价转换成小数
    price = float(input("请输入苹果价格："))
    # 2.要求苹果重量，并将苹果重量转换成小数
    weight = float(input("请输入苹果重量："))
    # 3>计算付款金额
    money = price * weight
    print(money)


