#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : notes_python.py
@author     : zgf
@brief      : python注释
@attention  : life is short,I need python
"""

# ========================================= 单行注释 =========================================
# 以 # 开头，# 右边的所有东西都被当做说明文字，而不是真正要执行的程序，只起到辅助说明作用
# 为了保证代码的可读性，# 后面建议先添加一个空格，然后再编写相应的说明文字
# flag = True
flag = False
if flag:
    pass  # 在程序开发时，同样可以使用 # 在代码的后面（旁边）增加说明性的文字.但是，需要注意的是，为了保证代码的可读性，注释和代码之间至少要有两个空格


# ========================================= 多行注释 =========================================
# 如果希望编写的 注释信息很多，一行无法显示，就可以使用多行注释
# 要在 Python 程序中使用多行注释，可以用 一对 连续的 三个 引号(单引号和双引号都可以)
# flag = True
flag = False
if flag:
    """
    这是一个多行注释

    在多行注释之间，可以写很多很多的内容……
    """
    print("hello python")
