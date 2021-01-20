#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : variable_python.py
@author     : zgf
@brief      : python变量
@attention  : life is short,I need python
"""


# =========================================  常量 =========================================
# 常量即不变的量 如π、e
# 全部用大写字母表示
# flag = True
flag = False
if flag:
    PI = 3.1415926
    print(PI)


# =========================================  变量赋值 =========================================
# 在 Python 中定义变量时不需要指定类型，Python 可以根据 = 等号右侧的值，自动推导出变量中存储数据的类型
# 赋值方式1：通过等号自右向左进行赋值
# 赋值方式2：增量赋值
# 赋值方式3：打包赋值

# 定义变量会有：id(唯一标识号）,type(变量类型）,value(变量值）
# 1.id相同，意味着type和value必定相同 is比较id
# 2.value相同type肯定相同，但id可能不同 ==
# flag = True
flag = False
if flag:
    x = 1 + 2  # 赋值方式1：通过等号自右向左进行赋值
    print(x)
    y = 10
    y += 10  # 赋值方式2：增量赋值
    print(y)
    u, v = 1, 2  # 赋值方式3：打包赋值
    print(u, v)
    v, u = u, v
    print(u, v)

    x = "sadasfgdafsdaaaaasadasfgdafsdaaaaasadasfgdafsdaaaaasadasfgdafsdaaaaa"
    y = "sadasfgdafsdaaaaasadasfgdafsdaaaaasadasfgdafsdaaaaasadasfgdafsdaaaaa"
    print(x, id(x), type(x))
    print(y, id(y), type(y))
    print(x == y)
    print(x is y)


# =========================================  变量的类型 =========================================
# Python属于强类型的动态脚本语言：不允许不同类型相加动态：
# 定义变量不用数据类型声明，且确定一个变量的类型是第一次给他赋值的时候
# 在 Python 中，定义变量时是不需要指定变量的类型的
# 在运行的时候，Python 解释器，会根据赋值语句等号右侧的数据，自动推导出变量中保存数据的准确类型
# flag = True
flag = False
if flag:
    """
    姓名：小明
    年龄：18 岁
    性别：是男生
    身高：1.75 米
    体重：75.0 公斤
    """
    # str 表示是一个字符串类型
    name = "小明"
    # int 表示是一个整数类型
    age = 18
    # bool 表示是一个布尔类型，真 True 或者假 False
    gender = False  # 不是
    # float 表示是一个小数类型，浮点数
    height = 1.75
    weight = 75
    print(name)


# =========================================  变量的输入 =========================================
# 使用解释器执行，如果要输出变量的内容，必须要要使用 print 函数
# 如果要获取用户在 键盘 上的输入信息，需要使用到 input 函数
# 用户输入的 任何内容 Python 都认为是一个 字符串
# 变量中存储的值，就是可以 变的
# flag = True
flag = False
if flag:
    # 1.输入苹果单价，并将苹果单价转换成小数
    price = float(input("请输入苹果价格："))
    # 2.要求苹果重量，并将苹果重量转换成小数
    weight = float(input("请输入苹果重量："))
    # 3>计算付款金额
    money = price * weight
    print(money)


# =========================================  变量的输出 =========================================
#
# flag = True
flag = False
if flag:
    pass


# =========================================  变量的引用 =========================================
#
# flag = True
flag = False
if flag:
    pass


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


# =========================================  全局变量 - 不允许直接修改全局变量的引用=========================================
# 不允许直接修改全局变量的引用 —— 使用赋值语句修改全局变量的值
# flag = True
flag = False
if flag:
    num = 10

    def demo1():
        print("demo1" + "-" * 50)
        # 注意：只是在函数内部定义了一个局部变量而已，不会修改到全局变量，只是变量名相同 —— 在函数内部不能直接修改全局变量的值
        num = 100
        print(num)

    def demo2():
        print("demo2" + "-" * 50)
        print(num)

    demo1()
    demo2()
    print("over")


# =========================================  全局变量 - 修改全局变量的引用=========================================
# 如果在函数中需要修改全局变量，需要使用 global 进行声明
# flag = True
flag = False
if flag:
    num = 10

    def demo1():
        print("demo1" + "-" * 50)
        # global关键字，告诉Python解释器num是一个全局变量
        global num
        # 只是定义了一个局部变量，不会修改到全局变量，只是变量名相同而已
        num = 100
        print(num)

    def demo2():
        print("demo2" + "-" * 50)
        print(num)

    demo1()
    demo2()
    print("over")


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
