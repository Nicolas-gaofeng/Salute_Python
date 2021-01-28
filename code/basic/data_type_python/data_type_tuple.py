#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : data_type_tuple.py
@author     : zgf
@brief      : 数据类型- 元组
@attention  : life is short,I need python
"""


# =========================================  元组（tuple）- 取值 =========================================
# 元组是不可变类型
# 元组里的数据不能修改
# 元组是一个可以使用多种类型元素，一旦定义，内部元素不支持增、删和修改操作的序列类型
# 通俗的讲，可以将元组视作“不可变的列表”
# 元组的操作不支持元素增加、元素删除、元素修改操作 其他操作与列表的操作完全一致
# flag = True
flag = False
if flag:
    name = ("zhangsan", "lisi", "wangwu")
    print(name, type(name))
    # 1. 取值和取索引
    print(name[0])
    # 已经知道数据的内容，希望知道该数据在元组中的索引
    print(name.index("zhangsan"))
    # 2. 统计计数
    print(name.count("zhangsan"))
    # 统计元组中包含元素的个数
    print(len(name))
    # 直接迭代
    graduates = ("李雷", "韩梅梅", "Jim")
    for graduate in graduates:
        print("Congratulations, " + graduate)


# =========================================  元组（tuple）-打包与解包 =========================================
#
# flag = True
flag = False
if flag:

    def f1(x):  # 返回x的平方和立方
        return x ** 2, x ** 3  # 实现打包返回

    print(f1(3))
    print(type(f1(3)))  # 元组类型
    a, b = f1(3)  # 实现解包赋值
    print(a)
    print(b)
    # example
    numbers = [201901, 201902, 201903]
    name = ["小明", "小红", "小强"]
    print(list(zip(numbers, name)))
    for number, name in zip(numbers, name):  # 每次取到一个元组，立刻进行解包赋值
        print(number, name)
    # example
    info_tuple = ("小明", 21, 1.85)
    # 格式化字符串后面的 `()` 本质上就是元组
    print("%s 年龄是 %d 身高是 %.2f" % info_tuple)
    info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
    print(info_str)
