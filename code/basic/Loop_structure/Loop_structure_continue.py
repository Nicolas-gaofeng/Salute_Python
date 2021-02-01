#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : Loop_structure_continue.py
@author     : zgf
@brief      : 循环结构 - continue
@attention  : life is short,I need python
"""


# ========================================= continue =========================================
# 结束本次循环
# continue用于退出本次循环，继续下一次循环
# flag = True
flag = False
if flag:
    i = 0
    while i < 10:
        # continue 某一条件满足时，不执行后续重复的代码
        # i == 3
        if i == 3:
            # 注意：在循环中，如果使用 continue 这个关键字
            # 在使用关键字之前，需要确认循环的计数是否修改，
            # 否则可能会导致死循环
            i += 1
            continue
        print(i)
        i += 1
    # 程序练习
    product_scores = [89, 90, 99, 70, 67, 78, 85, 92, 77, 82]  # 1组10个产品的性能评分
    # 如果低于75分,输出警示
    print(len(product_scores))
    for i in range(len(product_scores)):
        if product_scores[i] >= 75:
            continue
        print("第{0}个产品，分数为{1}，不合格".format(i, product_scores[i]))
