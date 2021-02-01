#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : Loop_structure_for.py
@author     : zgf
@brief      : 循环结构 - for
@attention  : life is short,I need python
"""


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


# =========================================  for循环-list遍历 =========================================
# li = [ 1 , 3 , 4 , " alex " , [ 3 , 7 , 8 , " TaiBal " ] , 5 , " RiTiAn " ]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
# flag = True
flag = False
if flag:
    li = [1, 3, 4, " alex ", [3, 7, 8, " TaiBal "], 5, " RiTiAn "]
    for i in li:
        if type(i) == list:
            for j in i:
                print(j)
        else:
            print(i)


# =========================================  for循环-list遍历 =========================================
# 开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# #敏感词列表1i=[”苍老师”，”东京热”，“武藤兰”，“波多野结衣”
# #则将用户输入的内容中的敏感词汇替换成等长度的*(苍老师就替换***),并添加到一个列表中；
# #如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# flag = True
flag = False
if flag:
    li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
    con_list = []
    while True:
        comment = input("请输入评论：").strip()
        if comment.upper() == "Q":
            break
        for i in li:
            if i in comment:
                comment = comment.replace(i, "*" * len(i))
        con_list.append(comment)
    print(con_list)


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


# =========================================  for循环 - 计算用户输入的内容中有几个整数 =========================================
# flag = True
flag = False
if flag:
    content = input("请输入内容:").strip()
    count = 0
    for i in content:
        if i.isdigit():
            count += 1
    print(count)


# =========================================  for循环 - for + else =========================================
# 要判断某一个字典中是否存在指定的值
# - 如果存在，提示并且退出循环
# - 如果不存在，在循环整体结束后，希望得到一个统一的提示
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

    print("查找名片example".center(50, "*"))
    students = [
        {"name": "阿土", "age": 20, "gender": True, "height": 1.7, "weight": 75.0},
        {"name": "小美", "age": 19, "gender": False, "height": 1.6, "weight": 45.0},
    ]
    find_name = "阿土"
    for stu_dict in students:
        # 判断当前遍历的字典中姓名是否为find_name
        if stu_dict["name"] == find_name:
            print("找到了")
            # 如果已经找到，直接退出循环，就不需要再对后续的数据进行比较
            break
    else:
        print("没有找到")
    print("循环结束")


# ========================================= range()对象 =========================================
#
# flag = True
flag = False
if flag:
    res = []
    for i in range(10000):
        res.append(i ** 2)
    print(res[:5])
    print(res[-1])

    res = []
    for i in range(1, 10, 2):
        res.append(i ** 2)
    print(res)

    # range(起始数字,中止数字,数字间隔)
    for i in [0, 1, 2, 3, 4, 5]:
        print(i)
    # range(起始数字,中止数字,数字间隔) 如果起始数字缺省，默认为0 必须包含中止数字 数字间隔缺省，默认为1
    for i in range(6):
        print(i)
    for i in range(1, 11, 2):
        print(i)
    # range()转列表
    print(list(range(1, 11, 2)))