#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : variable_output.py
@author     : zgf
@brief      : python变量输入
@attention  : life is short,I need python
"""


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

    print(1, 2, 3, sep="|")  # sep 打印多个内容是分隔符默认是空格


# =========================================  变量的输出 - print() -格式化输出 - 单 =========================================
# %d %s %f
# flag = True
flag = False
if flag:
    PI = 3.1415926
    E = 2.71828
    # %s
    name = "大小明"
    print("我的名字叫 %s，请多多关照！" % name)

    # %d
    student_no = 100123456
    print("我的学号是 %06d" % student_no)

    # %f
    price = 8.5
    print("苹果单价 %.2f 元／斤" % price)

    # 在格式化输出中，只想单纯表示一个 % 号时，应该用 % % 表示
    scale = 0.8
    print("数据比例是 %.2f%%" % (scale * 100))

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


# =========================================  变量的输出 - print() -格式化输出 -多 =========================================
# %d %s %f 组合输出
# flag = True
flag = False
if flag:
    # %s
    name = "大小明"
    # %d
    student_no = 100123456

    # 组合输出：方式一
    print("姓名为%s，学号为%d" % (name, student_no))
    # 组合输出：方式二
    print("姓名为%(name)s，学号为%(student_no)d" % {"name": name, "student_no": student_no})
    # 组合输出：方式三
    print("我叫{name},今年{age},性别{sex}".format(age="28", name="zhangsna", sex="男"))

    """顺序填充输出"""
    PI = 3.1415926
    E = 2.71828
    print("PI = {0} , E = {1}".format(PI, E))  # 基本格式：“字符{0}字符{1}.format(v0,v1)”
    print("PI = {} , E = {}".format(PI, E))  # 按顺序分配
    print("PI = {1} , E = {0}".format(PI, E))  # 指定顺序分配
    print("PI = {0} , E = {0}".format(PI, E))  # 指定顺序分配


# =========================================  变量的输出 - print() - 骚操作 - flush=========================================
# flush
# flag = True
flag = False
if flag:
    import time

    num = 20
    for i in range(num):
        print("#", end="", flush=True)
        time.sleep(1)


# =========================================  变量的输出 - print() - 骚操作 - 百分比=========================================
# 进度百分比
# flag = True
flag = False
if flag:
    import time

    days = 365
    for i in range(days):
        print("\r", "进度百分比：{0}%".format(round(i + 1) * 100 / days), end="", flush=True)
        time.sleep(0.02)


# =========================================  变量的输出 - print() - 骚操作 - tqdm百分比=========================================
# tqdm进度百分比
# flag = True
flag = False
if flag:
    from tqdm import tqdm

    for i in tqdm(range(10000)):
        pass


# =========================================  变量的输出 - print() - 骚操作 - progressbar百分比=========================================
# progressbar进度百分比
flag = True
# flag = False
if flag:
    import time
    from progressbar import *

    progress = ProgressBar()
    for i in progress(range(1000)):
        time.sleep(0.02)
