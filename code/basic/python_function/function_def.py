#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : function_def.py
@author     : zgf
@brief      : 函数定义和调用
@attention  : life is short,I need python
"""

# ========================================= 函数 - 调用 - 打印分割线=========================================
# 注意：定义好函数之后，只表示这个函数封装了一段代码而已
# 如果不主动调用函数，函数是不会主动执行的
# 只有在程序中，主动调用函数，才会让函数执行
# flag = True
flag = False
if flag:

    def print_line(char, times):
        """打印单行分隔线
        :param char: 分隔字符
        :param times: 重复次数
        """
        print(char * times)

    def print_lines(char, times):
        """打印多行分隔线
        :param char: 分隔线使用的分隔字符
        :param times: 分隔线重复的次数
        """
        row = 0
        while row < 5:
            print_line(char, times)
            row += 1

    print_lines("-", 20)


# ========================================= 函数 - 调用  - 99乘法表 =========================================
# 函数 - 99乘法表
# flag = True
flag = False
if flag:

    def multiple_table():
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

    multiple_table()


# =========================================  函数 - 阶乘 =========================================
#
# flag = True
flag = False
if flag:

    def factoria(n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    print(factoria(5))
    print(factoria(20))


# ========================================= 函数--函数的嵌套调用 =========================================
#
# flag = True
flag = False
if flag:

    def test1():
        print("*" * 50)

    def test2():
        print("-" * 50)
        # 函数的嵌套调用
        test1()
        print("+" * 50)

    test2()


# ========================================= 函数--函数的递归 =========================================
# 递归函数
# 定义一个函数 sum_numbers
# 能够接收一个 num 的整数参数
# 计算 1 + 2 + ... num 的结果
# flag = True
flag = False
if flag:

    def sum_numbers(num):

        # 1. 出口
        if num == 1:
            return 1

        # 2. 数字的累加 num + (1...num -1)
        # 假设 sum_numbers 能够正确的处理 1...num - 1
        temp = sum_numbers(num - 1)

        # 两个数字的相加
        return num + temp

    result = sum_numbers(100)
    print(result)


# ========================================= 函数练习 =========================================
# 写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
# # 此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
# flag = True
flag = False
if flag:

    def func8(l):
        dic = {}
        for key, value in enumerate(l):
            dic[key] = value
        return dic

    print(func8([1, 2, 3]))


# ========================================= 函数 - 交换数字 =========================================
# flag = True
flag = False
if flag:
    a = 6
    b = 100

    # 解法1：-使用其他变量
    # c = a
    # a = b
    # b = c

    # 解法2：-不使用其他的变量
    # a = a + b
    # b = a - b
    # a = a - b

    # 解法3：-Python 专有
    # a, b = (b, a)
    # 提示：等号右边是一个元组，只是把小括号省略了
    a, b = b, a

    print(a)
    print(b)


# ========================================= 函数 - example =========================================
# 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# flag = True
flag = False
if flag:
    # 方法1
    def func4(l):
        if len(l) > 2:
            l1 = l[:2]
        else:
            l1 = l
        return l1

    # print(func4([1,]))

    # 方法2
    def func4(l):
        return l[:2]


# ========================================= 函数 - example =========================================
# 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# 	dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# 	PS:字典中的value只能是字符串或列表。
# flag = True
flag = False
if flag:
    dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}

    def func1(argv):
        dic = {}
        for i in argv:
            if len(argv[i]) > 2:
                dic[i] = argv[i][0:2]
            else:
                dic[i] = argv[i]
        return dic

    print(func1(dic))

    def func2(argv):
        dic = {}
        for i in argv:
            dic[i] = argv[i][:2]
        return dic

    print(func2(dic))


# ========================================= 函数 - example =========================================
# 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# flag = True
flag = False
if flag:

    def func(l1):
        return l1[1::2]


# ========================================= 函数 - 注册 - example =========================================
# 12，写一个函数完成三次登陆功能：(升级题,两天做完)
# (1)	用户的用户名密码从一个文件register中取出。
# (2)	register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
# (3)	完成三次验证，三次验证不成功则登录失败，登录失败返回False。
# (4)	登陆成功返回True。


# 13，再写一个函数完成注册功能：(升级题,两天做完)
# (1)	用户输入用户名密码注册。
# (2)	注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
# (3)	注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
# (4)	注册成功后，返回True,否则返回False。
# flag = True
flag = False
if flag:

    def register():
        while 1:
            username = input("请输入用户名:").strip()
            with open(
                "register",
                encoding="utf-8",
            ) as f1:
                for line in f1:
                    uname, pwd = line.strip().split("|")  # [诸葛,123]
                    if username == uname:
                        print("此用户名已存在，请重新输入")
                        break
                else:
                    password = input("请输入密码:").strip()
                    with open("register", encoding="utf-8", mode="a") as f2:
                        f2.write("\n{}|{}".format(username, password))
                        return True

    register()
