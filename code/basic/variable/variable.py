#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : variable.py
@author     : zgf
@brief      : python变量
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


# =========================================  变量的输入 =========================================
# 使用解释器执行，如果要输出变量的内容，必须要使用 print 函数
# 如果要获取用户在 键盘上的输入信息，需要使用到 input 函数
# input:函数接受一个标准输入数据，返回为 string 类型，即数据输出的是一个字符串 。
# 用户输入的 任何内容 Python 都认为是一个字符串
# 变量中存储的值，就是可以变的
# flag = True
flag = False
if flag:
    x = input("请输入一个数字：")
    print(x, type(x))

    # 1.输入苹果单价，并将苹果单价转换成小数
    price = float(input("请输入苹果价格："))
    # 2.要求苹果重量，并将苹果重量转换成小数
    weight = float(input("请输入苹果重量："))
    # 3>计算付款金额
    money = price * weight
    print(money)


# ========================================= 变量的输出 - print()=========================================
# 在默认情况下，print 函数输出内容之后，会自动在内容末尾增加换行
# flag = True
flag = False
if flag:
    # print():打印输出。
    print("666")
    print(1, 2, 3, 4)  # 1 2 3 4
    print(*[1, 2, 3])  # 1 2 3

    # print()： 组合输出
    PI = 3.1415926
    E = 2.71828
    print("PI = ", PI, "E = ", E)

    # print()： 默认换行
    print(1)  # 默认换行
    print(2)  # 默认换行
    print(123, end="")  # 换行控制end=
    print(123, end="留在这里")  # 换行控制end可自定义
    print("*", end="---")
    print("*")


# =========================================  变量的输出 - print() -格式化输出 =========================================
# %d %s %f
# flag = True
flag = False
if flag:
    # %s
    name = "大小明"
    print("我的名字叫 %s，请多多关照！" % name)

    # %d
    student_no = 100123456
    print("我的学号是 %06d" % student_no)

    # 组合输出：方式一
    print("姓名为%s，学号为%d" % (name, student_no))
    # 组合输出：方式二
    print("姓名为%(name)s，学号为%(student_no)d" % {"name": name, "student_no": student_no})

    # %f
    price = 8.5
    weight = 7.5
    money = price * weight
    print("苹果单价 %.2f 元／斤，购买了 %.3f 斤，需要支付 %.4f 元" % (price, weight, money))

    # 在格式化输出中，只想单纯表示一个 % 号时，应该用 % % 表示
    scale = 0.8
    print("数据比例是 %.2f%%" % (scale * 100))

    """顺序填充输出"""
    PI = 3.1415926
    E = 2.71828
    print("PI = {0} , E = {1}".format(PI, E))  # 基本格式：“字符{0}字符{1}.format(v0,v1)”
    print("PI = {} , E = {}".format(PI, E))  # 按顺序分配
    print("PI = {1} , E = {0}".format(PI, E))  # 指定顺序分配
    print("PI = {0} , E = {0}".format(PI, E))  # 指定顺序分配

    print("我叫{name},今年{age},性别{sex}".format(age="28", name="zhangsna", sex="男"))

    """填充输出"""
    print("PI = {0:_^20}".format(PI))  # 0代表占位符 ：表示对变量进行修饰 _表示填充的图案 ^表示中间 20表示输出的宽度
    print("PI = {0:*<20}".format(PI))  # 0代表占位符 ：表示对变量进行修饰 _表示填充的图案 <表示左对齐 20表示输出的宽度
    print("PI = {0:_>30}".format(PI))  # 0代表占位符 ：表示对变量进行修饰 _表示填充的图案 >表示右对齐 20表示输出的宽度

    """数字千分位分隔符"""
    print("{0:,}".format(10000000))  # 数字千分位分隔符：在：后加，如果需要填充 ， 需要在最后
    print("{0:&>20,}".format(10000000))  # 第一步必须是填充
    # print("{0:,&>20}".format(10000000))  # 第一步必须是填充 不能先表示分隔符

    """浮点数简化输出"""
    print("{0:.2f}".format(PI))  # 留两位小数
    print("{0:.3f}".format(PI))
    print("{0:.1%}".format(0.818727))  # 按百分号输出
    print("{0:.2%}".format(0.817819))
    print("{0:.2e}".format(0.818727))  # 科学计数法输出

    """整数的进制转换输出"""
    print("二进制{0:b},Unicode码{0:c},十进制{0:d},八进制{0:o},十六进制{0:x}".format(450))


# =========================================  变量的引用 =========================================
# 函数的参数传递以及返回值都是靠引用传递的
# flag = True
flag = False
if flag:
    pass


# =========================================  全局变量 - 定义 =========================================
# 全局变量是在 函数外部定义的变量，所有函数内部都可以使用这个变量
# flag = True
flag = False
if flag:
    """定义一个全局变量"""
    num = 10

    def demo1():
        print(num)

    def demo2():
        print(num)

    demo1()
    demo2()
    print("over")


# =========================================  全局变量 - 修改全局变量=========================================
# 不允许直接修改全局变量的引用 —— 使用赋值语句修改全局变量的值
# 如果在函数中需要修改全局变量，需要使用 global 进行声明
# flag = True
flag = False
if flag:
    num = 10

    def demo1():
        # 注意：只是在函数内部定义了一个局部变量而已，不会修改到全局变量，只是变量名相同 —— 在函数内部不能直接修改全局变量的值
        num = 100
        print(num)

    def demo2():
        print(num)

    def demo3():
        # global关键字，告诉Python解释器num是一个全局变量
        global num
        # 只是定义了一个局部变量，不会修改到全局变量，只是变量名相同而已
        num = 100
        print(num)

    print("不允许直接修改全局变量的引用".center(50, "*"))
    demo1()
    demo2()
    print("over".center(50, "*"))

    print("使用global声明修改全局变量的引用".center(50, "*"))
    demo3()
    demo1()
    demo2()
    print("over".center(50, "*"))


# =========================================  局部变量 =========================================
# 局部变量 是在 函数内部 定义的变量，只能在函数内部使用
# 函数执行结束后，函数内部的局部变量，会被系统回收
# 不同的函数，可以定义相同的名字的局部变量，但是 彼此之间 不会产生影响
# flag = True
flag = False
if flag:

    def demo1():
        num = 10
        print(num)
        num = 20
        print("修改后 %d" % num)

    def demo2():
        num = 100
        print(num)

    demo1()
    demo2()
    print("over")


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
