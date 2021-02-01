#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : python_iterator_o.py
@author     : zgf
@brief      : 可迭代对象
@attention  : life is short,I need python
"""


# =========================================  可迭代对象 =========================================
# 可直接作用于for循环的对象统称为可迭代对象：Iterable
# 可迭代对象：str list dict,tuple,set,range()，可迭代对象满足可迭代协议。
# flag = True
flag = False
if flag:
    # 可迭代对象
    for i in "abc":
        print(i)

    # 'int' object is not iterable
    # for i in 123:
    #     print(i)

    s1 = "strs"
    print(dir(s1))  # dir()查看内部方法


# =========================================  可迭代对象 vs 迭代器 =========================================
# 可迭代对象不能取值，迭代器是可以取值的。
# flag = True
flag = False
if flag:

    # 可迭代对象 --->(转化成)迭代器
    lis = [1, 2, 3]  # 可迭代对象
    # ite1 = lis.__iter__()  # 迭代器  <list_iterator object at 0x0000027A183BFFD0>
    ite1 = iter(lis)  # 迭代器  <list_iterator object at 0x0000027A183BFFD0>
    print(ite1)

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


# =========================================  判断可迭代对象 =========================================
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


# ========================================= isinstance(变量,预判类型)  类型判别 =========================================
# isinstance(变量,预判类型) 承认继承
# 变量类型是预判类型的子类型，则为真，否则为假
# flag = True
flag = False
if flag:
    age = 20
    name = "zhangsan"
    print(isinstance(age, int))  # 承认继承
    print(isinstance(age, object))
    print(isinstance(name, object))  # object 是老祖宗
