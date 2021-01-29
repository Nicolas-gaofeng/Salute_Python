#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : python_iterator.py
@author     : zgf
@brief      : 迭代器
@attention  : life is short,I need python
"""


# =========================================  迭代器 =========================================
# 对象内部含有__iter__方法就是可迭代对象.
#  列表、元组、字符串、字典、集合不是迭代器
# 可直接作用于for循环的对象统称为可迭代对象：Iterable
# 可迭代对象满足可迭代协议。
# for item in Iterable 等价于：
# 先通过iter()函数获取可迭代对象Iterable的迭代器
# 然后对获取到的迭代器不断调用next()方法来获取下一个值并将其赋值给item
# 当遇到StopIteration的异常后循环结束
# flag = True
flag = False
if flag:
    # 可迭代对象
    for i in "abc":
        print(i)
    # for i in 123:
    #     print(i)  # 'int' object is not iterable

    # 可迭代对象：str list dict,tuple,set,range()
    s1 = "strs"
    print(dir(s1))

    # 可迭代对象vs迭代器
    # 可迭代对象不能取值，迭代器是可以取值的。
    # 可迭代对象 --->(转化成)迭代器
    lis = [1, 2, 3]  # 可迭代对象
    # ite1 = lis.__iter__()  # 迭代器  <list_iterator object at 0x0000027A183BFFD0>
    ite1 = iter(lis)  # 迭代器  <list_iterator object at 0x0000027A183BFFD0>
    print(ite1)

    # 迭代器如何取值？  next一次，取一个值
    # print(ite1.__next__())
    # print(ite1.__next__())
    # print(ite1.__next__())
    # print(ite1.__next__())

    # 1, 可迭代对象不能取值，迭代器是可以取值的。
    # 2, 迭代器非常节省内存。
    # 3, 迭代器每次只会取一个值。
    # 4,，迭代器单向的，一条路走到头。

    s1 = "kfdsjl"
    # for i in s1:
    #     print(i)

    # 1,将可迭代对象转化成迭代器。
    # 2，调用__next__方法取值。
    # 3，利用异常处理停止报错。
    iter1 = s1.__iter__()

    while 1:
        try:
            print(iter1.__next__())
        except StopIteration:
            break


# =========================================  迭代器 =========================================
# 判断一个对象是否是可迭代对象
# flag = True
flag = False
if flag:
    # 第一个方法
    dic = {"name": "alex"}
    print("__iter__" in dir(dic))
    # 第二种方法
    # 可以使用isinstance()判断一个对象是否是Iterable对象
    from collections import Iterable
    from collections import Iterator

    print(isinstance("alex", Iterable))  # True
    print(isinstance("alex", Iterator))  # False

    print(isinstance("alex", str))

    # 对象内部含有__iter__方法且含有__next__方法就是迭代器.

    # f = open('register', encoding='utf-8')
    # print('__iter__' in dir(f))
    # print('__next__' in dir(f))
    # print('__iter__' in dir(dict))
    # print('__next__' in dir(dict))


# =========================================  迭代器 =========================================
#
# flag = True
flag = False
if flag:
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
