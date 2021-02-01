#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : Loop_structure_break.py
@author     : zgf
@brief      : 循环结构 - break
@attention  : life is short,I need python
"""


# ========================================= break =========================================
# break用于退出本层循环
# flag = True
flag = False
if flag:
    i = 0
    while i < 10:
        # break 某一条件满足时，退出循环，不再执行后续重复的代码
        # i == 3
        if i == 3:
            break
        print(i)
        i += 1
    print("over")
