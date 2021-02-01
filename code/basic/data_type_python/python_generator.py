#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : python_generator.py
@author     : zgf
@brief      : 生成器
@attention  : life is short,I need python
"""


# =========================================  列表生成器 =========================================
# 程序缺点：占用大量内存
# flag = True
flag = False
if flag:
    ls = [i ** 2 for i in range(1, 1000001)]
    for i in ls:
        pass


# =========================================  斐波那契数列 =========================================
# 生产斐波那契数列 - 数列前两个元素为1,1 之后的元素为其前两个元素之和
# flag = True
flag = False
if flag:

    def fib(max):
        ls = []
        n, a, b = 0, 1, 1
        while n < max:
            ls.append(a)
            a, b = b, a + b
            n = n + 1
        return ls

    print(fib(10))

    # print()每次函数运行都要打印，占内存，所以为了不占内存，我们也可以使用生成器
    def fib(max):
        n, a, b = 0, 1, 1
        while n < max:
            print(a)
            a, b = b, a + b
            n = n + 1

    fib(10)

    print("yield()".center(50, "*"))

    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1
        return "done"

    a = fib(10)
    print(fib(10))
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print("可以顺便干其他事情")
    print(a.__next__())
    print(a.__next__())

    print("for循环调用".center(50, "*"))
    # for循环调用generator时，发现拿不到generator的return语句的返回值
    for i in fib(6):
        print(i)

    print("捕获StopIteration错误".center(50, "*"))
    g = fib(6)
    while True:
        try:
            x = next(g)
            print("generator: ", x)
        except StopIteration as e:
            print("生成器返回值：", e.value)
            break


# =========================================  生成器函数 =========================================
# 生成器：就是自己python用代码写的迭代器，生成器的本质就是迭代器。生成器都是迭代器
# （1）采用惰性计算的方式
# （2）无需一次性存储海量数据
# （3）一边执行一边计算，只计算每次需要的值
# （4）实际上一直在执行next()操作，直到无值可取
# yield return
# return 结束函数，给函数的执行者返回值
# yield 不会结束函数，一个next对应一个yield，给  生成器对象.__next__() 返回值。
# flag = True
flag = False
if flag:
    # 用以下两种方式构建一个生成器:
    # 1，通过生成器函数。
    # 2，生成器表达式。

    # 生成器函数
    def func1(x):
        x += 1
        print(1111)
        print(1111)
        print(1111)
        print(1111)
        print(1111)
        print(1111)
        yield x
        x += 2
        print(2222)
        yield "alex"

        x += 3

    g_obj = func1(5)  # 生成器函数对象
    print(g_obj)  # <generator object func1 at 0x0000025E5D618780>
    print(g_obj.__next__())
    print(g_obj.__next__())
    # 一个next 对应一个 yield
    # yield 将值返回给  生成器对象.__next__()


# =========================================  生成器表达式 =========================================
#
# flag = True
flag = False
if flag:
    # 海量数据，不需存储
    squares = (i ** 2 for i in range(1000000))
    for i in squares:
        pass
    sum((i for i in range(101)))


# =========================================  send 与 next =========================================
# send 与next一样，也是对生成器取值（执行一个yield）的方法。
# send 可以给上一个yield 传值。
# 第一次取值永远都是next。
# 最后一个yield 永远也得不到send传的值。
# flag = True
flag = False
if flag:

    def func1():
        # print(1)
        count = yield 6
        print(count)
        # print(2)
        count1 = yield 7
        print(count1)
        # print(3)
        yield 8

    g = func1()
    print(next(g))
    # g.send('alex')
    g.send("alex")
    g.send("太白")
    # g.send("太白")

    # def cloth1(n):
    #     for i in range(n+1):
    #         print('衣服%s号' % i)
    # cloth1(100000)
    def cloth2(n):
        for i in range(1, n + 1):
            yield "衣服%s号" % i

    g = cloth2(10000)
    for i in range(50):
        print(g.__next__())


# =========================================  生成器函数 vs 迭代器 =========================================
# 生成器函数 vs 迭代器
# flag = True
flag = False
if flag:

    #  自定制的区别
    l1 = [1, 2, 3, 4, 5]
    l1.__iter__()

    def func1(x):
        x += 1
        yield x
        x += 3
        yield x
        x += 5
        yield x

    g1 = func1(5)
    print(g1.__next__())
    print(g1.__next__())
    print(g1.__next__())

    def func1():
        for i in range(1000000):
            yield i

    g1 = func1()
    for i in range(50):
        print(g1.__next__())
