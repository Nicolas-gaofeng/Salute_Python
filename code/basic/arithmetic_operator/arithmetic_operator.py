#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : arithmetic_operator.py
@author     : zgf
@brief      : python算数运算符
@attention  : life is short,I need python
"""


# =========================================  算术运算符 =========================================
# 和数学中的运算符的优先级一致，在 Python 中进行数学计算时，同样也是：
# 先乘除后加减
# 同级运算符是 从左至右 计算
# 可以使用 () 调整计算的优先级
# 加减乘除取模幂
# 整数与浮点数运算结果是浮点数
# 除法运算的结果是浮点数
# flag = True
flag = False
if flag:
    a = 10
    b = 20
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)  # 取模  %	取余数	返回除法的余数 9 % 2 = 1
    print(a ** b)  # 幂	又称次方、乘方，2 ** 3 = 8
    print(a // b)  # 取整除 返回除法的整数部分（商） 9 // 2 输出结果 4
    print(13 // 5)  # 整数商    x/y 向下取整数
    x = 1
    print(-x)  # 取反
    # 在 Python 中 * 运算符还可以用于字符串，计算结果就是字符串重复指定次数的结果
    print("-" * 50)
    print(1 + 1.5, type(1 + 1.5))  # 2.5 <class 'float'>
    print(2 / 5, type(2 / 5))  # 0.4 <class 'float'>
    print(8 / 4, type(8 / 4))  # 2.0 <class 'float'>


# =========================================  比较运算符 =========================================
#
# flag = True
flag = False
if flag:
    a = 10
    b = 20
    print(a == b)
    print(a != b)
    print(a > b)
    print(a < b)
    print(a >= b)
    print(a <= b)
    # 非空
    ls = [1]
    if ls:  # 数据结构不为空、变量不为0、None、False 则条件成立
        print("非空")
    else:
        print("空的")


# =========================================  逻辑运算 =========================================
# 与运算，True和False进行与运算结果应该为False
# 或运算，True和False进行或运算结果应该为True
# 非运算，将结果置非，即True变False,False变True
# 复合逻辑运算的优先级 非 > 与 > 或
# 优先级 （）> not >and>or
# 0对应的bool值为False,非0都为True
#  x or y if x is True,return x
#  求and与or相反
# flag = True
flag = False
if flag:
    a = 10
    b = 8
    c = 12
    print((a > b) and (b > c))  # 与
    print((a > b) or (b > c))  # 或
    print(not (a > b))  # 非
    print(a == b)  # 相等

    print(True and False)
    print(True or False)
    print(not (True and False))

    # bool ：用于将给定参数转换为布尔类型，如果没有参数，返回False。 ***
    print(bool(1 < 2 and 3 > 4 or 5 < 6 and 9 > 2 or 3 > 1))
    print(bool("fdsjkfl"))

    """逻辑运算作为指示条件"""
    n = 2800
    while True:
        m = eval(input("请输入一个正整数："))
        if m == n:
            print("你猜对啦")
            break
        elif m > n:
            print("太大了")
        else:
            print("太小了")

    """逻辑运算作为掩码"""
    import numpy as np

    x = np.array([[1, 3, 2, 5, 7]])  # 定义 numpy数组
    print(x > 3)  # [[False False False  True  True]]
    print(x[x > 3])  # [5 7]

    """数字逻辑运算"""
    #  x or y if x is True,return x
    #  x and y if x is True,return y
    print(1 or 2)  # 1
    print(1 and 2)  # 2
    print(5 or 2)  # 5
    print(5 and 2)  # 2
    print(0 or 3 and 5 or 4)  # 5


# =========================================  赋值运算 =========================================
# 使用 = 可以给变量赋值
# flag = True
flag = False
if flag:
    a = 10
    b = 20
    a += b
    print(a)
    a -= b
    print(a)
    a *= b
    print(a)
    a /= b
    print(a)


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


# =========================================  身份运算 =========================================
# is比较id,判断的是两个变量的id值是否相同。是判断两个标识符是不是引用同一个对象
# is not 是判断两个标识符是不是引用不同对象
# ==比较值
# 在内存中id都是唯一的，如果两个变量指向的值的id相同，就证明他们在内存中是同一个。
# 与None值比较 判断某个变量是否为None时，请使用is 而不是==
# 如果is是True, == 一定是True。
# flag = True
flag = False
if flag:
    a = "sdasdsadasdasdasdasdasdddddddddddddddddddddddddddfsafdafaag.62952a9fadggagag"
    b = "sdasdsadasdasdasdasdasdddddddddddddddddddddddddddfsafdafaag.62952a9fadggagag"
    print(a is b)  #  用于判断 两个变量 引用对象是否为同一个
    print(a is None)
    print(a == b)  # 用于判断引用变量的值 是否相等
    print(a is not b)


# =========================================  存在运算 =========================================
# 元素 in 列表/字符串
# flag = True
flag = False
if flag:
    cars = ["BYD", "BMW", "AUDI", "TOYOTA"]
    print("BMW" in cars)
    print("BENZ" in cars)
    print("BMW" not in cars)
    print("BENZ" not in cars)


# =========================================  数学运算操作函数 - abs() =========================================
# 求绝对值 abs()
# flag = True
flag = False
if flag:
    print(abs(-5))  # 5
    print(abs(3 + 4j))  # 5.0 # 对复数a+bj 执行的是求模运算(a^2+b^2)^0.5


# =========================================  数学运算操作函数 -  pow(x,n) =========================================
# 幂次方 pow(x,n)
# pow：求x**y次幂。（三个参数为x**y的结果对z取余） **
# flag = True
flag = False
if flag:
    print(pow(2, 5))  # 32 # pow(x,n) x的n次方  等价于x**n
    print(pow(2, 5, 3))  # 2 # 2^5 % 3  更快速


# =========================================  数学运算操作函数 -  round(x,n) =========================================
# 四舍五入 round(x,n) 保留浮点数的小数位数，默认保留整数,四舍五入。
# flag = True
flag = False
if flag:
    a = 1.618
    print(round(a))  # 2 默认四舍五入为整数
    print(round(a, 2))  # 1.62 参数2表示四舍五入后保留2位小数
    print(round(a, 5))  # 1.618 位数不足，无需补齐


# =========================================  数学运算操作函数 -  divmod(x,y) =========================================
# 整数商和模运算 divmod(x,y)
# 等价于返回二元元组（x//y,x % y）
# flag = True
flag = False
if flag:
    #  divmod：计算除数与被除数的结果，返回一个包含商和余数的元组(a // b, a % b)。
    print(divmod(13, 5))  # (2, 3)  较（x//y,x % y）更快，只执行了一次x/y
    # 分页。
    # 103 条数据，你每页显示12 条数据，你最终显示多少页。
    print(divmod(103, 12))


# =========================================  数学运算操作函数 -  max( )  min( ) =========================================
# 序列最大/最小值 max( )  min( )
# flag = True
flag = False
if flag:
    # max：返回可迭代对象的最大值（可加key，key为函数名，通过函数的规则，返回最大值）。
    a = [3, -2, 3, 6, 9, 4, 5]
    print("max:", max(a))  # max:9
    # min：返回可迭代对象的最小值（可加key，key为函数名，通过函数的规则，返回最小值）。
    print("min:", min(a))  # min:-2
    print("min:", min(a, key=abs))  # min:-2

    # 求出年龄最小的那个元组
    ls = [("alex", 1000), ("太白", 18), ("wusir", 500)]
    min1 = min([i[1] for i in ls])
    for i in ls:
        if i[1] == min1:
            print(i)

    def func(x):
        return x[1]  # 1000  18  500

    print(min([("alex", 1000), ("太白", 18), ("wusir", 500)], key=func))
    # 1,他会将iterable的每一个元素当做函数的参数传进去。
    # 2，他会按照返回值去比较大小。
    # 3,返回的是 遍历的元素 x.
    # [('alex',1000),('太白',18),('wusir',500)]


# =========================================  数学运算操作函数 -  sum(x) =========================================
# 求和sum(x)
# sum：对可迭代对象进行求和计算（可设置初始值）
# flag = True
flag = False
if flag:
    print(sum((1, 2, 3, 4, 5)))  # 15
    print(sum([1, 2, 3, 4, 100, 101]))
    # sum(iterable,start_num)
    # iterable – 可迭代对象，如：列表(list)、元组(tuple)、集合(set)、字典(dictionary)。
    # start – 指定相加的参数，如果没有设置这个值，默认为0。
    # 也就是说sum() 最后求得的值 = 可迭代对象里面的数加起来的总和(字典:key值相加) + start的值(如果没写start的值，则默认为0)
    print(sum([1, 2, 3, 4, 100, 101], 100))
    print(sum({1: 5, 2: 6, 3: 7}))  # 6   in dictionary key
    print(sum([int(i) for i in [1, "2", 3, "4", "100", 101]]))


# =========================================  数学运算操作函数 -  借助科学计算库 math\scipy\numpy =========================================
# 借助科学计算库 math\scipy\numpy
# flag = True
flag = False
if flag:
    import math  # 导入库
    import numpy as np

    print(math.exp(1))  # 2.718281828459045 指数运算 e^x
    print(math.log2(2))  # 1.0 对数运算
    print(math.sqrt(4))  # 2.0 开平方运算  等价于4^0.5

    a = [1, 2, 3, 4, 5]
    print(np.mean(a))  # 3.0 求均值
    print(np.median(a))  # 3.0 求中位数
    print(np.std(a))  # 1.4142135623730951 求标准差
