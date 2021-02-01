#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : variable_local_global.py
@author     : zgf
@brief      : python局部/全局变量
@attention  : life is short,I need python
"""


# =========================================  全局变量 - 定义 =========================================
# 全局变量是在 函数外部定义的变量，所有函数内部都可以使用这个变量
# flag = True
flag = False
if flag:
    """定义一个全局变量"""
    num = 10

    def demo1():
        print(num)

    def demo2():
        print(num)

    demo1()
    demo2()
    print("over")


# =========================================  全局变量 - 修改全局变量=========================================
# 不允许直接修改全局变量的引用 —— 使用赋值语句修改全局变量的值
# 如果在函数中需要修改全局变量，需要使用 global 进行声明
# flag = True
flag = False
if flag:
    num = 10

    def demo1():
        # 注意：只是在函数内部定义了一个局部变量而已，不会修改到全局变量，只是变量名相同 —— 在函数内部不能直接修改全局变量的值
        num = 100
        print(num)

    def demo2():
        print(num)

    def demo3():
        # global关键字，告诉Python解释器num是一个全局变量
        global num
        # 只是定义了一个局部变量，不会修改到全局变量，只是变量名相同而已
        num = 100
        print(num)

    print("不允许直接修改全局变量的引用".center(50, "*"))
    demo1()
    demo2()
    print("over".center(50, "*"))

    print("使用global声明修改全局变量的引用".center(50, "*"))
    demo3()
    demo1()
    demo2()
    print("over".center(50, "*"))


# =========================================  局部变量 =========================================
# 局部变量 是在 函数内部 定义的变量，只能在函数内部使用
# 函数执行结束后，函数内部的局部变量，会被系统回收
# 不同的函数，可以定义相同的名字的局部变量，但是 彼此之间 不会产生影响
# flag = True
flag = False
if flag:

    def demo1():
        num = 10
        print(num)
        num = 20
        print("修改后 %d" % num)

    def demo2():
        num = 100
        print(num)

    demo1()
    demo2()
    print("over")
