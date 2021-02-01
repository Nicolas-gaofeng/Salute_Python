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
        # 注意：只是在函数内部定义了一个局部变量而已，不会修改到全局变量，只是变量名相同
        # 在函数内部不能直接修改全局变量的值
        # 如果使用赋值语句，会在函数内部，定义一个局部变量
        num = 100
        print(num)

    def demo2():
        print(num)

    def demo3():
        # 希望修改全局变量的值 - 使用 global 声明一下变量即可
        # global 关键字会告诉解释器后面的变量是一个全局变量
        # 再使用赋值语句时，就不会创建局部变量
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


# =========================================  函数体与变量作用域 =========================================
# 函数体就是一段只在函数被调用时，才会执行的代码，代码构成与其他代码并无不同
# python中，名称空间分三种：
# 全局名称空间
# 局部名称空间（临时）
# 内置名称空间
# 作用域：
#     全局作用域 全局名称空间 内置名称空间
#     局部作用域 局部名称空间（临时）
# 取值顺序： 就近原则
# 局部名称空间  ---->  全局名称空间 ----->内置名称空间  单向从小到大范围
# flag = True
flag = False
if flag:

    def multipy(x, y):
        z = x * y
        return z

    multipy(2, 9)
    # print(z)  # 函数执行完毕，局部变量z已经被释放掉了

    """ globals() locals()"""
    # globals() # 返回全局变量的一个字典。
    # locals()  返回 当前位置 的局部变量的字典。

    def func1():
        a = 2
        b = 3
        print(globals())
        print(locals())

        def inner():
            c = 5
            d = 6
            print(globals())
            print(locals())

        inner()

    # print(globals())
    # print(locals())
    func1()
