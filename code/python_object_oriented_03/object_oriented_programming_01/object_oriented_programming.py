#!/usz/bin/env python
# -*- coding:utf-8 -*-


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
flag = True
# flag = False
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

    # 单例初始化一次
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


# =========================================  面向对象 - 例子 =========================================
# 小明爱跑步
# flag = True
flag = False
if flag:

    class Person:
        def __init__(self, name, weight):
            # self.属性 = 形参
            self.name = name
            self.weight = weight

        def __str__(self):
            return "我的名字叫 %s 体重是 %.2f 公斤" % (self.name, self.weight)

        def run(self):
            print("%s 爱跑步，跑步锻炼身体" % self.name)

            self.weight -= 0.5

        def eat(self):
            print("%s 是吃货，吃完这顿再减肥" % self.name)

            self.weight += 1

    xiaoming = Person("小明", 75.0)

    xiaoming.run()
    xiaoming.eat()

    print(xiaoming)
    # 扩展
    class Person:
        def __init__(self, name, weight):
            # self.属性 = 形参
            self.name = name
            self.weight = weight

        def __str__(self):
            return "我的名字叫 %s 体重是 %.2f 公斤" % (self.name, self.weight)

        def run(self):
            print("%s 爱跑步，跑步锻炼身体" % self.name)

            self.weight -= 0.5

        def eat(self):
            print("%s 是吃货，吃完这顿再减肥" % self.name)

            self.weight += 1

    xiaoming = Person("小明", 75.0)

    xiaoming.run()
    xiaoming.eat()

    print(xiaoming)

    # 小美爱跑步
    xiaomei = Person("小美", 45)

    xiaomei.eat()
    xiaomei.run()

    print(xiaomei)
    print(xiaoming)


# =========================================  面向对象 - 例子 =========================================
# 摆放家具
# flag = True
flag = False
if flag:
    # 家具类 添加家具
    class HouseItem:
        def __init__(self, name, area):
            self.name = name
            self.area = area

        def __str__(self):
            return "[%s] 占地 %.2f" % (self.name, self.area)

    class House:
        def __init__(self, house_type, area):
            self.house_type = house_type
            self.area = area

            # 剩余面积
            self.free_area = area

            # 家具名称列表
            self.item_list = []

        def __str__(self):
            # Python 能够自动的将一对括号内部的代码连接在一起
            return "户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s" % (
                self.house_type,
                self.area,
                self.free_area,
                self.item_list,
            )

        def add_item(self, item):
            print("要添加 %s" % item)
            # 1. 判断家具的面积
            if item.area > self.free_area:
                print("%s 的面积太大了，无法添加" % item.name)

                return

            # 2. 将家具的名称添加到列表中
            self.item_list.append(item.name)

            # 3. 计算剩余面积
            self.free_area -= item.area

    # 1. 创建家具
    bed = HouseItem("席梦思", 40)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 20)

    print(bed)
    print(chest)
    print(table)

    # 2. 创建房子对象
    my_home = House("两室一厅", 60)

    my_home.add_item(bed)
    my_home.add_item(chest)
    my_home.add_item(table)

    print(my_home)


# =========================================  面向对象 - 例子 =========================================
# 士兵突击
# flag = True
flag = False
if flag:
    # 枪类
    class Gun:
        def __init__(self, model):
            # 1. 枪的型号
            self.model = model

            # 2. 子弹的数量
            self.bullet_count = 0

        def add_bullet(self, count):
            self.bullet_count += count

        def shoot(self):
            # 1. 判断子弹数量
            if self.bullet_count <= 0:
                print("[%s] 没有子弹了..." % self.model)

                return

            # 2. 发射子弹，-1
            self.bullet_count -= 1

            # 3. 提示发射信息
            print("[%s] 突突突... [%d]" % (self.model, self.bullet_count))

    # 1. 创建枪对象
    ak47 = Gun("AK47")

    ak47.add_bullet(50)
    ak47.shoot()

    # 士兵类
    class Gun:
        def __init__(self, model):
            # 1. 枪的型号
            self.model = model

            # 2. 子弹的数量
            self.bullet_count = 0

        def add_bullet(self, count):
            self.bullet_count += count

        def shoot(self):
            # 1. 判断子弹数量
            if self.bullet_count <= 0:
                print("[%s] 没有子弹了..." % self.model)

                return

            # 2. 发射子弹，-1
            self.bullet_count -= 1

            # 3. 提示发射信息
            print("[%s] 突突突... [%d]" % (self.model, self.bullet_count))

    class Soldier:
        def __init__(self, name):
            # 1. 姓名
            self.name = name

            # 2. 枪 - 新兵没有枪
            self.gun = None

    # 1. 创建枪对象
    ak47 = Gun("AK47")

    ak47.add_bullet(50)
    ak47.shoot()

    # 2. 创建许三多
    xusanduo = Soldier("许三多")

    xusanduo.gun = ak47

    print(xusanduo.gun)

    # 改进  士兵开火
    class Gun:
        def __init__(self, model):
            # 1. 枪的型号
            self.model = model

            # 2. 子弹的数量
            self.bullet_count = 0

        def add_bullet(self, count):
            self.bullet_count += count

        def shoot(self):
            # 1. 判断子弹数量
            if self.bullet_count <= 0:
                print("[%s] 没有子弹了..." % self.model)

                return

            # 2. 发射子弹，-1
            self.bullet_count -= 1

            # 3. 提示发射信息
            print("[%s] 突突突... [%d]" % (self.model, self.bullet_count))

    class Soldier:
        def __init__(self, name):
            # 1. 姓名
            self.name = name

            # 2. 枪 - 新兵没有枪
            self.gun = None

        def fire(self):
            # 1. 判断士兵是否有枪
            # if self.gun == None:
            if self.gun is None:
                print("[%s] 还没有枪..." % self.name)

                return

            # 2. 高喊口号
            print("冲啊...[%s]" % self.name)

            # 3. 让枪装填子弹
            self.gun.add_bullet(50)

            # 4. 让枪发射子弹
            self.gun.shoot()

    # 1. 创建枪对象
    ak47 = Gun("AK47")

    # 2. 创建许三多
    xusanduo = Soldier("许三多")

    xusanduo.gun = ak47
    xusanduo.fire()

    print(xusanduo.gun)


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
