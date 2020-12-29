#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : test_module_1.py
@author     : zgf
@brief      : 模块
@attention  : life is short,I need python
"""


# 全局变量
title = "模块1"

# 函数
def say_hello():
    print("我是 %s" % title)


# 类
class Dog(object):
    pass


if __name__ == "__main__":
    print(__name__)

    # 文件被导入时，能够直接执行的代码不需要被执行！
    print("小明开发的模块1")
    say_hello()
