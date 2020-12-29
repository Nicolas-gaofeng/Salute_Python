#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : data_type_list.py
@author     : zgf
@brief      : 数据类型- list
@attention  : life is short,I need python
"""


# =========================================  组合类型：列表（lsit） =========================================
# 列表是可变类型
# 序列类型：内部元素有位置关系，能通过位置序号访问其中元素
# 列表是一个可以使用多种类型元素，支持元素的增、删、查、改操作的序列类型
# 列表除了直接创建外，另一种产生方式：list(可迭代对象)
# 可迭代对象包括：字符串、元组、集合、range()等
# 列表可以存储大量数据，32位的python限制是536870912个元素，64位python限制是1152921504606846975个元素
# flag = True
flag = False
if flag:

    """*.列表的创建"""
    name = ["zhangsan", "lisi", "wangwu"]
    print(name, type(name))

    ls = ["Python", 1989, True, {"version": 3.7}]
    print(ls, type(ls))
    # 多维列表的创建
    ls = [[0] * 10] * 5
    print(ls)
    ls[0][0] = 1
    print(ls)


# =========================================  组合类型：列表（lsit）- 列表的索引与切片 =========================================
# index()
# 索引
# 切片
# flag = True
flag = False
if flag:
    cars = ["BYD", "BMW", "AUDI", "TOYOTA"]
    """*.列表的索引——与同为序列类型的字符串完全相同"""
    # 正向索引从0开始 反向索引从-1开始
    print(cars[0])

    # 列表中第一次出现待查元素的位置列表.index(待查元素)
    # 使用index方法需要注意，如果传递的数据不在列表中，程序会报错！
    languages = ["Python", "C", "R", "Java"]
    idx = languages.index("R")
    print(idx)

    """列表的切片"""
    # 变量名[开始位置：结束位置：切片间隔]
    # 正向切片
    print(cars[:3])  # 前三个元素，开始位置缺省，默认为0；切片间隔缺省，默认为1
    print(cars[1:4:2])  # 第二个到第四个元素 前后索引差为2
    print(cars[:])  # 获取整个列表，结束位置缺省，默认取值到最后
    print(cars[-4:-2])  # 获取前两个元素
    # 反向切片
    print(cars[:-4:-1])  # 开始位置缺省，默认为-1
    print(cars[::-1])  # 获得反向列表


# =========================================  组合类型：列表（lsit）- 列表的数据统计  =========================================
# len()
# count()
# index()
# flag = True
flag = False
if flag:
    """列表的数据统计"""
    name_list = ["张三", "李四", "王五", "王小二", "张三"]
    # len(length 长度) 函数可以统计列表中元素的总数
    list_len = len(name_list)
    print("列表中包含 %d 个元素" % list_len)

    # count 方法可以统计列表中某一个数据出现的次数
    count = name_list.count("张三")
    print("张三出现了 %d 次" % count)


# =========================================  组合类型：列表（lsit）- 列表的排序 =========================================
# 列表.sort() 直接在列表上进行操作，无返回值
# sorted(列表) 原列表保持不变，返回排序后的列表
# 列表.reverse() 直接在列表上进行操作，无返回值
# flag = True
flag = False
if flag:
    """*.列表的排序"""
    # 使用列表.sort()对列表进行永久排序
    # 直接在列表上进行操作，无返回值
    ls = [2, 5, 2, 8, 19, 3, 7]
    ls.sort()  # 升序
    print(ls)
    # 递减排列
    ls.sort(reverse=True)
    print(ls)
    # 使用sorted(列表)对列表进行临时排序
    # 原列表保持不变，返回排序后的列表
    ls = [2, 5, 2, 8, 19, 3, 7]
    ls_2 = sorted(ls)
    print(ls)
    print(ls_2)
    print(sorted(ls, reverse=True))

    """列表的翻转"""
    # 使用列表.reverse()对列表进行永久翻转
    # 直接在列表上进行操作，无返回值
    ls = [1, 2, 3, 4, 5]
    print(ls[::-1])
    print(ls)
    ls.reverse()
    print(ls)


# =========================================  组合类型：列表（lsit）-增加元素 =========================================
# +
# append()
# insert()
# extend()
# flag = True
flag = False
if flag:
    """*.列表的增加"""
    # 列表的操作符 + 拼接列表
    a = [1, 2]
    b = [3, 4]
    print(a + b)  # 该用法用的不多
    # 用n*list或list*n实现列表的成倍复制
    print([0] * 10)
    # append（）：增加元素 - 在末尾增加元素——列表.append(待增元素)
    languages = ["Python", "C++", "R"]
    languages.append("Java")
    print(languages)
    languages.append(["Ruby", "PHP"])
    print(languages)

    # insert（）： 方法可以在列表的指定索引位置插入数据
    languages.insert(1, "小美眉")

    # extend（）：增加元素 -在末尾整体并入另一列表——列表1.extend(列表2)
    # extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾
    # 增加元素 -extend 将待列表2内的元素逐个添加到列表1中
    languages = ["Python", "C", "C++", "R", "Java"]
    languages.extend(["Ruby", "PHP"])
    print(languages)


# =========================================  赋值运算 - 面试题 =========================================
# 面试题 += 列表
# 列表变量使用 + 不会做相加再赋值的操作 ！ 本质上是在调用列表的 extend 方法
# flag = True
flag = False
if flag:

    def demo(num, num_list):
        print("函数开始")
        # num = num + num
        num += num
        # 列表变量使用 + 不会做相加再赋值的操作 ！
        # num_list = num_list + num_list
        # 本质上是在调用列表的 extend 方法
        num_list += num_list
        # num_list.extend(num_list)
        print(num)
        print(num_list)
        print("函数完成")

    gl_num = 9
    gl_list = [1, 2, 3]
    demo(gl_num, gl_list)
    print(gl_num)
    print(gl_list)


# =========================================  组合类型：列表（lsit）- 转换 =========================================
# list()
# flag = True
flag = False
if flag:
    """*.列表的转换"""
    # 字符串转列表
    print(list("人工智能是未来的趋势"))
    # 元组转列表
    print(list(("我", "们", "很", "像")))
    # 集合转列表
    print(list({"李雷", "韩梅梅", "Jim", "Green"}))


# =========================================  组合类型：列表（lsit）- 修改 =========================================
# 通过"先索引后赋值"的方式，对元素进行修改列表名[位置]=新值
# 列表指定的索引超出范围，程序会报错！
# flag = True
flag = False
if flag:
    languages = ["Python", "C", "R", "Java"]
    languages[1] = "C++"
    print(languages)


# =========================================  组合类型：列表--操作：删除 =========================================
# 列表的删除
# pop()
# remove()
# clear()
# del
# flag = True
flag = False
if flag:
    """pop()"""
    print("pop()".center(50, "*"))
    #  pop() :删除列表i位置的元素 列表.pop(位置)
    languages = ["Python", "C", "C++", "R", "Java"]
    languages.pop(1)
    print(languages)
    # 不写位置信息，默认删除最后一个元素 .pop()有返回值
    languages.pop()
    print(languages)

    """remove()"""
    print("remove()".center(50, "*"))
    # remove(): 删除 - 删除列表中的第一次出现的待删元素，如果数据不存在，程序会报错
    languages = ["Python", "C", "R", "C", "Java"]
    languages.remove("C")
    print(languages)  # ['Python', 'R', 'C', 'Java']

    """clear()"""
    print("clear()".center(50, "*"))
    # clear(): 删除 - clear 方法可以清空列表
    languages = ["Python", "C", "R", "C", "Java"]
    languages.clear()
    print(languages)

    """ del 关键字"""
    # 使用 del 关键字(delete)删除列表元素
    # 提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法
    print("del".center(50, "*"))
    name_list = ["张三", "李四", "王五"]
    del name_list[0:1]  # 按照切片删除
    print(name_list)
    del name_list[1]
    # del 关键字本质上是用来将一个变量从内存中删除的
    name = "小明"
    # del name
    # 注意：如果使用 del 关键字将变量从内存中删除
    # 后续的代码就不能再使用这个变量了
    print(name)
    print(name_list)

    """ 删除列表内的特定元素 - 存在删除法 """
    # 方法1 存在运算删除法
    # 缺点：每次存在运算，都要从头对列表进行遍历、查找、效率低
    alist = ["d", "d", "d", "2", "2", "d", "d", "4"]
    s = "d"
    while True:
        if s in alist:
            alist.remove(s)
        else:
            break
    print(alist)

    """ 删除列表内的特定元素 - 一次性遍历元素执行删除 """
    alist = ["d", "d", "d", "2", "2", "d", "d", "4"]
    for s in alist:
        if s == "d":
            alist.remove(s)  # remove（s） 删除列表中第一次出现的该元素
    #         删除第一个之后for循环还是记录的第二个 ，但是列表已经发生变化
    print(alist)  # ['2', '2', 'd', 'd', '4']

    # 解决方法：使用负向索引
    alist = ["d", "d", "d", "2", "2", "d", "d", "4"]
    for i in range(-len(alist), 0):
        if alist[i] == "d":
            alist.remove(alist[i])  # remove（s） 删除列表中第一次出现的该元素
    print(alist)


# =========================================  列表推导式 =========================================
# 列表推导式：一行代码几乎搞定你需要的任何的列表。
# [expression for value in iterable if conditihon]
# 三要素：表达式、可迭代对象、if条件（可选）
# 列表推导式
# 优点：一行解决，方便。
# 缺点：容易着迷，不易排错，不能超过三次循环。
# 列表推导式不能解决所有列表的问题，所以不要太刻意用。
# """
# 执行过程
#
# （1）从可迭代对象中拿出一个元素
#
# （2）通过if条件（如果有的话），对元素进行筛选
#
#  若通过筛选：则把元素传递给表达式
#
#  若未通过：  则进入（1）步骤，进入下一次迭代
# （3）将传递给表达式的元素，代入表达式进行处理，产生一个结果
#
# （4）将（3）步产生的结果作为列表的一个元素进行存储
#
# （5）重复（1）~（4）步，直至迭代对象迭代结束，返回新创建的列表
# """
# flag = True
flag = False
if flag:

    l1 = []
    for num in range(1, 101):
        l1.append(num)
    print(l1)

    # 循环模式  [变量（加工后的变量） for 变量 in iterable]
    l = [i for i in range(1, 101)]
    print(l)
    print([i * i for i in range(1, 11)])
    l2 = ["python%s期" % i for i in range(1, 16)]
    print(l2)
    # 支持循环嵌套
    colors = ["black", "white"]
    sizes = ["S", "M", "L"]
    tshirts = ["{} {}".format(color, size) for color in colors for size in sizes]
    print(tshirts)
    # 支持多变量
    x = [1, 2, 3]
    y = [1, 2, 3]
    results = [i * j for i, j in zip(x, y)]
    print(results)
    # 筛选模式 [变量（加工后的变量） for 变量 in iterable if 条件]
    l3 = [i for i in range(1, 31) if i % 2 == 0]
    print(l3)
    print([i for i in range(1, 31) if i % 3 == 0])
    print([i ** 2 for i in range(1, 31) if i % 3 == 0])
    names = [
        ["Tom", "Billy", "Jefferson", "Andrew", "Wesley", "Steven", "Joe"],
        ["Alice", "Jill", "Ana", "Wendy", "Jennifer", "Sherry", "Eva"],
    ]
    print([j for i in names for j in i if j.count("e") == 2])

    # 解析语法构造字典（字典推导）
    mcase = {"a": 10, "b": 34}
    mcase_frequency = {mcase[k]: k for k in mcase}
    print(mcase_frequency)

    squares = {i: i ** 2 for i in range(10)}
    for k, v in squares.items():
        print(k, ":  ", v)

    squared = {x ** 2 for x in [1, -1, 2]}
    print(squared)

    # 生成器表达式：将列表推导式的 []  换成() 即可。
    # g = (i for i in range(100000000000))
    # print(g)
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())
    squares = (i ** 2 for i in range(10))
    print(squares)

    # 条件表达式
    # expr1 if condition else expr2
    # 将变量n的绝对值赋值给变量x
    n = -10
    if n >= 0:
        x = n
    else:
        x = -n
    print(x)

    n = -10
    x = n if n >= 0 else -n
    print(x)


# =========================================  数据的复制 - 深浅拷贝 =========================================
# 列表的复制 深浅拷贝
# 列表内的元素可以分散的存储在内存中
# 列表存储的，实际上是这些元素的地址！！！——地址的存储在内存中是连续的
# deepcopy()
# 完全独立的copy一份数据，与原数据没有关系，深copy
# flag = True
flag = False
if flag:
    print("浅拷贝".center(50, "*"))
    # 浅拷贝之后
    # 针对不可变元素（数字、字符串、元组）的操作，都各自生效了
    # 针对不可变元素（列表、集合）的操作，发生了一些混淆
    # 方法1：列表.copy()
    languages = ["Python", "C", "R", "Java"]
    languages_2 = languages.copy()
    languages.pop()
    print(languages)
    print(languages_2)
    # 方法2：列表[:]
    languages = ["Python", "C", "R", "Java"]
    languages_3 = languages[:]
    languages.pop()
    print(languages)
    print(languages_3)

    l1 = [1, 2, 3]
    l2 = l1.copy()
    l1.append(666)
    print(l1, l2)
    # 对于浅拷贝来说，第一层在内存中是独立的，从第二层开始以及更深的层数，都是使用的一个内存地址，一变都变
    l1 = [
        1,
        2,
        3,
        [
            22,
        ],
    ]
    l2 = l1.copy()
    # l1.append(666)
    # print(l1,l2)
    l1[-1].append("taibai")
    # print(l1,l2)
    print(id(l1))
    print(id(l2))
    print(id(l1[-1]))
    print(id(l2[-1]))

    print("深拷贝".center(50, "*"))
    # 深拷贝将所有层级的相关元素全部复制，完全分开，泾渭分明，避免了上述问题
    import copy

    l1 = [
        1,
        2,
        3,
        [
            22,
            33,
        ],
    ]
    l2 = copy.deepcopy(l1)
    print(l1, l2, id(l1), id(l2))
    l1.append(666)
    l1[-2].append("太白")
    print(l1, type(l1))
    print(l2)

    # 应用场景：面试会考，解释深浅copy
    # 如果一份数据（列表）第二层时，你想与原数据进行公用，浅copy。
    #  面试题
    # 切片属于浅copy
    l1 = [1, 2, 3, [22, 33]]
    l2 = l1[:]
    # l1.append(666)
    l1[-1].append(666)
    print(l2)
