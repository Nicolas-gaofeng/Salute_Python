#!/usz/bin/env python
# -*- coding:utf-8 -*-


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


# =========================================  面向对象 类属性 =========================================
#
# flag = True
flag = False
if flag:

    class Tool(object):
        # 使用赋值语句定义类属性，记录所有工具对象的数量
        count = 0

        def __init__(self, name):
            self.name = name

            # 让类属性的值+1
            Tool.count += 1

    # 1. 创建工具对象
    tool1 = Tool("斧头")
    tool2 = Tool("榔头")
    tool3 = Tool("水桶")

    # 2. 输出工具对象的总数
    print(Tool.count)


# =========================================  面向对象 属性获取机制 =========================================
#
# flag = True
flag = False
if flag:

    class Tool(object):
        # 使用赋值语句定义类属性，记录所有工具对象的数量
        count = 0

        def __init__(self, name):
            self.name = name

            # 让类属性的值+1
            Tool.count += 1

    # 1. 创建工具对象
    tool1 = Tool("斧头")
    tool2 = Tool("榔头")
    tool3 = Tool("水桶")

    # 2. 输出工具对象的总数
    print(Tool.count)
    print("工具对象总数 %d" % tool3.count)


# =========================================  面向对象 属性获取机制 =========================================
# 使用对象名访问类属性的问题
# flag = True
flag = False
if flag:

    class Tool(object):
        # 使用赋值语句定义类属性，记录所有工具对象的数量
        count = 0

        def __init__(self, name):
            self.name = name

            # 让类属性的值+1
            Tool.count += 1

    # 1. 创建工具对象
    tool1 = Tool("斧头")
    tool2 = Tool("榔头")
    tool3 = Tool("水桶")

    # 2. 输出工具对象的总数
    tool3.count = 99
    print("工具对象总数 %d" % tool3.count)
    print("===> %d" % Tool.count)
