#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : data_type_string.py
@author     : zgf
@brief      : 数据类型- string
@attention  : life is short,I need python
"""


# =========================================  字符串 - 创建 =========================================
# 单引号‘’ 双引号“” 三引号‘’‘ ’‘’
# 内部编码方式 Unicode
# 通过紧凑数组实现字符串的存储
# 数据在内存中是连续存放的，效率更高，节省空间
# flag = True
flag = False
if flag:
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


# =========================================  字符串 - 拆分与拼接 =========================================
#
# flag = True
flag = False
if flag:

    """*.字符串的拼接  +  """
    a = "I love "
    b = "my wife "
    print(a + b)

    """*.字符串的成倍复制： 字符串 * n  n * 字符串"""
    c = a + b
    print(c * 3)
    print(3 * c)

    """*.字符串的聚合"""
    # “聚合字符”.join(可迭代数据类型)：可迭代类型 如：字符串、列表
    s = "12345"
    s_join = ",".join(s)
    print(s_join)  # 1,2,3,4,5
    #     序列类型的元素必须是字符类型
    # s = [1, 2, 3, 4, 5]
    s = ["1", "2", "3", "4", "5"]
    print("*".join(s))  # 1*2*3*4*5

    """*. 字符串的分割"""
    # 字符串.split(分割字符)：返回一个列表 原字符串不变
    languages = "Python C C++ Java PHP R"
    # 默认按照空格分隔
    languages_list = languages.split()
    print(languages_list)
    print(languages)
    s = "aleclwle"
    print(s.split("l", 1))  # 分隔一次 1代表分隔次数
    print(s.rsplit("l"))  # 从右至左分隔


# =========================================  字符串 - 取值 =========================================
#
# flag = True
flag = False
if flag:

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

    """*.按切片取值"""
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


# =========================================  字符串 - 查找 =========================================
#
# flag = True
flag = False
if flag:
    """*.成员运算 ：子集in全集  任何一个连续的切片都是原字符串的子集"""
    folk_singers = "Peter, Paul and Mary"
    print("Peter" in folk_singers)
    print("PPM" in folk_singers)

    """*. 查找指定字符串"""
    hello_str = "hello world"
    # index同样可以查找指定的字符串在大字符串中的索引
    print(hello_str.index("llo"))
    # 注意：如果使用index方法传递的子字符串不存在，程序会报错！
    # print(hello_str.index("abc"))
    print(hello_str.find("llo"))
    # find如果指定的字符串不存在，会返回-1
    print(hello_str.find("abc"))
    print(hello_str.find("lo", 1, -1))  # 返回整体的索引，搜索的切片

    """*. 判断是否以指定字符串开始"""
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


# =========================================  字符串 - 替换 =========================================
#
# flag = True
flag = False
if flag:
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
    s2 = s.replace("i", "I", 1)  # 1代表可以设置次数
    print(s2)


# =========================================  字符串 - 判断 =========================================
#
# flag = True
flag = False
if flag:
    """字符串.upper() 字母全部大写"""
    s = "hello python"
    print(s.upper())

    """字符串.lower()  字母全部小写 应用场景：验证码转大小写"""
    print(s.lower())
    print(s)

    """字符串.title()非字母隔开的每个部分的首字母大写"""
    l = "alex wusir*tai6dsa"
    print(l.title())

    """首字母大写 str.capitalize()"""
    name = "oldboy"
    print(name.capitalize())

    """大小写翻转 str.swapcase()"""
    name = "olDbOy"
    print(name.swapcase())

    """字符串.isdigit()字符是否只有数字组成"""
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

    """str.isspace()判断空白字符"""
    space_str = "      \t\n\r"
    print(space_str.isspace())

    # *-* coding:utf8 *-*
    # 引号前面的u告诉解释器这是一个utf8编码格式的字符串
    hello_str = u"hello世界"
    print(hello_str)
    for c in hello_str:
        print(c)


# ========================================= 转义字符 =========================================
# flag = True
flag = False
if flag:
    # \t 在控制台输出一个 制表符，协助在输出文本时 垂直方向 保持对齐
    print("1\t2\t3")
    print("10\t20\t30")

    # \n 在控制台输出一个 换行符
    print("hello\n python")

    # \" 可以在控制台输出 "
    print('hello"hello')


# =========================================  字符串练习 =========================================
# 字符串文本对齐
# 假设：以下内容是从网络上抓取的
# 要求：顺序并且居中对齐输出以下内容
# flag = True
flag = False
if flag:
    poem = ["\t\n登鹳雀楼", "王之涣", "白日依山尽\t\n", "黄河入海流", "欲穷千里目", "更上一层楼"]
    for poem_str in poem:
        # 先使用strip方法去除字符串中的空白字符
        # 再使用center方法居中显示文本""为填入字符
        print("|%s|" % poem_str.strip().center(10, "　"))
    # 1. 将字符串中的空白字符全部去掉
    # 2. 再使用 " " 作为分隔符，拼接成一个整齐的字符串
    poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t\t\n更上一层楼"
    print(poem_str)
    # 1. 拆分字符串
    poem_list = poem_str.split()
    print(poem_list)
    # 2. 合并字符串
    result = " ".join(poem_list)
    print(result)