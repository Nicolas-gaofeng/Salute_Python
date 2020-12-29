#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : conditional_branching_structure.py
@author     : zgf
@brief      : 条件分支结构
@attention  : life is short,I need python
"""


# =========================================  if 语句 - 判断年龄 =========================================
# if 语句以及缩进部分的代码是一个完整的代码块
# 1. 定义一个整数变量记录年龄
# 2. 判断是否满 18 岁 （**>=**）
# 3. 如果满 18 岁，允许进网吧嗨皮
# flag = True
flag = False
if flag:
    # 1. 定义年龄变量
    age = 18
    # 2. 判断是否满 18 岁
    if age >= 18:
        print("可以进网吧嗨皮……")
    # 3. 思考！ 无论条件是否满足都会执行
    print("这句代码什么时候执行?")


# =========================================  if else分支语句 =========================================
# 不管多少分支，最后只执行一个分支
# 尽可能减少多层嵌套
# 避免死循环
# flag = True
flag = False
if flag:
    height = 183
    weight = 75
    vision = 5.0
    if height == 183 and weight == 70 and vision > 5.0:
        print("可以做飞行员")
    else:
        print("不可以")


# =========================================  逻辑运算 =========================================
# not
# or
# and
# flag = True
flag = False
if flag:
    print("and".center(50, "*"))
    # 定义一个整数变量age，编写代码判断年龄是否正确 要求人的年龄在 0-120 之间
    age = 100
    if age >= 0 and age <= 120:
        print("年龄正确")
    else:
        print("年龄不正确")

    print("or".center(50, "*"))
    # 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩 要求只要有一门成绩 > 60 分就算合格
    python_score = 50
    c_score = 50
    if python_score > 60 or c_score > 60:
        print("考试通过")
    else:
        print("再接再厉！")

    print("not".center(50, "*"))
    # 练习3: 定义一个布尔型变量 is_employee，编写代码判断是否是本公司员工 如果不是提示不允许入内
    is_employee = True
    # 如果不是提示不允许入内
    if not is_employee:
        print("非公勿内")


# =========================================  if循环嵌套 =========================================
# 不管多少分支，最后只执行一个分支
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

# =========================================  if elif else =========================================
#
# flag = True
flag = False
if flag:
    score = int(input("请输入成绩："))
    if score > 90:
        print("well")
    elif score >= 80:
        print("good")
    elif score >= 70:
        print("little")
    else:
        print("bad")


# =========================================  石头剪刀布 =========================================
# 1. 从控制台输入要出的拳     —— 石头（1）／剪刀（2）／布（3）
# 2. 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
# 3. 比较胜负
# flag = True
flag = False
if flag:
    if (
        (player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)
    ):
        print("噢耶！！！电脑弱爆了！！！")
    elif player == computer:
        print("心有灵犀，再来一盘！")
    else:
        print("不行，我要和你决战到天亮！")
