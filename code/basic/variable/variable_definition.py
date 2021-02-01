#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : variable_definition.py
@author     : zgf
@brief      : python变量创建
@attention  : life is short,I need python
"""


# =========================================  变量赋值 =========================================
# 赋值方式1：通过等号自右向左进行赋值
# 赋值方式2：增量赋值
# 赋值方式3：打包赋值
# 定义变量会有：id(唯一标识号）,type(变量类型）,value(变量值）
# flag = True
flag = False
if flag:
    x = 1 + 2  # 赋值方式1：通过等号自右向左进行赋值
    print(x)
    y = 10
    y += 10  # 赋值方式2：增量赋值
    print(y)
    u, v = 1, 2  # 赋值方式3：打包赋值
    print(u, v)
    v, u = u, v
    print(u, v)

    # 1.id相同，意味着type和value必定相同 is比较id
    # 2.value相同type肯定相同，但id可能不同 ==
    x = "sadasfgdafsdaaaaasadasfgdafsdaaaaasadasfgdafsdaaaaasadasfgdafsdaaaaa"
    y = "sadasfgdafsdaaaaasadasfgdafsdaaaaasadasfgdafsdaaaaasadasfgdafsdaaaaa"
    print(x, id(x), type(x))
    print(y, id(y), type(y))
    print(x == y)
    print(x is y)


# =========================================  变量的类型 =========================================
# 在 Python 中定义变量时不需要指定类型，Python 可以根据等号右侧的值，自动推导出变量中存储数据的类型
# 定义变量不用数据类型声明，且确定一个变量的类型是第一次给他赋值的时候
# Python属于强类型的动态脚本语言：不允许不同类型相加
# 使用type()可以查看一个变量的类型
# flag = True
flag = False
if flag:
    # str 表示是一个字符串类型
    name = "小明"
    # int 表示是一个整数类型
    age = 18
    # bool 表示是一个布尔类型，真 True 或者假 False
    gender = False  # 不是
    # float 表示是一个小数类型，浮点数
    height = 1.75
    weight = 75
    print(name)

    """type()"""
    print(type(height))
    print(type(weight))
    print(type(name))

# =========================================  变量类型转换 =========================================
# 数字类型转字符串 str(数字类型)
# int()： 函数用于将一个字符串或数字转换为整型。有去除空格的功能和取整数的功能
# float()：函数用于将整数和字符串转换成浮点数。
# eval()：函数用于去掉引号
# flag = True
flag = False
if flag:
    """数字类型转字符串 str(数字类型)"""
    print("str()".center(50, "*"))
    age = 20
    print("My age is " + str(age))
    print("str() - end".center(50, "*"))

    """int() 仅有数字组成的字符串转数字 """
    print("int()".center(50, "*"))
    print(int("20"))  # 只能为整形
    print(int("   5"), type(int("   5")))  # 去除空格
    print(int("123"))
    print(int(3.74))  # 取整 不是四舍五入
    print(int("0101", base=2))  # 将2进制的 0100 转化成十进制。结果为 4
    print("int() - end".center(50, "*"))

    """float()  仅有数字组成的字符串转数字"""
    print("float()".center(50, "*"))
    print(float("20"))
    print(float("10.1"))
    print("float() - end".center(50, "*"))

    """eval()  仅有数字组成的字符串转数字"""
    print("eval()".center(50, "*"))
    print(eval("20"))
    print(eval("10.1"))

    x = input("请输入一个数字：")
    print(x, type(x))
    x = eval(x)
    print(x, type(x))

    # eval: 执行字符串类型的代码，并返回最终结果
    s1 = "1+2+3"
    print(s1)
    s2 = "{'name':'alex'}"
    print(eval(s1), type(eval(s1)))
    print(eval(s2), type(eval(s2)))
    print("eval() - end".center(50, "*"))


# =========================================  example - 整数加法计算器 =========================================
# 整数加法计算器
# flag = True
flag = False
if flag:
    # 方法一
    content = input("请输入内容：").strip()  # 5+9 100 +99    22 + 34
    plus_index = content.find("+")
    num1 = content[:plus_index]  # '5'
    num2 = content[plus_index + 1 :]  # '9'
    result = int(num1) + int(num2)
    print(result)
    # 方法二
    content = input("请输入内容：").strip()
    num_list = content.split("+")
    result = int(num_list[0]) + int(num_list[1])
    print(result)
