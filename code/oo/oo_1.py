#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : oo_1.py
@author     : zgf
@brief      : python面向对象
@attention  : life is short,I need python
"""


# =========================================  面向对象 - 初识 =========================================
# 第一个面向对象
# Why：面向对象更符合人类对客观世界的抽象和理解
#
# 一切皆对象
# 一只小狗，一把椅子，一张信用卡，一条巧克力。。。
# 一切对象，都有自己内在的属性
# 狗狗的品种、椅子的质地、信用卡的额度、巧克力的口味。。。
# 一切行为，皆是对象的行为
# 狗狗蹲下、椅子移动位置、刷信用卡、巧克力融化了。。。
# How：类是对象的载体
#
# 不同年龄、肤色、品质的猫，每一只都是一个对象
#
# 他们有一个共同的特征：都是猫
#
# 我们可以把一类对象的公共特征抽象出来，创建通用的类
# flag = True
flag = False
if flag:

    class Cat:
        def eat(self):
            print("小猫爱吃鱼")

        def drink(self):
            print("小猫要喝水")

    # 创建猫对象
    tom = Cat()

    tom.eat()
    tom.drink()

    print(tom)

    addr = id(tom)
    print("%x" % addr)


# =========================================  面向对象 - 初识 =========================================
# 新建两个猫对象
# flag = True
flag = False
if flag:

    class Cat:
        def eat(self):
            print("小猫爱吃鱼")

        def drink(self):
            print("小猫要喝水")

    # 创建猫对象
    tom = Cat()

    tom.eat()
    tom.drink()

    print(tom)

    # 再创建一个猫对象
    lazy_cat = Cat()

    lazy_cat.eat()
    lazy_cat.drink()

    print(lazy_cat)

    lazy_cat2 = lazy_cat

    print(lazy_cat2)


# =========================================  面向对象 - 初识 =========================================
# 设置对象属性
# flag = True
flag = False
if flag:

    class Cat:
        def eat(self):
            # 哪一个对象调用的方法，self就是哪一个对象的引用
            print("%s 爱吃鱼" % self.name)

        def drink(self):
            print("%s 要喝水" % self.name)

    # 创建猫对象
    tom = Cat()

    # 可以使用　.属性名　利用赋值语句就可以了
    tom.name = "Tom"

    tom.eat()
    tom.drink()

    print(tom)

    # 再创建一个猫对象
    lazy_cat = Cat()

    lazy_cat.name = "大懒猫"

    lazy_cat.eat()
    lazy_cat.drink()

    print(lazy_cat)

    # 在外界设置属性的问题
    class Cat:
        def eat(self):
            # 哪一个对象调用的方法，self就是哪一个对象的引用
            print("%s 爱吃鱼" % self.name)

        def drink(self):
            print("%s 要喝水" % self.name)

    # 创建猫对象
    tom = Cat()

    # 可以使用　.属性名　利用赋值语句就可以了
    # tom.name = "Tom"

    tom.eat()
    tom.drink()
    tom.name = "Tom"


# =========================================  面向对象 - __init()__ =========================================
# 设置对象属性
# def __init__(self,要传递的参数)  初始化类的属性
# flag = True
flag = False
if flag:

    class Cat:
        def __init__(self):
            print("这是一个初始化方法")

            # self.属性名 = 属性的初始值
            self.name = "Tom"

        def eat(self):
            print("%s 爱吃鱼" % self.name)

    # 使用类名()创建对象的时候，会自动调用初始化方法 __init__
    tom = Cat()

    print(tom.name)

    #  利用参数设置属性初始值
    class Cat:
        def __init__(self, new_name):
            print("这是一个初始化方法")

            # self.属性名 = 属性的初始值
            # self.name = "Tom"
            self.name = new_name

        def eat(self):
            print("%s 爱吃鱼" % self.name)

    # 使用类名()创建对象的时候，会自动调用初始化方法 __init__
    tom = Cat("Tom")

    print(tom.name)

    lazy_cat = Cat("大懒猫")
    lazy_cat.eat()


# =========================================  面向对象 - __del__ =========================================
# 设置对象属性
# flag = True
flag = False
if flag:

    class Cat:
        def __init__(self, new_name):
            self.name = new_name

            print("%s 来了" % self.name)

        def __del__(self):
            print("%s 我去了" % self.name)

    # tom 是一个全局变量
    tom = Cat("Tom")
    print(tom.name)

    # del 关键字可以删除一个对象
    del tom

    print("-" * 50)


# =========================================  面向对象 - __str__ =========================================
#
# flag = True
flag = False
if flag:

    class Cat:
        def __init__(self, new_name):
            self.name = new_name

            print("%s 来了" % self.name)

        def __del__(self):
            print("%s 我去了" % self.name)

        def __str__(self):
            # 必须返回一个字符串
            return "我是小猫[%s]" % self.name

    # tom 是一个全局变量
    tom = Cat("Tom")
    print(tom)
