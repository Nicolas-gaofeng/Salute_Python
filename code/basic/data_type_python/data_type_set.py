#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : data_type_set.py
@author     : zgf
@brief      : 数据类型- 集合
@attention  : life is short,I need python
"""


# =========================================  集合（set）- 创建 =========================================
# 集合是可变类型
# 不能重复 没有顺序
# 一系列互不相等元素的无序集合
# 元素必须是不可变类型：数字，字符串或元组，可视作字典的键
# 可以看做是没有值，或者值为None的字典
# 可用于去重
# flag = True
flag = False
if flag:
    NBA_player = {
        "zhangsan",
        "lisi",
        "wangwu",
    }
    print(NBA_player, type(NBA_player))
    NBA_players = {"zhangsan", "lisi", "wangwu", "zhangsan"}
    print(NBA_players, type(NBA_players))

    # 不可变数据类型
    set1 = {1, 2, 3}
    set3 = frozenset(set1)
    print(set3)


# =========================================  集合（set）- 运算 =========================================
# 交集 S & T 返回一个新集合，包括同时在集合S和T中的元素
# 并集 S | T 返回一个新集合，包括集合S和T中的所有元素
# 反交集 S ^ T 返回一个新集合，包括集合S和T中的非共同元素
# 差集 S - T 返回一个新集合，包括在集合S但不在集合T中的元素
# flag = True
flag = False
if flag:
    Chinese_A = {"刘德华", "张学友", "张曼玉", "钟楚红", "古天乐", "林青霞"}
    print(Chinese_A)
    Math_A = {"林青霞", "郭富城", "王祖贤", "刘德华", "张曼玉", "黎明"}
    print(Math_A)
    print(Chinese_A & Math_A)
    print(Chinese_A | Math_A)
    print(Chinese_A ^ Math_A)
    print(Chinese_A - Math_A)
    print(Chinese_A < Math_A)  # 子集
    print(Chinese_A > Math_A)  # 超集
    print(Chinese_A.issuperset(Math_A))  # 超集


# =========================================  集合（set）- 增加元素 =========================================
# S.add(x)
# flag = True
flag = False
if flag:
    stars = {"刘德华", "张学友", "张曼玉"}
    stars.add("王祖贤")
    print(stars)


# =========================================  集合（set）- 移除元素 =========================================
# S.remove(x)
# pop()
# clear()
# flag = True
flag = False
if flag:
    stars = {"刘德华", "张学友", "张曼玉"}
    stars.remove("刘德华")
    print(stars)
    # pop() 随机删除
    stars.pop()
    print(stars.pop(), stars)
    # clear() 清空集合
    stars.clear()
    print(stars)


# =========================================  集合（set）- 集合的长度 =========================================
# len()
# flag = True
flag = False
if flag:
    stars = {"刘德华", "张学友", "张曼玉"}
    print(len(stars))


# =========================================  集合（set）-遍历 =========================================
# 集合的遍历——借助for循环
# flag = True
flag = False
if flag:
    stars = {"刘德华", "张学友", "张曼玉"}
    for star in stars:
        print(star)


# =========================================  集合（set）- 去重 =========================================
#
# flag = True
flag = False
if flag:
    """list去重"""
    l1 = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8]
    set1 = set(l1)
    l2 = list(set1)
    print(l2)
