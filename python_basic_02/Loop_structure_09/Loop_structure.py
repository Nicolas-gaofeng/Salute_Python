#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : Loop_structure.py
@author     : zgf
@brief      : 循环结构
@attention  : life is short,I need python
"""


# ========================================= while循环 - 程序计数 =========================================
# 打印 5 遍 Hello Python
# 注意：循环结束后，之前定义的计数器条件的数值是依旧存在的
# flag = True
flag = False
if flag:
    # 1. 定义一个整数变量，记录循环次数
    i = 1
    # 2. 开始循环
    while i <= 3:
        # 1> 希望在循环内执行的代码
        print("Hello Python")
        # 2> 处理计数器
        # i = i + 1
        i += 1
    # 3. 观察一下，循环结束后，计数器 i 的数值是多少
    print("循环结束后，i = %d" % i)


# ========================================= while循环 - 循环输出 =========================================
# 使用while循环输出1 2 3 4 5 6     8 9 10
# flag = True
flag = False
if flag:
    print("方式一".center(50, "*"))
    count = 1
    while count <= 10:
        if count == 7:
            count += 1
            continue
        print(count)
        count += 1

    print("方式二".center(50, "*"))
    count = 1
    while count <= 10:
        if count != 7:
            print(count)
        count += 1

    print("方式三".center(50, "*"))
    for i in range(1, 11):
        if i == 7:
            continue
        print(i)


# ========================================= while循环 - 循环计算 =========================================
# flag = True
flag = False
if flag:
    # 计算 0 ~ 100 之间所有数字的累计求和结果
    # 0. 定义最终结果的变量
    result = 0
    # 1. 定义一个整数的变量记录循环的次数
    i = 0
    # 2. 开始循环
    while i <= 100:
        print(i)
        # 每一次循环，都让 result 这个变量和 i 这个计数器相加
        result += i
        # 处理计数器
        i += 1
    print("0~100之间的数字求和结果 = %d" % result)


# ========================================= while循环 - 偶数求和 =========================================
# flag = True
flag = False
if flag:
    # 计算 0 ~ 100 之间 所有 偶数 的累计求和结果
    # 开发步骤
    # 1. 编写循环 确认 要计算的数字
    # 2. 添加 结果 变量，在循环内部 处理计算结果
    # 1> 定义一个记录最终结果的变量
    result = 0
    i = 0
    while i <= 100:
        # 判断变量 i 中的数值，是否是一个偶数
        # 偶数 i % 2 == 0
        # 奇数 i % 2 != 0
        if i % 2 == 0:
            print(i)
            # 2> 当 i 这个变量是偶数时，才进行累加操作！
            result += i
        # result += i
        i += 1
    print("0~100之间的偶数累加结果 = %d" % result)


# ========================================= while循环 - 奇数求和 =========================================
# flag = True
flag = False
if flag:
    # 计算 0 ~ 100 之间 所有 奇数 的累计求和结果
    # 开发步骤
    # 1. 编写循环 确认 要计算的数字
    # 2. 添加 结果 变量，在循环内部 处理计算结果
    # 1> 定义一个记录最终结果的变量
    result = 0
    i = 0
    while i <= 100:
        # 判断变量 i 中的数值，是否是一个偶数
        # 偶数 i % 2 == 0
        # 奇数 i % 2 != 0
        if i % 2 != 0:
            print(i)
            # 2> 当 i 这个变量是偶数时，才进行累加操作！
            result += i
        # result += i
        i += 1
    print("0~100之间的奇数累加结果 = %d" % result)


# ========================================= while循环 - 循环计算 =========================================
# 计算1-2+3-4...+99中除了88以外的所有数的和
# flag = True
flag = False
if flag:
    count = 1
    sum = 0
    while count < 100:
        if count == 88:
            count += 1
        if count % 2 == 0:
            sum -= count
        else:
            sum += count
        count += 1
    print(count)


# =========================================  while循环-猜测年龄 =========================================
# while 条件：
# 循环体
# 如果条件为真，那么循环体则执行，执行完毕后再次循环，重新判断条件。
# 如果条件为假，那么循环体不执行，循环终止
# flag = True
flag = False
if flag:
    age = 18
    while True:
        guess_age = int(input("请输入猜测的年龄："))
        if guess_age > age:
            print("猜大了")
        elif guess_age < age:
            print("猜小了")
        else:
            print("猜对了")
            break


# =========================================  while循环 - 风向标flag=========================================
#
# flag = True
flag = False
if flag:
    albert_age = 18
    flag = True  # 布尔类型
    while flag:
        guess = int(input(">>:"))
        if guess > albert_age:
            print("猜的太大了，往小里试试...")
        elif guess < albert_age:
            print("猜的太小了，往大里试试...")
        else:
            print("恭喜你，猜对了...")
            flag = False  # 当诉求得到满足，就让风向变一下

    # 例子
    """***多层循环使用tag快速跳出循环***"""
    tag = True
    while tag:
        print("111")
        while tag:
            print("22")
            while tag:
                tag = False


# =========================================  while循环 - 死循环 =========================================
#
# flag = True
flag = False
if flag:
    """while死循环"""
    import time

    num = 0
    while True:
        print("count", num)
        time.sleep(1)
        num += 1
    # 死循环
    while True:
        print("天地之渺渺，时间之无限")


# =========================================  while循环 - while + else =========================================
# 如果while循环正常执行，则会执行else函数，如果被break，则不会执行
# flag = True
flag = False
if flag:
    count = 0
    while count <= 5:
        count += 1
        print("Loop", count)
    else:
        print("循环正常执行完啦")
    print("-----out of while loop-------")

    count = 0
    while count <= 5:
        count += 1
        if count == 3:
            break
        print("Loop", count)
    else:
        print("循环正常执行完啦")
    print("-----out of while loop-------")


# =========================================   while循环 -打印小星星 =========================================
# 在控制台连续输出五行 *，每一行星号的数量依次递增
# *
# **
# ***
# ****
# *****
# 1. 定义一个计数器变量，从数字1开始，循环会比较方便
# flag = True
flag = False
if flag:
    row = 1
    # 2. 开始循环
    while row <= 5:
        print("*" * row)
        row += 1


# =========================================   while循环 -嵌套打印小星星 =========================================
# 需求
#
# 在控制台连续输出五行 *，每一行星号的数量依次递增
# *
# **
# ***
# ****
# *****
# 开发步骤
# 1> 完成 5 行内容的简单输出
# 2> 分析每行内部的 * 应该如何处理？
# flag = True
flag = False
if flag:
    row = 1
    while row <= 5:
        # 每一行要打印的星星就是和当前的行数是一致的
        # 增加一个小的循环，专门负责当前行中，每一 `列` 的星星显示
        # 1. 定义一个列计数器变量
        col = 1
        # 2. 开始循环
        """
        1   1
        2   2
        3   3
        4   4
        5   5
        """
        while col <= row:
            # print("%d" % col)
            print("*", end="")
            col += 1
        # print("第 %d 行" % row)
        # 这行代码的目的，就是在一行星星输出完成之后，添加换行！
        print("")
        row += 1


# =========================================  while循环 - 九九乘法表 =========================================
# flag = True
flag = False
if flag:
    # 1. 打印 9 行小星星
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # print("*", end="")
            print("%d * %d = %d" % (col, row, col * row), end="\t")
            col += 1
        # print("%d" % row)
        print("")
        row += 1


# =========================================  while循环 - example =========================================
# 将未读书籍列表中书名分别输出后，存入已读书籍列表
# flag = True
flag = False
if flag:
    not_read = ["红楼梦", "水浒传", "三国演义", "西游记"]
    have_read = []
    while not_read:  # not_read非空，循环继续，否则中止
        book = not_read.pop()
        have_read.append(book)
        print("我已经读过《{}》了".format(book))
    print(not_read)
    print(have_read)


# =========================================  for循环 - 迭代遍历 =========================================
# Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
# flag = True
flag = False
if flag:
    goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998},
    ]
    print("商品具体展示".center(50, "*"))
    for index, i in enumerate(goods):
        print("{}\t{}\t{}".format(index, i["name"], i["price"]))
    print("*" * 50)

    print("items()".center(50, "*"))
    dir = {1: "kobe", 2: "LBJ", 3: "CP3", 4: "TDK"}
    print(dir.items())
    for key, value in dir.items():
        print(key, value)
    else:
        print("ending")


# =========================================  for循环 - range遍历数组 =========================================
#
# flag = True
flag = False
if flag:
    for i in range(10):
        print(i)
    l1 = ["alex", "alex", "taibai", "egon", "景女神", "文周老师", "日天"]
    for i in range(0, len(l1)):
        print(i, l1[i])


# =========================================  for循环 - 计算0-9的和 =========================================
#
# flag = True
flag = False
if flag:
    sum = 0
    for i in range(10):
        sum += i
    print(sum)


# =========================================  for循环 - for + else =========================================
# 如果for 循环全部执行完毕，没有被break中止，则运行else块
# flag = True
flag = False
if flag:
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in L:
        print(i)
    else:
        print("ending")
    # 程序例子
    product_scores = [89, 90, 99, 70, 67, 78, 85, 92, 77, 82]  # 1组10个产品的性能评分
    # 如果低于75分的超过1个，则该组产品不合格
    i = 0
    for score in product_scores:
        if score < 75:
            i += 1
        if i == 2:
            print("产品抽检不合格")
            break
    else:
        print("产品抽检合格")


# ========================================= break =========================================
# break用于退出本层循环
# flag = True
flag = False
if flag:
    i = 0
    while i < 10:
        # break 某一条件满足时，退出循环，不再执行后续重复的代码
        # i == 3
        if i == 3:
            break
        print(i)
        i += 1
    print("over")


# ========================================= continue =========================================
# 结束本次循环
# continue用于退出本次循环，继续下一次循环
# flag = True
flag = False
if flag:
    i = 0
    while i < 10:
        # continue 某一条件满足时，不执行后续重复的代码
        # i == 3
        if i == 3:
            # 注意：在循环中，如果使用 continue 这个关键字
            # 在使用关键字之前，需要确认循环的计数是否修改，
            # 否则可能会导致死循环
            i += 1
            continue
        print(i)
        i += 1
    # 程序练习
    product_scores = [89, 90, 99, 70, 67, 78, 85, 92, 77, 82]  # 1组10个产品的性能评分
    # 如果低于75分,输出警示
    print(len(product_scores))
    for i in range(len(product_scores)):
        if product_scores[i] >= 75:
            continue
        print("第{0}个产品，分数为{1}，不合格".format(i, product_scores[i]))
