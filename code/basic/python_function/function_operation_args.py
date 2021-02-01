#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : function_args.py
@author     : zgf
@brief      : 函数参数
@attention  : life is short,I need python
"""


# ========================================= 函数的参数 =========================================
# 形参（形式参数）：函数定义时的参数，实际上就是变量名
# 实参（实际参数）：函数调用时的参数，实际上就是变量的值
# 位置参数：严格按照位置顺序，用实参对形参进行赋值(关联）实参与形参个数必须一一对应，一个不能多，一个不能少；用在参数比较少的时候
# 关键字参数：打破位置限制，直呼其名的进行值的传递（形参=实参）必须遵守实参与形参数量上一一对应；多用在参数比较多的场合
# 位置参数可以与关键字参数混合使用
# 但是，位置参数必须放在关键字参数前面
# 不能为同一个形参重复传值
# 默认参数：在定义阶段就给形参赋值——该形参的常用值 在定义阶段就给形参赋值——该形参的常用值 默认参数必须放在非默认参数后面 调用函数时，可以不对该形参传值
# flag = True
flag = False
if flag:

    def function(x, y, z):
        print(x, y, z)

    function(y=1, z=2, x=3)  # x = 1; y = 2; z = 3

    function(1, z=2, y=3)
    function(1, 2, z=3)

    def sum_2_num(num1, num2):
        """对两个数字的求和"""
        # num1 = 10
        # num2 = 20
        result = num1 + num2
        print("%d + %d = %d" % (num1, num2, result))

    sum_2_num(1, 2)

    # 默认参数
    def register(name, age, sex="male"):
        print(name, age, sex)

    register("林志玲", 38, "female")
    register("大杰仔", 18)


# ========================================= 函数的参数 - 缺省参数 =========================================
#
# flag = True
flag = False
if flag:

    # 函数的缺省参数
    gl_list = [6, 3, 9]

    # 默认按照升序排序 - 可能会多！
    # gl_list.sort()

    # 如果需要降序排序，需要执行reverse参数
    gl_list.sort(reverse=True)
    print(gl_list)

    # 函数的缺省参数定义
    def print_info(name, gender=True):
        """
        :param name: 班上同学的姓名
        :param gender: True 男生 False 女生
        """

        gender_text = "男生"

        if not gender:
            gender_text = "女生"

        print("%s 是 %s" % (name, gender_text))

    # 假设班上的同学，男生居多！
    # 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
    print_info("小明")
    print_info("老王")
    print_info("小美", False)


# ========================================= 函数的参数-不可变和可变参数 =========================================
#
# flag = True
flag = False
if flag:

    def demo(num, num_list):
        print("函数内部的代码")

        # 在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量
        num = 100
        num_list = [1, 2, 3]

        print(num)
        print(num_list)
        print("函数执行完成")

    gl_num = 99
    gl_list = [4, 5, 6]
    demo(gl_num, gl_list)
    print(gl_num)
    print(gl_list)


# ========================================= 函数 -  函数名的应用 =========================================
#
# if flag:
# flag = True
flag = False
if flag:
    # 1 ,函数名就是函数的内存地址。
    def func():
        print("111")

    print(func())

    # 2, 函数名可以作为变量。
    a = 2
    b = a
    c = b
    print(c)

    def func1():
        print(666)

    f1 = func1
    f2 = f1
    f2()

    # 3,函数名可以作为函数的参数。 --高阶函数

    def func1():
        print(666)

    def func2(x):
        print(x)  # <function func1 at 0x0000026C3D983BF8>
        # x()

    a = "太白"
    func2(a)
    print(func1)  # <function func1 at 0x0000026C3D983BF8>

    def func():
        print(666)

    def func1():
        func()

    def func2(x):
        x()  # func1()

    func2(func1)

    # 函数名可以当做函数的返回值。

    def wraaper():
        def inner():
            print("inner   ")

        return inner

    ret = wraaper()  # inner
    ret()  # inner()

    def func2():
        print("in func2")

    def func3(x):  # x = func2
        print("in func3")
        return x  # func2

    f1 = func3(func2)  # func2
    f1()

    # 函数名可以作为容器类类型的元素。

    a = 6
    b = 4
    c = 5
    l1 = [a, b, c]
    print(l1)

    def func1():
        print("in func1")

    def func2():
        print("in func2")

    def func3():
        print("in func3")

    def func4():
        print("in func4")

    l1 = [func1, func2, func3, func4]
    for i in l1:
        i()

    # 向上面的函数名这种，第一类对象。


