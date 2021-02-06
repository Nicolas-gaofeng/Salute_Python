#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : oo_5.py
@author     : zgf
@brief      : python面向对象 - 类属性和类方法
@attention  : life is short,I need python
"""


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



# =========================================  面向对象 - 类方法 =========================================
# 设置对象属性
# flag = True
flag = False
if flag:

    class Tool(object):
        # 使用赋值语句定义类属性，记录所有工具对象的数量
        count = 0

        @classmethod
        def show_tool_count(cls):
            print("工具对象的数量 %d" % cls.count)

        def __init__(self, name):
            self.name = name

            # 让类属性的值+1
            Tool.count += 1

    # 创建工具对象
    tool1 = Tool("斧头")
    tool2 = Tool("榔头")

    # 调用类方法
    Tool.show_tool_count()


# =========================================  面向对象 - 静态方法 =========================================
# 设置对象属性
# flag = True
flag = False
if flag:

    class Dog(object):
        @staticmethod
        def run():
            # 不访问实例属性/类属性
            print("小狗要跑...")

    # 通过类名.调用静态方法 - 不需要创建对象
    Dog.run()


# =========================================  面向对象 - 综合案例 =========================================
# 设置对象属性
# flag = True
flag = False
if flag:

    class Game(object):
        # 历史最高分
        top_score = 0

        def __init__(self, player_name):
            self.player_name = player_name

        @staticmethod
        def show_help():
            print("帮助信息：让僵尸进入大门")

        @classmethod
        def show_top_score(cls):
            print("历史记录 %d" % cls.top_score)

        def start_game(self):
            print("%s 开始游戏啦..." % self.player_name)

    # 1. 查看游戏的帮助信息
    Game.show_help()

    # 2. 查看历史最高分
    Game.show_top_score()

    # 3. 创建游戏对象
    game = Game("小明")

    game.start_game()


# =========================================  面向对象 - __new__ =========================================
#
# flag = True
flag = False
if flag:

    class MusicPlayer(object):
        def __new__(cls, *args, **kwargs):
            # 1. 创建对象时，new方法会被自动调用
            print("创建对象，分配空间")

            # 2. 为对象分配空间
            instance = super().__new__(cls)

            # 3. 返回对象的引用
            return instance

        def __init__(self):
            print("播放器初始化")

    # 创建播放器对象
    player = MusicPlayer()

    print(player)


# =========================================  面向对象 - 单例 =========================================
#
# flag = True
flag = False
if flag:
    class MusicPlayer(object):

        # 记录第一个被创建对象的引用
        instance = None

        def __new__(cls, *args, **kwargs):
            # 1. 判断类属性是否是空对象
            if cls.instance is None:
                # 2. 调用父类的方法，为第一个对象分配空间
                cls.instance = super().__new__(cls)

            # 3. 返回类属性保存的对象引用
            return cls.instance

    # 创建多个对象
    player1 = MusicPlayer()
    print(player1)

    player2 = MusicPlayer()
    print(player2)

# =========================================  面向对象 - 单例 =========================================
# 单例初始化一次
# flag = True
flag = False
if flag:

    class MusicPlayer(object):

        # 记录第一个被创建对象的引用
        instance = None

        # 记录是否执行过初始化动作
        init_flag = False

        def __new__(cls, *args, **kwargs):

            # 1. 判断类属性是否是空对象
            if cls.instance is None:
                # 2. 调用父类的方法，为第一个对象分配空间
                cls.instance = super().__new__(cls)

            # 3. 返回类属性保存的对象引用
            return cls.instance

        def __init__(self):

            # 1. 判断是否执行过初始化动作
            if MusicPlayer.init_flag:
                return

            # 2. 如果没有执行过，在执行初始化动作
            print("初始化播放器")

            # 3. 修改类属性的标记
            MusicPlayer.init_flag = True

    # 创建多个对象
    player1 = MusicPlayer()
    print(player1)

    player2 = MusicPlayer()
    print(player2)


# =========================================  面向对象 - 私有属性私有方法 =========================================
#
# flag = True
flag = False
if flag:

    class Women:
        def __init__(self, name):
            self.name = name
            self.__age = 18

        def __secret(self):
            # 在对象的方法内部，是可以访问对象的私有属性的
            print("%s 的年龄是 %d" % (self.name, self.__age))

    xiaofang = Women("小芳")

    # 私有属性，在外界不能够被直接访问
    # print(xiaofang.__age)
    # 私有方法，同样不允许在外界直接访问
    # xiaofang.__secret()


# =========================================  面向对象 - 伪私有属性私有方法 =========================================
#
# flag = True
flag = False
if flag:

    class Women:
        def __init__(self, name):
            self.name = name
            self.__age = 18

        def __secret(self):
            # 在对象的方法内部，是可以访问对象的私有属性的
            print("%s 的年龄是 %d" % (self.name, self.__age))

    xiaofang = Women("小芳")

    # 伪私有属性，在外界不能够被直接访问
    print(xiaofang._Women__age)
    # 伪私有方法，同样不允许在外界直接访问
    xiaofang._Women__secret()
