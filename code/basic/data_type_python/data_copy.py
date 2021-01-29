#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : data_copy.py
@author     : zgf
@brief      : 数据- 深浅拷贝
@attention  : life is short,I need python
"""


# =========================================  数据的复制 - 浅拷贝 =========================================
# 浅拷贝之后
# 针对不可变元素（数字、字符串、元组）的操作，都各自生效了
# 针对不可变元素（列表、集合）的操作，发生了一些混淆
# 对于浅拷贝来说，第一层在内存中是独立的，从第二层开始以及更深的层数，都是使用的一个内存地址，一变都变
flag = True
# flag = False
if flag:
    import copy

    # 列表浅拷贝方式1 copy()
    languages = ["Python", "C", "R", "Java"]
    languages_2 = languages.copy()
    languages.pop()
    print("languages:{},id:{}".format(languages, id(languages)))
    print("languages_2:{},id:{}".format(languages_2, id(languages_2)))

    # 元组 copy()
    a = (11, 22, 33)
    b = copy.copy(a)
    print(id(a))
    print(id(b))

    # 列表浅拷贝方式2：列表[:]
    languages = ["Python", "C", "R", "Java"]
    languages_3 = languages[:]
    languages.pop()
    print("languages:{},id:{}".format(languages, id(languages)))
    print("languages_3:{},id:{}".format(languages_3, id(languages_3)))

    # 对于浅拷贝来说，第一层在内存中是独立的，从第二层开始以及更深的层数，都是使用的一个内存地址，一变都变
    l1 = [
        1,
        2,
        3,
        [
            22,
        ],
    ]
    l2 = l1.copy()
    print("l1:{},id{}".format(l1, id(l1)))
    print("l2:{},id{}".format(l2, id(l2)))
    l1[-1].append("taibai")
    print("l1[-1]:{},id{}".format(l1[-1], id(l1[-1])))
    print("l2[-1]:{},id{}".format(l2[-1], id(l2[-1])))

    # 如果一份数据（列表）第二层时，你想与原数据进行公用，浅copy。
    #  面试题
    # 切片属于浅copy
    l1 = [1, 2, 3, [22, 33]]
    l2 = l1[:]
    # l1.append(666)
    l1[-1].append(666)
    print(l2)


# =========================================  数据的复制 - 深拷贝 =========================================
# deepcopy()
# 完全独立的copy一份数据，与原数据没有关系，深copy
# flag = True
flag = False
if flag:

    # 深拷贝将所有层级的相关元素全部复制，完全分开，泾渭分明，避免了上述问题
    import copy

    l1 = [
        1,
        2,
        3,
        [
            22,
            33,
        ],
    ]
    l2 = copy.deepcopy(l1)
    print(l1, l2, id(l1), id(l2))
    l1.append(666)
    l1[-2].append("太白")
    print(l1, type(l1))
    print(l2)
