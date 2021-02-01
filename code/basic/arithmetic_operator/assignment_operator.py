#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : assignment_operator.py
@author     : zgf
@brief      : python赋值运算符
@attention  : life is short,I need python
"""


# =========================================  赋值运算 =========================================
# 使用 = 可以给变量赋值
# flag = True
flag = False
if flag:
    a = 10
    b = 20
    a += b
    print(a)
    a -= b
    print(a)
    a *= b
    print(a)
    a /= b
    print(a)


# =========================================  赋值运算 - 面试题 =========================================
# 面试题 += 列表
# 列表变量使用 + 不会做相加再赋值的操作 ！ 本质上是在调用列表的 extend 方法
# flag = True
flag = False
if flag:

    def demo(num, num_list):
        print("函数开始")
        # num = num + num
        num += num
        # 列表变量使用 + 不会做相加再赋值的操作 ！
        # num_list = num_list + num_list
        # 本质上是在调用列表的 extend 方法
        num_list += num_list
        # num_list.extend(num_list)
        print(num)
        print(num_list)
        print("函数完成")

    gl_num = 9
    gl_list = [1, 2, 3]
    demo(gl_num, gl_list)
    print(gl_num)
    print(gl_list)
