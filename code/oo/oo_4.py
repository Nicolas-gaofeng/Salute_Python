#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : oo_4.py
@author     : zgf
@brief      : python面向对象 - 多态
@attention  : life is short,I need python
"""

# =========================================  面向对象 多态 - 初识 =========================================
# 重写父类的方法
# flag = True
flag = False
if flag:

    class Dog(object):
        def __init__(self, name):
            self.name = name

        def game(self):
            print("%s 蹦蹦跳跳的玩耍..." % self.name)

    class XiaoTianDog(Dog):
        def game(self):
            print("%s 飞到天上去玩耍..." % self.name)

    class Person(object):
        def __init__(self, name):
            self.name = name

        def game_with_dog(self, dog):
            print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))

            # 让狗玩耍
            dog.game()

    # 1. 创建一个狗对象
    # wangcai = Dog("旺财")
    wangcai = XiaoTianDog("飞天旺财")

    # 2. 创建一个小明对象
    xiaoming = Person("小明")

    # 3. 让小明调用和狗玩的方法
    xiaoming.game_with_dog(wangcai)

