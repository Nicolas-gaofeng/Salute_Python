#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : python_iterator.py
@author     : zgf
@brief      : 迭代器
@attention  : life is short,I need python
"""


# =========================================  判断是否是迭代器 =========================================
# 对象内部含有__iter__方法且含有__next__方法就是迭代器.
#  列表、元组、字符串、字典、集合不是迭代器
# for item in Iterable 等价于：先通过iter()函数获取可迭代对象Iterable的迭代器,然后对获取到的迭代器不断调用next()方法来获取下一个值并将其赋值给item
# 当遇到StopIteration的异常后循环结束
# flag = True
flag = False
if flag:
    f = open("register", encoding="utf-8")
    print("__iter__" in dir(f))
    print("__next__" in dir(f))
    print("__iter__" in dir(dict))
    print("__next__" in dir(dict))

    from collections import Iterator

    # zip enumerate 等itertools里的函数是迭代器
    x = [1, 2]
    y = ["a", "b"]
    zip(x, y)
    for i in zip(x, y):
        print(i)

    print(isinstance(zip(x, y), Iterator))
    numbers = [1, 2, 3, 4, 5]

    enumerate(numbers)
    for i in enumerate(numbers):
        print(i)
    print(isinstance(enumerate(numbers), Iterator))
    # 文件是迭代器
    with open("测试文件.txt", "r", encoding="utf-8") as f:
        print(isinstance(f, Iterator))

    #  range()不是迭代器
    numbers = range(10)
    isinstance(numbers, Iterator)
