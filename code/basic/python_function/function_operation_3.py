#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : function_operation_3.py
@author     : zgf
@brief      : 内置函数
@attention  : life is short,I need python
"""


# =========================================  函数 - hash()函数 =========================================
# 1.2.3内存相关 hash id ***
#
# 　　hash：获取一个对象（可哈希对象：int，str，Bool，tuple）的哈希值。
#     id:获取该对象的内存地址。

# hash()
# 字典：会将你的所有的key 在内存中转化成id
# flag = True
flag = False
if flag:

    dic = {"name": "alex", "kfdshjfhdskjfhsd": "123"}
    print(hash("name"))
    print(hash("name1"))
    print(hash("fdsmkfghsdlksld"))
    print(hash(1))
    print(hash(100))
    print(hash(100000000000))
    print(hash([1, 2, 3]))


# =========================================  函数 - 内置函数 =========================================
#
# flag = True
flag = False
if flag:
    """
    len()
    range()
    min()
    max()
    input()
    print()
    id()
    type()
    int()
    list()
    str()
    set()
    next()
    tuple()
    iter()
    bool()
    dict()
    globals()
    dir()
    enmurate()
    locals()
    open()
    send()
    """
    # 作用域相关  ******
    # globals() :返回一个字典：包含全部的全局变量。
    # locals() ： 返回一个字典：包含的是当前作用域 所有的变量。
    b = 2

    def func1():
        a = 1
        print(locals())
        print(globals())

    func1()

    # # exec 执行字符串类型的代码，不返回结果  代码流
    s3 = """for i in range(3):
        print(i)
    """
    print(exec(s3))
    exec(s3)

    # 1.2.3文件操作相关
    #
    # 　　open：函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。 *****
    #
    # 1.2.4模块相关__import__　 ***
    #
    # 　　__import__：函数用于动态加载类和函数 。

    # 1.2.5帮助
    #
    # 　　help：函数用于查看函数或模块用途的详细说明。 **
    # name = 'alex'
    # print(help(name))

    # 1.2.6调用相关
    #
    # 　　callable：函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；
    # 但如果返回False，调用对象ojbect绝对不会成功。  ***
    name = "alex"

    def func1():
        pass

    print(callable(name))  # False
    print(callable(func1))  # True # 可以被调用
    #
    # 1.2.7查看内置属性  ***
    #
    # 　　dir：函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
    # 如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
    # name = 'alex'
    # print(dir(name))

    # range：函数可创建一个整数对象，一般用在 for 循环中。
    #  python2x: range(3) ---> [0,1,2] 列表
    #            xrange(3) ---> 迭代器。
    #  python3x: range(3) ---> range(0,3) 可迭代对象

    # 　　next：内部实际使用了__next__方法，返回迭代器的下一个项目。
    # 　　iter：函数用来生成迭代器（讲一个可迭代对象，生成迭代器）。


# ========================================= bytearry()   =========================================
# bytearry：返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
# flag = True
flag = False
if flag:

    # [97,110,103,115]
    ret = bytearray("alex", encoding="utf-8")
    print(id(ret))
    print(ret)  # bytearray(b'alex')
    print(ret[0])  # 97
    ret[0] = 65
    print(ret)  # bytearray(b'Alex')
    print(id(ret))


# ========================================= memoryview()   =========================================
#
# flag = True
flag = False
if flag:
    ret = memoryview(bytes("你好", encoding="utf-8"))
    print(len(ret))  # 6
    print(ret)  # <memory at 0x000001D3D6FCD048>  # [\xe4,\xbd,\xa0,\xe5,\xa5,\xbd]
    print(bytes(ret[:3]).decode("utf-8"))  # 你
    print(bytes(ret[3:]).decode("utf-8"))  # 好


# ========================================= zip()  =========================================
# zip：函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。 *****
#     如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。
#     拉链方法  将多个iter 纵向组成一个个元组。
# flag = True
flag = False
if flag:

    l1 = [1, 2, 3, 5, 6, 7]
    tu1 = ("alex", "太白", "wusir", "女神")
    dic = {"name": "日天", "age": 28, "hobby": "tea", "weight": 100}
    print(zip(l1, tu1, dic))
    for i in zip(l1, tu1, dic):
        print(i)


# ========================================= filter()  =========================================
# filter：过滤· 迭代器。 *****
# flag = True
flag = False
if flag:

    l1 = [i for i in range(10)]

    def func1(x):
        return x % 2 == 0

    print(list(filter(func1, l1)))


# ========================================= map()  =========================================
# filter：过滤· 迭代器。 *****
# flag = True
flag = False
if flag:
    l1 = [1, 2, 3, 4]
    # print([i**2 for i in l1])
    def func(x):
        return x ** 2

    print(list(map(func, l1)))

    # print() sum reversed
    # key : min max map sorted filter zip


# ========================================= repr()   =========================================
# repr()  json pickle序列化模块 特殊字符串，python字符串的区别
# flag = True
# flag = False
if flag:
    # repr:返回一个对象的string形式（原形毕露）。  *****
    print("alex")
    print(repr("ale,x"))
    print(repr("{'alex':'sb'}"))

    # 格式化输出 %r
    msg = "alex 是 %r的人" % ("德高望重")
    print(msg)
