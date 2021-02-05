#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : function_operation_2.py
@author     : zgf
@brief      : 匿名函数
@attention  : life is short,I need python
"""


# ========================================= 匿名函数 =========================================
# 基本形式 lambda 变量: 函数体
# 匿名函数  lambda表达式，
# 匿名函数 不单独使用，多与内置函数结合
# 普通函数 有且只有返回值的函数才可以用匿名函数进行简化，一行函数。
# 常用用法 ：在参数列表中最适合使用匿名函数，尤其是与key = 搭配
# flag = True
flag = False
if flag:
    ls = [(93, 88), (79, 100), (86, 71), (85, 85), (76, 94)]
    ls.sort()
    print(ls)  # [(76, 94), (79, 100), (85, 85), (86, 71), (93, 88)]
    ls.sort(key=lambda x: x[1])
    print(ls)  # [(86, 71), (85, 85), (93, 88), (76, 94), (79, 100)]
    ls = [(93, 88), (79, 100), (86, 71), (85, 85), (76, 94)]
    temp = sorted(ls, key=lambda x: x[0] + x[1], reverse=True)
    print(temp)  # [(93, 88), (79, 100), (85, 85), (76, 94), (86, 71)]
    # max() min()
    ls = [(93, 88), (79, 100), (86, 71), (85, 85), (76, 94)]
    n = max(ls, key=lambda x: x[1])
    print(n)  # (79, 100)
    n = min(ls, key=lambda x: x[1])
    print(n)  # (86, 71)

    func2 = lambda x: x ** 2
    print(func2(6))

    func2 = lambda x, y: x + y
    print(func2(1, 2))

    l2 = [(1, 1000), (2, 18), (4, 250), (3, 500)]
    print(sorted(l2, key=lambda x: x[1]))

    dic = {"k1": 10, "k2": 100, "k3": 30}
    # 1,利用内置函数匿名函数将dic按照值进行排序。
    print(sorted(dic, key=lambda x: dic[x]))
    print(sorted(dic.items(), key=lambda x: x[1]))
    # [1,5,7,4,8]
    # 利用内置函数匿名函数 计算列表的每个数的2倍。
    print(list(map(lambda x: x * 2, [1, 5, 7, 4, 8])))
    # [5,8,11,9,15]
    # 利用内置函数匿名函数，将值大于10的留下来。
    print(list(filter(lambda x: x > 10, [5, 8, 11, 9, 15])))

    # func = lambda x:x if x > 2 else x * 2
