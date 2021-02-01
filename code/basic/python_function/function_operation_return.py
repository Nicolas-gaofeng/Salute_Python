#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : function_operation_return.py
@author     : zgf
@brief      : 函数返回值
@attention  : life is short,I need python
"""


# ========================================= 函数的返回值 - 单个返回值 =========================================
# 函数中如果遇到retrun,则直接结束函数。
# flag = True
flag = False
if flag:

    def sum_2_num(num1, num2):
        """对两个数字的求和"""
        result = num1 + num2
        # 可以使用返回值，告诉调用函数一方计算的结果
        return result
        # 注意：return 就表示返回，下方的代码不会被执行到！
        # num = 1000

    # 可以使用变量，来接收函数执行的返回结果
    sum_result = sum_2_num(10, 20)
    print("计算结果：%d" % sum_result)


# ========================================= 函数的返回值 - 多个返回值 =========================================
# 函数中如果遇到retrun,则直接结束函数。
# flag = True
flag = False
if flag:

    def foo(x):
        return 1, x, x ** 2, x ** 3  # 逗号分开，打包返回

    print(foo(3))

    def measure():
        """测量温度和湿度"""

        print("测量开始...")
        temp = 39
        wetness = 50
        print("测量结束...")

        # 元组-可以包含多个数据，因此可以使用元组让函数一次返回多个值
        # 如果函数返回的类型是元组，小括号可以省略
        # return (temp, wetness)
        return temp, wetness

    # 元组
    result = measure()
    print(result)

    # 需要单独的处理温度或者湿度 - 不方便
    print(result[0])
    print(result[1])

    # 如果函数返回的类型是元组，同时希望单独的处理元组中的元素
    # 可以使用多个变量，一次接收函数的返回结果
    # 注意：使用多个变量接收结果时，变量的个数应该和元组中元素的个数保持一致
    gl_temp, gl_wetness = measure()

    print(gl_temp)
    print(gl_wetness)

    """解包赋值"""
    a, b, c, d = foo(3)  # 解包赋值
    print(a)
    print(b)
    print(c)
    print(d)

    # 可以有多个return 语句，一旦其中一个执行，代表了函数运行的结束
    def is_holiday(day):
        if day in ["Sunday", "Saturday"]:
            return "Is holiday"
        else:
            return "Not holiday"
        print("啦啦啦德玛西亚，啦啦啦啦")  # 你丫根本没机会运行。。。

    print(is_holiday("Sunday"))
    print(is_holiday("Monday"))

    # 没有return语句，返回值为None
    def foo():
        print("我是孙悟空")

    res = foo()
    print(res)
