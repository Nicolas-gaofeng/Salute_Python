#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : oo_2.py
@author     : zgf
@brief      : python面向对象 - 封装
@attention  : life is short,I need python
"""


# =========================================  面向对象 - 小明爱跑步 =========================================
#
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


# =========================================  面向对象 - 小美爱跑步 =========================================
#
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
    # 小美爱跑步
    xiaomei = Person("小美", 45)
    xiaomei.eat()
    xiaomei.run()
    print(xiaomei)
    print(xiaoming)


# =========================================  面向对象 - 摆放家具 =========================================
#
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


# =========================================  面向对象 - 士兵突击1 =========================================
#
# flag = True
flag = False
if flag:

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


# =========================================  面向对象 - 士兵突击2 =========================================
#
# flag = True
flag = False
if flag:

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
