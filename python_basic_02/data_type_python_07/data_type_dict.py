#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : data_type_dict.py
@author     : zgf
@brief      : 数据类型- dict
@attention  : life is short,I need python
"""


# =========================================  数据类型 =========================================
# 在 Python 中定义变量是 不需要指定类型（在其他很多高级语言中都需要）
# 数据类型可以分为 数字型 和 非数字型
# 数字型： 整型 (int) 浮点型（float） 布尔型（bool）真 True 非 0 数 —— 非零即真 假 False 0 复数型 (complex)
# 主要用于科学计算，例如：平面场问题、波动问题、电感电容等问题
# 非数字型 -字符串 -列表 -元组 -字典
# flag = True
flag = False
if flag:
    pass


# =========================================  1.数字类型 - 字节（bytes） =========================================
# python的基础数据类型之一，他和str相当于双胞胎，str拥有的所有方法，bytes类型都适用
# 内部编码方式：非unicode
# 你想将一部分内容（字符串）写入文件，或者通过网络socket传输，这样这部分内容（字符串）必须转化成bytes才可以进行
# 平时你代码中，使用字符串。
# flag = True
flag = False
if flag:
    i = b"alex"
    print(i, type(i))  # 查询十进制转化成二进制占用的最小位数

# =========================================  1.数字类型 - 整型（int） =========================================
# 整型是不可变类型
# 数据类型之间的转化。 int ---> str str (int) int(str) - int----bool:非零及True,零即为False,True--->1 False--->0
# flag = True
flag = False
if flag:
    age = 18
    print(age, type(age))
    print(16 == 0b10000 == 0o20 == 0x10)  # 默认输入十进制 二进制0b、八进制0o、十六进制0x
    # 十进制与其他进制的转换
    a = bin(16)  # 转二进制 注意：上述转换后结果为字符串类型
    b = oct(16)  # 转八进制 注意：上述转换后结果为字符串类型
    c = hex(16)  # 转十六进制 注意：上述转换后结果为字符串类型
    print(
        a,
        b,
        c,
        type(a),
        type(b),
        type(c),
    )  # 0b10000 0o20 0x10
    print(a == b == c)  # False
    # 其他进制转换十进制
    d = int(a, 2)  # 二进制转十进制
    e = int(b, 8)  # 八进制转十进制
    f = int(c, 16)  # 十六进制转十进制
    print(d, e, f)  # 16 16 16

    i = 4
    print(i.bit_length())  # 查询十进制转化成二进制占用的最小位数


# =========================================  1.数字类型 - 浮点型（float） =========================================
# 浮点型是不可变类型
# 计算机采用二进制小数来表示浮点数的小数部分
# 部分小数不能用二进制小数完全表示,通常情况下不会影响计算精度
# flag = True
flag = False
if flag:
    height = 1.83
    print(height, type(height))
    # 不确定小数问题
    print((0.1 + 0.2) == 0.3)  # False
    print(0.1 + 0.2)  # 0.30000000000000004
    print(0.1 + 0.7)  # 0.7999999999999999
    a = 3 * 0.1
    print(a)
    b = round(a, 1)
    print(b, b == 0.3)


# =========================================  1.数字类型 - 复数（complex）a+bj =========================================
# 浮点型是不可变类型
# 大写J或小写j均可
# 虚部系数为1时，需要显式写出
# 3是实部，4是虚部
# flag = True
flag = False
if flag:
    a = 3 + 4j
    print(a, type(a))
    print(3 + 4j, 2 + 5j, type(3 + 4j), type(2 + 5j))
    print(2 + 1j)  # 虚部系数为1时，需要显式写出


# =========================================  2.字符串 =========================================
# 单引号‘’ 双引号“” 三引号‘’‘ ’‘’
# 内部编码方式 Unicode
# 通过紧凑数组实现字符串的存储
# 数据在内存中是连续存放的，效率更高，节省空间
# flag = True
flag = False
if flag:
    """*.字符串的创建"""
    name = "xiaoming"
    name2 = "xiaoming"
    name3 = """xiao
    ming"""  # 字符串为多行时可以用三引号
    print(name, type(name))
    print(name2, type(name2))
    print(name3, type(name3))
    print("I'm 18 years old")  # 双中有单
    print('"Python" is good')  # 单中有双
    # print(""Python" is good")
    print('"Python" is good')  # 双中有双，单中有单——转义符 \
    s = "py" "thon"
    print(s)  # 转义符可以用来换行继续输入

    """*.字符串的拼接"""
    a = "I love "
    b = "my wife "
    print(a + b)
    # 字符串的成倍复制： 字符串 * n  n * 字符串
    c = a + b
    print(c * 3)
    print(3 * c)

    """*.字符串取值"""
    # 按索引取值，取出来的是一个新的字符串
    # 字符串的索引 格式：变量名[位置编号]
    # 正向索引——从零开始递增
    # 位置编号不能超过字符串的长度
    s = "My name is Peppa Pig"
    print(s[0])
    print(s[2])
    print(s[5])
    # 反向索引——从-1开始递减
    print(s[-1])
    print(s[-3])
    print(s[-5])
    # 字符串的遍历
    for char in s:
        print(char)

    # 按切片取值
    # 字符串的切片 变量名[开始位置：结束位置：切片间隔]
    # 切片间隔如不设置默认为1，可省略 切片范围不包含结束位置(顾头不顾尾)
    # 起始位置是0 可以省略
    # 结束位置省略，代表可以取到最后一个字符
    # 可以使用反向索引
    s = "Python"
    print(s[0:3:1])  # Pyt
    print(s[0:3])  # Pyt
    print(s[0:3:2])  # Pt
    print(s[0:6])  # Python
    print(s[:6])  # Python
    print(s[:])  # Python
    print(s[-6:])  # Python
    # 反向切片 ： 起始位置是 - 1 也可以省略
    # 结束位置省略，代表可以取到第一个字符
    s = "123456789"
    print(s[-1:-10:-1])  # 987654321
    print(s[:-10:-1])  # 987654321
    print(s[::-1])  # 987654321

    """*.成员运算 ：子集in全集  任何一个连续的切片都是原字符串的子集"""
    folk_singers = "Peter, Paul and Mary"
    print("Peter" in folk_singers)
    print("PPM" in folk_singers)

    """*. 查找指定字符串"""
    # index同样可以查找指定的字符串在大字符串中的索引
    print(hello_str.index("llo"))
    # 注意：如果使用index方法传递的子字符串不存在，程序会报错！
    # print(hello_str.index("abc"))
    print(hello_str.find("llo"))
    # find如果指定的字符串不存在，会返回-1
    print(hello_str.find("abc"))
    print(hello_str.find("lo", 1, -1))  # 返回整体的索引，搜索的切片

    # 判断是否以指定字符串开始
    hello_str = "hello world"
    print(hello_str.startswith("Hello"))
    print(hello_str.startswith("llo", 3, 5))  # 判断其中一部分
    # 判断是否以指定字符串结束
    print(hello_str.endswith("world"))
    """*.字符串统计字符"""
    hello_str = "hello hello"
    # 1. 统计字符串长度
    print(len(hello_str))  # 所含字符的个数
    # 2. 字符串统计——字符串.count("待统计字符串") 统计某一个小（子）字符串出现的次数
    print(hello_str.count("llo"))
    s = "Python is an excellent language"
    print("an:", s.count("an"))
    print("e:", s.count("e"))
    # print(hello_str.count("abc"))

    """*. 字符串的分割"""
    # 4. 字符串.split(分割字符)：返回一个列表 原字符串不变
    languages = "Python C C++ Java PHP R"
    # 默认按照空格分隔
    languages_list = languages.split(" ")
    print(languages_list)
    print(languages)
    s = "aleclwle"
    print(s.split("l", 1))  # 分隔一次 1代表分隔次数
    print(s.rsplit("l"))  # 从右至左分隔

    """*.字符串的聚合"""
    # “聚合字符”.join(可迭代数据类型)：可迭代类型 如：字符串、列表
    s = "12345"
    s_join = ",".join(s)
    print(s_join)  # 1,2,3,4,5
    #     序列类型的元素必须是字符类型
    # s = [1, 2, 3, 4, 5]
    s = ["1", "2", "3", "4", "5"]
    print("*".join(s))  # 1*2*3*4*5

    """*.字符串去除空格"""
    # 删除两端特定字符——字符串.strip(删除字符)
    # strip从两侧开始搜索，遇到指定字符执行删除，遇到非指定字符，搜索停止
    # 类似的还有左删除lstrip和右删除rstrip
    s = "      I have many blanks     "
    print(s.strip(" "))  # 还有吗？hahaha
    print(s.lstrip(" "))
    print(s.rstrip(" "))
    print(s)
    name = "*alex**"
    print(name.strip("*"))
    name2 = "weralexqwe"
    print(name2.strip("erw"))  # 前后同时进行去除，有就去掉

    """*.字符串的替换"""
    # 字符串.replace("被替换"，"替换成")
    # replace方法执行完成之后，会返回一个新的字符串
    #   注意：不会修改原有字符串的内容
    s = "Python is coming"
    s1 = s.replace("Python", "Py")
    print(s1)
    s2 = s.replace("i", "I", 2)  # 2代表可以设置次数
    print(s2)

    # 8.  字符串.upper() 字母全部大写
    s = "hello python"
    print(s.upper())
    # 9.  字符串.lower() 字母全部小写 应用场景：验证码转大小写
    print(s.lower())
    print(s)
    # 10. 字符串.title()非字母隔开的每个部分的首字母大写
    l = "alex wusir*tai6dsa"
    print(l.title())
    # *. 首字母大写 str.capitalize()
    name = "oldboy"
    print(name.capitalize())
    # *. 大小写翻转 str.swapcase()
    name = "olDbOy"
    print(name.swapcase())
    # 11. 字符串.isdigit()字符是否只有数字组成
    age = "20"
    name = "Ada"
    print(age.isdigit())
    print(name.isdigit())

    num_str = "一千零一"
    print(num_str)
    print(
        num_str.isdecimal()
    )  # 如果 string 只包含数字则返回 True，全角数字如果 string 只包含数字则返回 True，全角数字
    print(num_str.isdigit())  # 如果 string 只包含数字则返回 True，全角数字、⑴、\u00b2
    print(num_str.isnumeric())  # 如果 string 只包含数字则返回 True，全角数字，汉字数字

    """*.字符串判断字母和数字组成"""
    # str.isalpha()字符是否只有字母组成
    age = "20"
    name = "Ada"
    print(name.isalpha())
    print(age.isalpha())
    # str.isalnum()字符是否只有数字和字母组成
    print("Ada20".isalnum())  # 比如可用于判断用户名是否合法
    # str.判断空白字符
    space_str = "      \t\n\r"
    print(space_str.isspace())

    # *-* coding:utf8 *-*

    # 引号前面的u告诉解释器这是一个utf8编码格式的字符串
    hello_str = u"hello世界"
    print(hello_str)
    for c in hello_str:
        print(c)

# =========================================  3.布尔类型 =========================================
# 主要用于逻辑运算
# 真 True 非 0 数 —— 非零即真 假 False 0
# 空字符串对应 bool False
# 非空即True
# flag = True
flag = False
if flag:
    y = 2 > 1
    print(y, type(y))
    l = ""
    print(l, type(bool(l)))


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
    """*.列表的索引——与同为序列类型的字符串完全相同"""
    # 正向索引从0开始
    # 反向索引从-1开始
    print(name[0])
    """列表的切片"""
    # 变量名[开始位置：结束位置：切片间隔]
    cars = ["BYD", "BMW", "AUDI", "TOYOTA"]
    # 正向切片
    print(cars[:3])  # 前三个元素，开始位置缺省，默认为0；切片间隔缺省，默认为1
    print(cars[1:4:2])  # 第二个到第四个元素 前后索引差为2
    print(cars[:])  # 获取整个列表，结束位置缺省，默认取值到最后
    print(cars[-4:-2])  # 获取前两个元素
    # 反向切片
    cars = ["BYD", "BMW", "AUDI", "TOYOTA"]
    print(cars[:-4:-1])  # 开始位置缺省，默认为-1
    print(cars[::-1])  # 获得反向列表

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

    """*.列表的转换"""
    # 字符串转列表
    print(list("人工智能是未来的趋势"))
    # 元组转列表
    print(list(("我", "们", "很", "像")))
    # 集合转列表
    print(list({"李雷", "韩梅梅", "Jim", "Green"}))

    """列表的数据统计"""
    name_list = ["张三", "李四", "王五", "王小二", "张三"]
    # len(length 长度) 函数可以统计列表中元素的总数
    list_len = len(name_list)
    print("列表中包含 %d 个元素" % list_len)
    ls = [1, 2, 3, 4, 5]
    len(ls)
    # count 方法可以统计列表中某一个数据出现的次数
    count = name_list.count("张三")
    print("张三出现了 %d 次" % count)
    # 从列表中删除第一次出现的数据，如果数据不存在，程序会报错
    name_list.remove("张三")
    print(name_list)
    # 列表中第一次出现待查元素的位置列表.index(待查元素)
    # 使用index方法需要注意，如果传递的数据不在列表中，程序会报错！
    languages = ["Python", "C", "R", "Java"]
    idx = languages.index("R")
    print(idx)

    """*.列表修改元素"""
    # 通过"先索引后赋值"的方式，对元素进行修改列表名[位置]=新值
    # 列表指定的索引超出范围，程序会报错！
    languages = ["Python", "C", "R", "Java"]
    languages[1] = "C++"
    print(languages)

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


# =========================================  组合类型：列表--操作：删除 =========================================
# """*.列表的删除"""
# flag = True
flag = False
if flag:

    """pop()"""
    #  pop() :删除列表i位置的元素 列表.pop(位置)
    languages = ["Python", "C", "C++", "R", "Java"]
    languages.pop(1)
    print(languages)
    # 不写位置信息，默认删除最后一个元素 .pop()有返回值
    languages.pop()
    print(languages)

    """remove()"""
    # remove(): 删除 - 删除列表中的第一次出现的待删元素 列表.remove(待删元素)
    languages = ["Python", "C", "R", "C", "Java"]
    languages.remove("C")
    print(languages)  # ['Python', 'R', 'C', 'Java']
    # 方法1 存在运算删除法
    # 缺点：每次存在运算，都要从头对列表进行遍历、查找、效率低
    languages = ["Python", "C", "R", "C", "Java"]
    while "C" in languages:
        languages.remove("C")
    print(languages)  # ['Python', 'R' , 'Java']

    """clear()"""
    # clear(): 删除 - clear 方法可以清空列表
    languages = ["Python", "C", "R", "C", "Java"]
    languages.clear()
    print(languages)

    """ del 关键字"""
    name_list = ["张三", "李四", "王五"]
    del name_list[0:1]  # 按照切片删除
    print(name_list)
    # (知道)使用 del 关键字(delete)删除列表元素
    # 提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法
    del name_list[1]
    # del 关键字本质上是用来将一个变量从内存中删除的
    name = "小明"
    # del name
    # 注意：如果使用 del 关键字将变量从内存中删除
    # 后续的代码就不能再使用这个变量了
    print(name)
    print(name_list)
    """ example 删除列表内的特定元素 """
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
    # 方法2 一次性遍历元素执行删除
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
    l2 = ["python%s期" % i for i in range(1, 16)]
    print(l2)
    print([i * i for i in range(1, 11)])
    # 支持多变量
    x = [1, 2, 3]
    y = [1, 2, 3]
    # 支持循环嵌套
    colors = ["black", "white"]
    sizes = ["S", "M", "L"]
    tshirts = ["{} {}".format(color, size) for color in colors for size in sizes]
    print(tshirts)
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

    # 生成器表达式：将列表推导式的 []  换成() 即可。
    # g = (i for i in range(100000000000))
    # print(g)
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())

    # 解析语法构造字典（字典推导）
    mcase = {"a": 10, "b": 34}
    mcase_frequency = {mcase[k]: k for k in mcase}
    print(mcase_frequency)

    squares = {i: i ** 2 for i in range(10)}
    for k, v in squares.items():
        print(k, ":  ", v)

    squared = {x ** 2 for x in [1, -1, 2]}
    print(squared)

    # 生成器表达式
    squares = (i ** 2 for i in range(10))
    print(squares)

    colors = ["black", "white"]
    sizes = ["S", "M", "L"]
    tshirts = ("{} {}".format(color, size) for color in colors for size in sizes)
    for tshirt in tshirts:
        print(tshirt)

    # 条件表达式¶
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


# =========================================  组合类型：元组（tuple） =========================================
# 元组是不可变类型
# 元组里的数据不能修改
# 元组是一个可以使用多种类型元素，一旦定义，内部元素不支持增、删和修改操作的序列类型
# 通俗的讲，可以将元组视作“不可变的列表”
# 元组的操作不支持元素增加、元素删除、元素修改操作 其他操作与列表的操作完全一致
# flag = True
flag = False
if flag:
    name = ("zhangsan", "lisi", "wangwu")
    print(name, type(name))
    # 1. 取值和取索引
    print(name[0])
    # 已经知道数据的内容，希望知道该数据在元组中的索引
    print(name.index("zhangsan"))
    # 2. 统计计数
    print(name.count("zhangsan"))
    # 统计元组中包含元素的个数
    print(len(name))
    # 直接迭代
    graduates = ("李雷", "韩梅梅", "Jim")
    for graduate in graduates:
        print("Congratulations, " + graduate)
    """打包与解包"""

    def f1(x):  # 返回x的平方和立方
        return x ** 2, x ** 3  # 实现打包返回

    print(f1(3))
    print(type(f1(3)))  # 元组类型
    a, b = f1(3)  # 实现解包赋值
    print(a)
    print(b)
    # example
    numbers = [201901, 201902, 201903]
    name = ["小明", "小红", "小强"]
    list(zip(numbers, name))
    for number, name in zip(numbers, name):  # 每次取到一个元组，立刻进行解包赋值
        print(number, name)
    # example
    info_tuple = ("小明", 21, 1.85)
    # 格式化字符串后面的 `()` 本质上就是元组
    print("%s 年龄是 %d 身高是 %.2f" % info_tuple)
    info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
    print(info_str)

# =========================================  组合类型：字典（dict） =========================================
# 字典是可变类型
# 字典的键不能重复
# 通过键-值的映射实现数据存储和查找
# 多个元素用逗号分割，每个元素按照key:value的形式
# 字典的key只能用不可变类型，我们一般使用字符串，字典是一个可变类型。
# 映射类型： 通过“键”-“值”的映射实现数据存储和查找
# 字典是一个无序的数据集合，使用print函数输出字典时，通常输出的顺序和定义的顺序是不一致的！
# python3.6之后，字典是有序的，
# 字典的键必须是不可变类型，如果键可变，就找不到对应存储的值了
# 1.不可变类型：数字、字符串、元组。 一旦确定，它自己就是它自己，变了就不是它了。
# 2.可变类型：列表、字典、集合。一旦确定，还可以随意增删改。
# 字典的底层实现
# 通过稀疏数组来实现值的存储与访问
# 字典的创建过程
# 第一步：创建一个散列表（稀疏数组 N >> n）第一步：通过hash()计算键的散列值
# 第二步：根据计算的散列值确定其在散列表中的位置 # 极个别时候，散列值会发生冲突，则内部有相应的解决冲突的办法
# 第三步：在该位置上存入值
# 键值对的访问过程
# 第一步：计算要访问的键的散列值
# 第二步：根据计算的散列值，通过一定的规则，确定其在散列表中的位置
# 第三步：读取该位置上存储的值 如果存在，则返回该值 如果不存在，则报错KeyError
# flag = True
flag = False
if flag:
    """*.字典创建"""
    # 循环创建 .fromkeys（）
    dic1 = dict.fromkeys([1, 2, 3], "alex")
    print(dic1)
    # 陷阱：
    dic2 = dict.fromkeys([1, 2, 3], [])
    print(dic2)
    dic2[1].append("alex")
    print(dic2)
    # 直接创建
    information = {"name": "albert", "age": 18, "height": 1.83}
    informations = [
        {"name": "zs", "age": 20, "height": 1.74},
        {"name": "ls", "age": 19, "height": 1.65},
    ]
    print(information, type(information))
    print(informations, type(informations))

    """*.字典的取值"""
    # 字典的索引--通过字典[键]的形式来获取对应的值
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    print(students[201902])
    print(information["name"])
    # 在取值的时候，如果指定的key不存在，程序会报错！
    # print(information["name123"])
    # 变换迭代
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    # d.keys( ) d.values( )方法
    print(list(students.keys()))
    for student in students.keys():
        print(student)
    print(list(students.values()))
    # d.items( )方法及字典的遍历
    print(list(students.items()))
    for k, v in students.items():
        print(k, v)

    """*.字典的增加键值对 -- 变量名[新键] = 新值"""
    # 如果key不存在，会新增键值对
    # 如果key存在，会修改已经存在的键值对
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    # students[201904] = "小雪"
    print(students)
    # dic.setdefault() 有则不变，无责增加
    students.setdefault(201904, "新增小雪")
    print(students)
    # updata() 合并字典
    xiaoming_dict = {"name": "小明", "age": 18}
    temp_dict = {"height": 1.75, "age": 20}
    # 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
    xiaoming_dict.update(temp_dict)

    """*.字典的删除键值对"""
    # 再循环一个字典时，不能改变字典的大小
    # 通过del 变量名[待删除键]
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    del students[201903]
    print(students)
    # 通过变量名.pop(待删除键)
    # 在删除指定键值对的时候，如果指定的key不存在，程序会报错！
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    value = students.pop(201903)  # 删除键值对，同时获得删除键值对的值
    print(value)
    print(students)
    # 变量名.popitem()随机删除一个键值对，并以元组返回删除键值对
    # python3.6之后字典是有序的，默认删除最后一个
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    key, value = students.popitem()
    print(key, value)
    print(students)
    # clear() 清空字典
    students.clear()
    print(students)

    """*.字典的修改值"""
    # 通过先索引后赋值的方式对相应的值进行修改
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    students[201902] = "小雪"
    print(students)

    """字典的查找操作"""
    # d.get(key,default)从字典d中获取键key对应的值，如果没有这个键，则返回default
    # 小例子：统计"牛奶奶找刘奶奶买牛奶"中字符的出现频率
    s = "牛奶奶找刘奶奶买牛奶"
    d = {}
    print(d)
    for i in s:
        d[i] = d.get(i, 0) + 1
        print(d)
    # print(d)

    """字典的长度——键值对的个数"""
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    print(len(students))


# =========================================  组合类型：集合（set） =========================================
# 集合是可变类型
# 不能重复 没有顺序
# 一系列互不相等元素的无序集合
# 元素必须是不可变类型：数字，字符串或元组，可视作字典的键
# 可以看做是没有值，或者值为None的字典
# 可用于去重
# flag = True
flag = False
if flag:
    NBA_player = {
        "zhangsan",
        "lisi",
        "wangwu",
    }
    print(NBA_player, type(NBA_player))
    NBA_players = {"zhangsan", "lisi", "wangwu", "zhangsan"}
    print(NBA_players, type(NBA_players))
    # 小例子 通过集合进行交集并集的运算
    Chinese_A = {"刘德华", "张学友", "张曼玉", "钟楚红", "古天乐", "林青霞"}
    print(Chinese_A)
    Math_A = {"林青霞", "郭富城", "王祖贤", "刘德华", "张曼玉", "黎明"}
    print(Math_A)
    print(Chinese_A & Math_A)  # 交集 S & T 返回一个新集合，包括同时在集合S和T中的元素
    print(Chinese_A | Math_A)  # 并集 S | T 返回一个新集合，包括集合S和T中的所有元素
    print(Chinese_A ^ Math_A)  # 反交集 S ^ T 返回一个新集合，包括集合S和T中的非共同元素
    print(Chinese_A - Math_A)  # 差集 S - T 返回一个新集合，包括在集合S但不在集合T中的元素
    print(Chinese_A < Math_A)  # 子集
    print(Chinese_A > Math_A)  # 超集
    print(Chinese_A.issuperset(Math_A))  # 超集
    """集合的增加元素——S.add(x)"""
    stars = {"刘德华", "张学友", "张曼玉"}
    stars.add("王祖贤")
    print(stars)
    """集合的移除元素——S.remove(x)"""
    stars.remove("王祖贤")
    print(stars)
    # pop() 随机删除
    stars.pop()
    # clear() 清空集合
    stars.clear()
    """集合的长度——len(S)"""
    print(len(stars))
    """集合的遍历——借助for循环"""
    for star in stars:
        print(star)
    """list去重"""
    l1 = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8]
    set1 = set(l1)
    l2 = list(set1)
    print(l2)
    # 不可变数据类型
    set1 = {1, 2, 3}
    set3 = frozenset(set1)
    print(set3)


# =========================================  数据的复制 - 深浅拷贝 =========================================
# """*.列表的复制 深浅拷贝 """
# 列表内的元素可以分散的存储在内存中
# 列表存储的，实际上是这些元素的地址！！！——地址的存储在内存中是连续的
# flag = True
flag = False
if flag:
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
    # 引入深拷贝 深copy
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
    print(l1, l2)
    l1.append(666)
    l1[-2].append("太白")
    print(l1, type(l1))
    print(l2)

    # 应用场景：面试会考，解释深浅copy
    # 完全独立的copy一份数据，与原数据没有关系，深copy
    # 如果一份数据（列表）第二层时，你想与原数据进行公用，浅copy。

    #  面试题
    # 切片属于浅copy
    # l1 = [1,2,3,[22,33]]
    # l2 = l1[:]
    # # l1.append(666)
    # l1[-1].append(666)
    # print(l2)


# =========================================  字典 - example =========================================
# 字典的 快速查找
# flag = True
flag = False
if flag:
    import time

    # 列表方式
    ls_1 = list(range(1000000))  # 1000000个元素
    ls_2 = list(range(500)) + [-10] * 500  # 1000个元素
    start = time.time()
    count = 0
    for n in ls_2:
        if n in ls_1:
            count += 1
    end = time.time()
    print(
        "查找{}个元素，在ls_1列表中的有{}个，共用时{}秒".format(len(ls_2), count, round((end - start), 2))
    )
    # 字典方式
    import time

    d = {i: i for i in range(100000)}
    ls_2 = list(range(500)) + [-10] * 500

    start = time.time()
    count = 0
    for n in ls_2:
        try:
            d[n]
        except:
            pass
        else:
            count += 1
    end = time.time()
    print("查找{}个元素，在ls_1列表中的有{}个，共用时{}秒".format(len(ls_2), count, round(end - start)))
