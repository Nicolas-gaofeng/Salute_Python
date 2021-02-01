#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : conditional_branching_structure.py
@author     : zgf
@brief      : 条件分支结构 - if 嵌套循环
@attention  : life is short,I need python
"""


# =========================================  if循环嵌套 - 飞行员 =========================================
#
# flag = True
flag = False
if flag:
    vision = 6.0
    if not vision > 5.0:
        print("视力太差，不能做飞行员")
    else:
        user_height = int(input("请输入身高："))
        if user_height == 183:
            user_weight = int(input("请输入体重："))
            if user_weight == 75:
                print("可以做飞行员")
            else:
                print("体重不合格，不能做飞行员")

        else:
            print("身高不合格，不能做飞行员")


# =========================================  if循环嵌套 - 过安检 =========================================
# 1. 定义布尔型变量 has_ticket 表示是否有车票
# 2. 定义整型变量 knife_length 表示刀的长度，单位：厘米
# 3. 首先检查是否有车票，如果有，才允许进行 **安检**
# 4. 安检时，需要检查刀的长度，判断是否超过 20 厘米
# 5. 如果没有车票，不允许进门
# flag = True
flag = False
if flag:
    # 定义布尔型变量 has_ticket 表示是否有车票
    has_ticket = True
    # 定义整数型变量 knife_length 表示刀的长度，单位：厘米
    knife_length = 20
    # 首先检查是否有车票，如果有，才允许进行安检
    if has_ticket:
        print("有车票，可以开始安检...")
        # 安检时，需要检查刀的长度，判断是否超过 20 厘米
        # 如果超过 20 厘米，提示刀的长度，不允许上车
        if knife_length >= 20:
            print("不允许携带 %d 厘米长的刀上车" % knife_length)
        # 如果不超过20厘米，安检通过
        else:
            print("安检通过，祝您旅途愉快……")
    # 如果没有车票，不允许进门
    else:
        print("大哥，您要先买票啊")


# =========================================  流程控制 - example - 判断元素是否大于10 =========================================
# 判断元素是否大于10
# flag = True
flag = False
if flag:

    def all_numbers_gt_10(numbers):
        # 仅当序列中所有数字大于10时，返回True
        if (
            not numbers
        ):  # 如果numbers为空，因为在这里numbers代表一个列表，[1,2,3...]这种格式，在列表中，空列表[]为False, 这行代码就用来判断numbers是否为空，为空就返回False
            return False
        for n in numbers:  # 通历numbers中的每一个元素
            if n <= 10:
                return False  # 如果有元素小于等于10,该函数马上返回False
        return True  # 如果numbers列表中的所有元素都大于10,那么返回True

    def all_numbers_gt_10_2(numbers):
        return bool(numbers) and all(n > 10 for n in numbers)


# =========================================  使用try/while/for中else分支 =========================================
# flag = True
flag = False
if flag:

    def do_the_first_thing():
        pass

    def do_the_second_thing():
        pass

    def do_stuff():
        first_thing_successed = False
        try:
            do_the_first_thing()  # 做第一件事
            first_thing_successed = True  # 第一件事成功了，把标志位置为True
        except Exception as e:  # 如果上面两行代码（try中的两行代码）有错误，第一件事没有成功，执行下面语句
            print("Error while calling do_some_thing")
            return
        # 仅当first_thing成功完成时，做第二件事
        if first_thing_successed:
            return do_the_second_thing()

    # else改写上述程序当循环使用的迭代对象被正常耗尽、或while循环使用的条件变量变为False后才执行else分支下的代码。
    def do_stuff():
        try:
            do_the_first_thing()
        except Exception as e:
            print("Error while calling do_some_thing")
            return
        else:
            return do_the_second_thing()
