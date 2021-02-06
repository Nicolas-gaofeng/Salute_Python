#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : oo_3.py
@author     : zgf
@brief      : python面向对象 - 继承
@attention  : life is short,I need python
"""

# =========================================  面向对象 继承 - 初识 =========================================
#  不使用继承开发动物和狗
# flag = True
flag = False
if flag:

    class Animal:
        def eat(self):
            print("吃")

        def drink(self):
            print("喝")

        def run(self):
            print("跑")

        def sleep(self):
            print("睡")

    class Dog:
        def eat(self):
            print("吃")

        def drink(self):
            print("喝")

        def run(self):
            print("跑")

        def sleep(self):
            print("睡")

        def bark(self):
            print("汪汪叫")

    # 创建一个对象 - 狗对象
    wangcai = Dog()

    wangcai.eat()
    wangcai.drink()
    wangcai.run()
    wangcai.sleep()
    wangcai.bark()


# =========================================  面向对象 继承 - 初识 =========================================
#  使用继承开发动物和狗
# flag = True
flag = False
if flag:

    class Animal:
        def eat(self):
            print("吃---")

        def drink(self):
            print("喝---")

        def run(self):
            print("跑---")

        def sleep(self):
            print("睡---")

    class Dog(Animal):

        # 子类拥有父类的所有属性和方法
        # def eat(self):
        #     print("吃")
        #
        # def drink(self):
        #     print("喝")
        #
        # def run(self):
        #     print("跑")
        #
        # def sleep(self):
        #     print("睡")

        def bark(self):
            print("汪汪叫")

    # 创建一个对象 - 狗对象
    wangcai = Dog()

    wangcai.eat()
    wangcai.drink()
    wangcai.run()
    wangcai.sleep()
    wangcai.bark()


# =========================================  面向对象 继承 - 继承的传递性 =========================================
#   继承的传递性
# flag = True
flag = False
if flag:

    class Animal:
        def eat(self):
            print("吃---")

        def drink(self):
            print("喝---")

        def run(self):
            print("跑---")

        def sleep(self):
            print("睡---")

    class Dog(Animal):
        def bark(self):
            print("汪汪叫")

    class XiaoTianQuan(Dog):
        def fly(self):
            print("我会飞")

    # 创建一个哮天犬的对象
    xtq = XiaoTianQuan()

    xtq.fly()
    xtq.bark()
    xtq.eat()


# =========================================  面向对象 继承 - 继承的传递性 =========================================
# 继承传递性注意事项
# flag = True
flag = False
if flag:

    class Animal:
        def eat(self):
            print("吃---")

        def drink(self):
            print("喝---")

        def run(self):
            print("跑---")

        def sleep(self):
            print("睡---")

    class Dog(Animal):
        def bark(self):
            print("汪汪叫")

    class XiaoTianQuan(Dog):
        def fly(self):
            print("我会飞")

    class Cat(Animal):
        def catch(self):
            print("抓老鼠")

    # 创建一个哮天犬的对象
    xtq = XiaoTianQuan()

    xtq.fly()
    xtq.bark()
    xtq.eat()


# =========================================  面向对象 继承 - 覆盖父类的方法 =========================================
#
# flag = True
flag = False
if flag:

    class Animal:
        def eat(self):
            print("吃---")

        def drink(self):
            print("喝---")

        def run(self):
            print("跑---")

        def sleep(self):
            print("睡---")

    class Dog(Animal):
        def bark(self):
            print("汪汪叫")

    class XiaoTianQuan(Dog):
        def fly(self):
            print("我会飞")

        def bark(self):
            print("叫得跟神一样...")

    xtq = XiaoTianQuan()

    # 如果子类中，重写了父类的方法
    # 在使用子类对象调用方法时，会调用子类中重写的方法
    xtq.bark()


# =========================================  面向对象 继承 - 扩展父类的方法 =========================================
#
# flag = True
flag = False
if flag:

    class Animal:
        def eat(self):
            print("吃---")

        def drink(self):
            print("喝---")

        def run(self):
            print("跑---")

        def sleep(self):
            print("睡---")

    class Dog(Animal):
        def bark(self):
            print("汪汪叫")

    class XiaoTianQuan(Dog):
        def fly(self):
            print("我会飞")

        def bark(self):
            # 1. 针对子类特有的需求，编写代码
            print("神一样的叫唤...")

            # 2. 使用 super(). 调用原本在父类中封装的方法
            # super().bark()

            # 父类名.方法(self)
            Dog.bark(self)
            # 注意：如果使用子类调用方法，会出现递归调用 - 死循环！
            # XiaoTianQuan.bark(self)

            # 3. 增加其他子类的代码
            print("$%^*%^$%^#%$%")

    xtq = XiaoTianQuan()

    # 如果子类中，重写了父类的方法
    # 在使用子类对象调用方法时，会调用子类中重写的方法
    xtq.bark()


# =========================================  面向对象 继承 - 父类的私有属性和私有方法 =========================================
#
# flag = True
flag = False
if flag:

    class A:
        def __init__(self):
            self.num1 = 100
            self.__num2 = 200

        def __test(self):
            print("私有方法 %d %d" % (self.num1, self.__num2))

    class B(A):
        def demo(self):
            # 1. 在子类的对象方法中，不能访问父类的私有属性
            # print("访问父类的私有属性 %d" % self.__num2)

            # 2. 在子类的对象方法中，不能调用父类的私有方法
            # self.__test()
            pass

    # 创建一个子类对象
    b = B()
    print(b)

    b.demo()

    # 在外界不能直接访问对象的私有属性/调用私有方法
    # print(b.__num2)
    # b.__test()


# =========================================  面向对象 继承 - 父类的公有方法 =========================================
#
# flag = True
flag = False
if flag:

    class A:
        def __init__(self):
            self.num1 = 100
            self.__num2 = 200

        def __test(self):
            print("私有方法 %d %d" % (self.num1, self.__num2))

        def test(self):
            print("父类的公有方法 %d" % self.__num2)

            self.__test()

    class B(A):
        def demo(self):
            # 1. 在子类的对象方法中，不能访问父类的私有属性
            # print("访问父类的私有属性 %d" % self.__num2)

            # 2. 在子类的对象方法中，不能调用父类的私有方法
            # self.__test()

            # 3. 访问父类的公有属性
            print("子类方法 %d" % self.num1)

            # 4. 调用父类的公有方法
            self.test()
            pass

    # 创建一个子类对象
    b = B()
    print(b)

    b.demo()
    # 在外界访问父类的公有属性/调用公有方法
    # print(b.num1)
    # b.test()

    # 在外界不能直接访问对象的私有属性/调用私有方法
    # print(b.__num2)
    # b.__test()


# =========================================  面向对象 多继承 =========================================
#
# flag = True
flag = False
if flag:

    class A:
        def test(self):
            print("test 方法")

    class B:
        def demo(self):
            print("demo 方法")

    class C(A, B):
        """多继承可以让子类对象，同时具有多个父类的属性和方法"""

        pass

    # 创建子类对象
    c = C()

    c.test()
    c.demo()


# =========================================  面向对象  多继承的使用注意事项 =========================================
#
# flag = True
flag = False
if flag:

    class A:
        def test(self):
            print("A --- test 方法")

        def demo(self):
            print("A --- demo 方法")

    class B:
        def test(self):
            print("B --- test 方法")

        def demo(self):
            print("B --- demo 方法")

    class C(B, A):
        """多继承可以让子类对象，同时具有多个父类的属性和方法"""

        pass

    # 创建子类对象
    c = C()

    c.test()
    c.demo()

    # 确定C类对象调用方法的顺序
    print(C.__mro__)
