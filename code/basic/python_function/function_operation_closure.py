#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : function_operation_closure.py
@author     : zgf
@brief      : 闭包函数
@attention  : life is short,I need python
"""


# ========================================= 函数 -  闭包 =========================================
# 闭包：延伸了作用域的函数
# 内层函数对外层函数的变量（非全局变量）的引用，并返回 这样就形成了闭包。
# 闭包作用：
#         当程序执行时，遇到了函数执行，他会在内存中开辟一个空间，局部名称空间，
#         如果这个函数内部形成了闭包，
#         那么他就不会随着函数的结束而消失。
# flag = True
flag = False
if flag:
    # 闭包1
    def wraaper():
        name = "alex"

        def inner():
            print(name)

        print(inner.__closure__)
        inner()
        return inner

    wraaper()
    # 不是闭包 name为全局变量
    name = "alex"

    def wraaper():
        def inner():
            print(name)

        print(inner.__closure__)  # None 返回none代表不是闭包
        inner()
        return inner

    wraaper()

    name = "alex"

    def wraaper(n):
        # n = 'alex' # 相当于外界传入name，函数内部创建一个n的变量并赋值alex
        def inner():
            print(n)

        print(inner.__closure__)  # 返回的cell at 0x000002AD93BF76D8:
        inner()
        return inner

    wraaper(name)

    # nonlocal允许内嵌的函数来修改闭包变量
    def outer():
        x = 1

        def inner():
            nonlocal x
            x = x + 100
            return x

        return inner

    f = outer()
    f()
    # 闭包例子 爬虫
    from urllib.request import urlopen

    def index():
        url = "http://m.gaosan.com/xiaohua/"

        def get():
            return urlopen(url).read()

        return get

    xiaohua = index()  # get
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    print(content.decode("utf-8"))

