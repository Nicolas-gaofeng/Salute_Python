#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : function_operation_mul.py
@author     : zgf
@brief      : 函数-多值参数
@attention  : life is short,I need python
"""


# ========================================= 函数的参数-多值参数 =========================================
#
# flag = True
flag = False
if flag:

    # 函数的多值参数
    def demo(num, *nums, **person):

        print(num)
        print(nums)
        print(person)

    demo(1, 2, 3, 4, 5, name="小明", age=18)

    # 多值参数求和
    # 在函数的定义时，在 *位置参数，聚合。
    # *args 将所有的实参的位置参数聚合到一个元组，并将这个元组赋值给args
    def sum_numbers(*args):
        # def sum_numbers(args):

        num = 0

        print(args)
        # 循环遍历
        for n in args:
            num += n

        return num

    result = sum_numbers(1, 2, 3, 4, 5)
    print(result)


# ========================================= 函数的参数-多值参数-元组字典的拆包 =========================================
#
# flag = True
flag = False
if flag:

    def demo(*args, **kwargs):

        print(args)
        print(kwargs)

    # 元组变量/字典变量
    gl_nums = (1, 2, 3)
    gl_dict = {"name": "小明", "age": 18}

    # demo(gl_nums, gl_dict)

    # 拆包语法，简化元组变量/字典变量的传递
    demo(*gl_nums, **gl_dict)

    demo(1, 2, 3, name="小明", age=18)

    # 函数内部通过方法修改可变参数
    def demo(num_list):
        print("函数内部的代码")

        # 使用方法修改列表的内容
        num_list.append(9)

        print(num_list)

        print("函数执行完成")

    gl_list = [1, 2, 3]
    demo(gl_list)
    print(gl_list)

    def func1(*args, **kwargs):  # 函数的定义：*聚合。
        print(*args)  # (*(1,2,3,4))函数的执行： * 打散  print(1,2,3,4)
        # print(**kwargs)  # print(name='alex',age=1000) print会报错
        print(kwargs)

    func1(1, 2, 3, 4, name="alex", age=1000)
