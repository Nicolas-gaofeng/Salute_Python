#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : python_coding.py
@author     : zgf
@brief      : 认识python
@attention  : life is short,I need python
"""

# =========================================  小数据池（缓存机制，驻留机制） =========================================

# flag = True
flag = False
if flag:
    """"""
    # 小数据池的应用的数据类型： 整数，字符串，bool值
    # 小数据池，python对内存做的一个优化：
    # 他将 -5 ~256 的整数，以及一定规则的字符串，提前在内存中创建了池，容器，
    # 容器里固定的放了这些数。
    # 字符串的长度为0或者1,默认都采用了驻留机制（小数据池）。
    # 字符串的长度>1,且只含有大小写字母，数字，下划线时，才会默认驻留。
    # 用乘法得到的字符串，分两种情况。
    # 1.乘数为1时：仅含大小写字母，数字，下划线，默认驻留。 含其他字符，长度<=1,默认驻留。 含其他字符，长度>1,默认驻留。
    # 2.乘数>=2时：仅含大小写字母，数字，下划线，总长度<=20，默认驻留。
    # 只要运行Python解释器，自动创建小数据池
    # 为什么这么做？？？
    # 1，节省内存。
    # 2，提高性能与效率。


# =========================================  代码块： =========================================
# is比较id
# ==比较值
# 在内存中id都是唯一的，如果两个变量指向的值的id相同，就证明他们在内存中是同一个。
#  is 判断的是两个变量的id值是否相同。
# 与None值比较 ***判断某个变量是否为None时，请使用is 而不是==***
# 如果is是True, == 一定是True。
# flag = True
flag = False
if flag:
    """代码块："""
    # python在同一个代码块中的变量，初始化对象的命令时，它会将变量与值的对应关系放到一个字典中，
    # 如果下面的代码在遇到初始化对象的命令，他会先从字典中寻找，如果存在相同的值，他会复用，指向的都是同一个内存地址。
    # dic = {'name': alex@的内存地址，}
    # python对于不同的代码块：初始化对象的命令时，他会从小数据池中寻找。
    # 小数据池与代码块的关系。
    # 同一个代码块：python在执行时，遇到了初始化对象命令，他会将这个变量名和数值放到一个字典中， 再次遇到他会从这字典中寻找。
    # 不同代码块：python在执行时，直接从小数据池中寻找，满足条件id相同。
    i1 = 100
    i2 = 100
    i3 = 100000000
    i4 = 100000000
    print(i1 is i2)
    print(i3 is i4)
    # 一定规则的字符串？

    # s1 = 'alex@'
    # s2 = 'alex@'
    # print(s1 is s2)


# ========================================= 编码 =========================================
#
# flag = True
flag = False
if flag:
    pass


# =========================================  字符编码 =========================================
# 将中文字库，英文字母、数字、特殊字符等转化成计算机可识别的二进制数
# 每个单一字符对应一个唯一的互不重复的二进制编码
# Python 中使用的是Unicode编码
# 你想将一部分内容（字符串）写入文件，或者通过网络socket传输，这样这部分内容（字符串）必须转化成bytes才可以进行
# 平时你代码中，使用字符串。

# flag = True
flag = False
if flag:
    #  进制转换（3）：
    # bin：将十进制转换成二进制并返回。
    print(bin(100))  # 0b1100100
    # oct：将十进制转化成八进制字符串并返回。
    print(oct(7))  # 0o7
    print(oct(8))  # 0o10
    print(oct(9))  # 0o10
    # hex：将十进制转化成十六进制字符串并返回。
    print(hex(10))  # 0xa
    print(hex(15))  # 0xf
    print(hex(17))  # 0xf
    # ord:输入字符找该字符编码 unicode  的位置  **
    print(ord("a"))
    print(ord("中"))

    # 将字符转化为Unicode码——ord(字符)
    print(ord("1"))
    print(ord("a"))
    print(ord("*"))
    print(ord("中"))
    print(ord("国"))
    # chr:输入位置数字找出其对应的字符 unicode **
    print(chr(97))
    print(chr(20013))

    # 将Unicode码转化为字符——chr(Unicode码)
    print(chr(1010))
    print(chr(10000))
    print(chr(12345))
    print(chr(23456))
    # ascii:是ascii码中的返回该值，不是则返回他在unicode的位置（16进制。） **
    print(ascii("a"))
    print(ascii("中"))  # '\u4e2d'
    # bytes：unicode ---> bytes 类型  ****
    # a1 = '太白'
    # # print(a1.encode('utf-8'))
    # print(a1.encode('utf-8').decode())

    # bytes：unicode ---> bytes 类型
    # a1 = '太白'
    # b1 = bytes(a1,encoding='utf-8')
    # print(b1)

    s1 = "太白"
    # print(s1)
    """str --- > bytes encode 编码"""
    s1 = "alex"
    s2 = "太白"
    b1 = s1.encode("utf-8")
    print(b1)
    b2 = s2.encode("gbk")
    print(b2)

    """bytes ---> str decode 解码"""
    b1 = b"\xcc\xab\xb0\xd7"  # gbk 的bytes
    s2 = b1.decode("gbk")
    print(s2)
    """gbk的bytes utf-8的bytes---> 英文字母、数字、特殊字符可以互相转化，他们引用的都是ascii"""


