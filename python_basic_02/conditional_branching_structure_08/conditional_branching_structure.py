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
    # 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确
    age = 12
    # 要求人的年龄在 0-120 之间
    """
    10000
    age >= 0 or age <= 120
    age >= 0 and age <= 120
    """
    if age >= 0 and age <= 120:
        print("年龄正确")
    else:
        print("年龄不正确")
    # 输入用户年龄
    age = int(input("请输入年龄："))
    # 判断是否满 18 岁 （>=）
    if age >= 18:
        # 如果满 18 岁，允许进网吧嗨皮
        print("你已经成年，欢迎来网吧嗨皮")
    else:
        # 如果未满 18 岁，提示回家写作业
        print("你还没有成年，请回家写作业吧")
    # 这句代码无论条件是否成立都会执行！
    print("这句代码什么时候执行？")


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


# =========================================   流程控制 - if - elif =========================================
#  写一个根据当日日期来说明是否上班的程序，请用户输入日期来获取
#     如果:今天是Monday,那么:上班
#     如果:今天是Tuesday,那么:上班
#     如果:今天是Wednesday,那么:上班
#     如果:今天是Thursday,那么:上班
#     如果:今天是Friday,那么:上班
#     如果:今天是Saturday,那么:出去浪
#     如果:今天是Sunday,那么:出去浪
# flag = True
flag = False
if flag:
    # 方式一：
    today = input(">>: ")
    if today == "Monday":
        print("上班")
    elif today == "Tuesday":
        print("上班")
    elif today == "Wednesday":
        print("上班")
    elif today == "Thursday":
        print("上班")
    elif today == "Friday":
        print("上班")
    elif today == "Saturday":
        print("出去浪")
    elif today == "Sunday":
        print("出去浪")
    else:
        print(
            """必须输入其中一种:
        Monday
        Tuesday
        Wednesday
        Thursday
        Friday
        Saturday
        Sunday
        """
        )
    # 方式二：
    today = input(">>: ")
    if today == "Saturday" or today == "Sunday":
        print("出去浪")
    elif (
        today == "Monday"
        or today == "Tuesday"
        or today == "Wednesday"
        or today == "Thursday"
        or today == "Friday"
    ):
        print("上班")
    else:
        print(
            """必须输入其中一种:
        Monday
        Tuesday
        Wednesday
        Thursday
        Friday
        Saturday
        Sunday
        """
        )
    # 方式三：
    today = input(">>: ")
    if today in ["Saturday", "Sunday"]:
        print("出去浪")
    elif today in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        print("上班")
    else:
        print(
            """必须输入其中一种:
        Monday
        Tuesday
        Wednesday
        Thursday
        Friday
        Saturday
        Sunday
        """
        )


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


# =========================================  石头剪刀布 =========================================
# 1. 从控制台输入要出的拳     —— 石头（1）／剪刀（2）／布（3）
# 2. 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
# 3. 比较胜负
# flag = True
flag = False
if flag:
    # 导入随机工具包
    # 注意：在导入工具包的时候，应该将导入的语句，放在文件的顶部
    # 因为，这样可以方便下方的代码，在任何需要的时候，使用工具包中的工具
    import random

    # 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
    player = int(input("请输入您要出的拳 石头（1）／剪刀（2）／布（3）："))
    # 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
    computer = random.randint(1, 3)
    print("玩家选择的拳头是 %d - 电脑出的拳是 %d" % (player, computer))
    # 比较胜负
    # 1	石头 胜 剪刀
    # 2	剪刀 胜 布
    # 3	布 胜 石头
    # if (()
    #        or ()
    #        or ()):
    if (
        (player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)
    ):
        print("欧耶，电脑弱爆了！")
    # 平局
    elif player == computer:
        print("真是心有灵犀啊，再来一盘")
    # 其他的情况就是电脑获胜
    else:
        print("不服气，我们决战到天明！")
