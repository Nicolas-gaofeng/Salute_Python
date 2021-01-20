#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : function_operation.py
@author     : zgf
@brief      : 函数
@attention  : life is short,I need python
"""


# ========================================= 函数 - 调用 =========================================
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


# ========================================= 函数 - 调用 =========================================
# 函数 - 调用
# flag = True
flag = False
if flag:
    """99乘法表"""

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

    """阶乘"""

    def factoria(n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    print("打印乘法表".center(50, "*"))
    multiple_table()
    print("阶乘".center(50, "*"))
    print(factoria(5))
    print(factoria(20))


# ========================================= 函数 -  引用 =========================================
#
# if flag:
# flag = True
flag = False
if flag:

    def test(num):
        print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))
        # 1> 定义一个字符串变量
        result = "hello"
        print("函数要返回数据的内存地址是 %d" % id(result))
        # 2> 将字符串变量返回，返回的是数据的引用，而不是数据本身
        return result

    # 1. 定义一个数字的变量
    a = 10
    # 数据的地址本质上就是一个数字
    print("a 变量保存数据的内存地址是 %d" % id(a))

    # 2. 调用 test 函数，本质上传递的是实参保存数据的引用，而不是实参保存的数据！
    # 注意：如果函数有返回值，但是没有定义变量接收
    # 程序不会报错，但是无法获得返回结果
    r = test(a)
    print("%s 的内存地址是 %d" % (r, id(r)))


# ========================================= 函数 -  闭包 =========================================
# 闭包：延伸了作用域的函数
# 内层函数对外层函数的变量（非全局变量）的引用，并返回 这样就形成了闭包。
# 闭包作用：
#         当程序执行时，遇到了函数执行，他会在内存中开辟一个空间，局部名称空间，
#         如果这个函数内部形成了闭包，
#         那么他就不会随着函数的结束而消失。
# flag = True
flag = False
if flag:
    # 闭包1
    def wraaper():
        name = "alex"

        def inner():
            print(name)

        print(inner.__closure__)
        inner()
        return inner

    wraaper()
    # 不是闭包 name为全局变量
    name = "alex"

    def wraaper():
        def inner():
            print(name)

        print(inner.__closure__)  # None 返回none代表不是闭包
        inner()
        return inner

    wraaper()

    name = "alex"

    def wraaper(n):
        # n = 'alex' # 相当于外界传入name，函数内部创建一个n的变量并赋值alex
        def inner():
            print(n)

        print(inner.__closure__)  # 返回的cell at 0x000002AD93BF76D8:
        inner()
        return inner

    wraaper(name)

    # nonlocal允许内嵌的函数来修改闭包变量
    def outer():
        x = 1

        def inner():
            nonlocal x
            x = x + 100
            return x

        return inner

    f = outer()
    f()
    # 闭包例子 爬虫
    from urllib.request import urlopen

    def index():
        url = "http://m.gaosan.com/xiaohua/"

        def get():
            return urlopen(url).read()

        return get

    xiaohua = index()  # get
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    content = xiaohua()  # get()
    print(content.decode("utf-8"))

# ========================================= 函数 -  函数名的应用 =========================================
#
# if flag:
# flag = True
flag = False
if flag:
    # 1 ,函数名就是函数的内存地址。
    def func():
        print("111")

    print(func())

    # 2, 函数名可以作为变量。
    a = 2
    b = a
    c = b
    print(c)

    def func1():
        print(666)

    f1 = func1
    f2 = f1
    f2()

    # 3,函数名可以作为函数的参数。 --高阶函数

    def func1():
        print(666)

    def func2(x):
        print(x)  # <function func1 at 0x0000026C3D983BF8>
        # x()

    a = "太白"
    func2(a)
    print(func1)  # <function func1 at 0x0000026C3D983BF8>

    def func():
        print(666)

    def func1():
        func()

    def func2(x):
        x()  # func1()

    func2(func1)

    # 函数名可以当做函数的返回值。

    def wraaper():
        def inner():
            print("inner   ")

        return inner

    ret = wraaper()  # inner
    ret()  # inner()

    def func2():
        print("in func2")

    def func3(x):  # x = func2
        print("in func3")
        return x  # func2

    f1 = func3(func2)  # func2
    f1()

    # 函数名可以作为容器类类型的元素。

    a = 6
    b = 4
    c = 5
    l1 = [a, b, c]
    print(l1)

    def func1():
        print("in func1")

    def func2():
        print("in func2")

    def func3():
        print("in func3")

    def func4():
        print("in func4")

    l1 = [func1, func2, func3, func4]
    for i in l1:
        i()

    # 向上面的函数名这种，第一类对象。

    """ globals() locals()"""
    # globals() # 返回全局变量的一个字典。
    # locals()  返回 当前位置 的局部变量的字典。

    def func1():
        a = 2
        b = 3
        print(globals())
        print(locals())

        def inner():
            c = 5
            d = 6
            print(globals())
            print(locals())

        inner()

    # print(globals())
    # print(locals())
    func1()


# ========================================= 函数的参数 =========================================
# 形参（形式参数）：函数定义时的参数，实际上就是变量名
# 实参（实际参数）：函数调用时的参数，实际上就是变量的值
# 位置参数：严格按照位置顺序，用实参对形参进行赋值(关联）实参与形参个数必须一一对应，一个不能多，一个不能少；用在参数比较少的时候
# 关键字参数：打破位置限制，直呼其名的进行值的传递（形参=实参）必须遵守实参与形参数量上一一对应；多用在参数比较多的场合
# 位置参数可以与关键字参数混合使用
# 但是，位置参数必须放在关键字参数前面
# 不能为同一个形参重复传值
# 默认参数：在定义阶段就给形参赋值——该形参的常用值 在定义阶段就给形参赋值——该形参的常用值 默认参数必须放在非默认参数后面 调用函数时，可以不对该形参传值
# flag = True
flag = False
if flag:

    def function(x, y, z):
        print(x, y, z)

    function(y=1, z=2, x=3)  # x = 1; y = 2; z = 3

    function(1, z=2, y=3)
    function(1, 2, z=3)

    def sum_2_num(num1, num2):
        """对两个数字的求和"""
        # num1 = 10
        # num2 = 20
        result = num1 + num2
        print("%d + %d = %d" % (num1, num2, result))

    sum_2_num(1, 2)

    # 默认参数
    def register(name, age, sex="male"):
        print(name, age, sex)

    register("林志玲", 38, "female")
    register("大杰仔", 18)
    # 函数的缺省参数
    gl_list = [6, 3, 9]

    # 默认按照升序排序 - 可能会多！
    # gl_list.sort()

    # 如果需要降序排序，需要执行reverse参数
    gl_list.sort(reverse=True)

    print(gl_list)
    # 函数的缺省参数定义
    def print_info(name, gender=True):
        """

        :param name: 班上同学的姓名
        :param gender: True 男生 False 女生
        """

        gender_text = "男生"

        if not gender:
            gender_text = "女生"

        print("%s 是 %s" % (name, gender_text))

    # 假设班上的同学，男生居多！
    # 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
    print_info("小明")
    print_info("老王")
    print_info("小美", False)
    # 函数的缺省参数注意点
    def print_info(name, title="", gender=True):
        """

        :param title: 职位
        :param name: 班上同学的姓名
        :param gender: True 男生 False 女生
        """

        gender_text = "男生"

        if not gender:
            gender_text = "女生"

        print("[%s]%s 是 %s" % (title, name, gender_text))

    # 假设班上的同学，男生居多！
    # 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
    print_info("小明")
    print_info("老王")
    print_info("小美", gender=False)

    """不可变和可变参数"""

    def demo(num, num_list):
        print("函数内部的代码")

        # 在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量
        num = 100
        num_list = [1, 2, 3]

        print(num)
        print(num_list)
        print("函数执行完成")

    gl_num = 99
    gl_list = [4, 5, 6]
    demo(gl_num, gl_list)
    print(gl_num)
    print(gl_list)

    # 函数的多值参数
    def demo(num, *nums, **person):

        print(num)
        print(nums)
        print(person)

    # 多值参数求和
    # 在函数的定义时，在 *位置参数，聚合。
    # *args 将所有的实参的位置参数聚合到一个元组，并将这个元组赋值给args
    def sum_numbers(*args):
        # def sum_numbers(args):

        num = 0

        print(args)
        # 循环遍历
        for n in args:
            num += n

        return num

    result = sum_numbers(1, 2, 3, 4, 5)
    print(result)

    # demo(1)
    demo(1, 2, 3, 4, 5, name="小明", age=18)

    # 元组字典的拆包
    def demo(*args, **kwargs):

        print(args)
        print(kwargs)

    # 元组变量/字典变量
    gl_nums = (1, 2, 3)
    gl_dict = {"name": "小明", "age": 18}

    # demo(gl_nums, gl_dict)

    # 拆包语法，简化元组变量/字典变量的传递
    demo(*gl_nums, **gl_dict)

    demo(1, 2, 3, name="小明", age=18)

    # 函数内部通过方法修改可变参数
    def demo(num_list):
        print("函数内部的代码")

        # 使用方法修改列表的内容
        num_list.append(9)

        print(num_list)

        print("函数执行完成")

    gl_list = [1, 2, 3]
    demo(gl_list)
    print(gl_list)

# =========================================  函数体与变量作用域 =========================================
# 函数体就是一段只在函数被调用时，才会执行的代码，代码构成与其他代码并无不同
# 局部变量——仅在函数体内定义和发挥作用
# 全局变量——外部定义的都是全局变量
# 全局变量可以在函数体内直接被使用
# python中，名称空间分三种：
# 全局名称空间
# 局部名称空间（临时）
# 内置名称空间

# 作用域：
#     全局作用域 全局名称空间 内置名称空间
#     局部作用域 局部名称空间（临时）

# 取值顺序： 就近原则
# 局部名称空间  ---->  全局名称空间 ----->内置名称空间  单向从小到大范围
# flag = True
flag = False
if flag:

    def multipy(x, y):
        z = x * y
        return z

    multipy(2, 9)
    # print(z)  # 函数执行完毕，局部变量z已经被释放掉了

    n = 3
    ls = [0]

    def multipy(x, y):
        z = n * x * y
        ls.append(z)
        return z

    print(multipy(2, 9))
    print(ls)
    # 通过global 在函数体内定义全局变量
    def multipy(x, y):
        global z
        z = x * y
        return z

    print(multipy(2, 9))
    print(z)

    # example
    def demo1():
        # 定义一个局部变量
        # 1> 出生：执行了下方的代码之后，才会被创建
        # 2> 死亡：函数执行完成之后
        num = 10

        print("在demo1函数内部的变量是 %d" % num)

    def demo2():
        num = 99

        print("demo2 ==> %d" % num)
        pass

    # 在函数内部定义的变量，不能在其他位置使用
    # print("%d" % num)
    demo1()
    demo2()

    # 全局变量
    num = 10

    def demo1():
        print("demo1 ==> %d" % num)

    def demo2():
        print("demo2 ==> %d" % num)

    demo1()
    demo2()

    # 函数不能直接修改全局变量
    num = 10

    def demo1():
        # 希望修改全局变量的值
        # 在 python 中，是不允许直接修改全局变量的值
        # 如果使用赋值语句，会在函数内部，定义一个局部变量
        num = 99

        print("demo1 ==> %d" % num)

    def demo2():
        print("demo2 ==> %d" % num)

    demo1()
    demo2()

    # 直接修改全局变量
    # 全局变量
    num = 10

    def demo1():
        # 希望修改全局变量的值 - 使用 global 声明一下变量即可
        # global 关键字会告诉解释器后面的变量是一个全局变量
        # 再使用赋值语句时，就不会创建局部变量
        global num

        num = 99

        print("demo1 ==> %d" % num)

    def demo2():
        print("demo2 ==> %d" % num)

    demo1()
    demo2()

    # 全局变量的位置
    # 注意：在开发时，应该把模块中的所有全局变量
    # 定义在所有函数上方，就可以保证所有的函数
    # 都能够正常的访问到每一个全局变量了
    num = 10
    # 再定义一个全局变量
    title = "黑马程序员"
    # 再定义一个全局变量
    name = "小明"

    def demo():
        print("%d" % num)
        print("%s" % title)
        print("%s" % name)

    # # 再定义一个全局变量
    # title = "黑马程序员"

    demo()

    # # 再定义一个全局变量
    # name = "小明"

# ========================================= 函数的返回值 =========================================
# 函数中如果遇到retrun,则直接结束函数。
# flag = True
flag = False
if flag:
    """单个返回值"""

    def sum_2_num(num1, num2):
        """对两个数字的求和"""
        result = num1 + num2
        # 可以使用返回值，告诉调用函数一方计算的结果
        return result
        # 注意：return 就表示返回，下方的代码不会被执行到！
        # num = 1000

    # 可以使用变量，来接收函数执行的返回结果
    sum_result = sum_2_num(10, 20)
    print("计算结果：%d" % sum_result)
    """多个返回值"""

    def foo(x):
        return 1, x, x ** 2, x ** 3  # 逗号分开，打包返回

    print(foo(3))

    def measure():
        """测量温度和湿度"""

        print("测量开始...")
        temp = 39
        wetness = 50
        print("测量结束...")

        # 元组-可以包含多个数据，因此可以使用元组让函数一次返回多个值
        # 如果函数返回的类型是元组，小括号可以省略
        # return (temp, wetness)
        return temp, wetness

    # 元组
    result = measure()
    print(result)

    # 需要单独的处理温度或者湿度 - 不方便
    print(result[0])
    print(result[1])

    # 如果函数返回的类型是元组，同时希望单独的处理元组中的元素
    # 可以使用多个变量，一次接收函数的返回结果
    # 注意：使用多个变量接收结果时，变量的个数应该和元组中元素的个数保持一致
    gl_temp, gl_wetness = measure()

    print(gl_temp)
    print(gl_wetness)

    """解包赋值"""
    a, b, c, d = foo(3)  # 解包赋值
    print(a)
    print(b)
    print(c)
    print(d)

    # 可以有多个return 语句，一旦其中一个执行，代表了函数运行的结束
    def is_holiday(day):
        if day in ["Sunday", "Saturday"]:
            return "Is holiday"
        else:
            return "Not holiday"
        print("啦啦啦德玛西亚，啦啦啦啦")  # 你丫根本没机会运行。。。

    print(is_holiday("Sunday"))
    print(is_holiday("Monday"))

    # 没有return语句，返回值为None
    def foo():
        print("我是孙悟空")

    res = foo()
    print(res)


# ========================================= 递归函数--函数的嵌套调用 =========================================
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
    # 递归函数
    def sum_number(num):

        print(num)
        # 递归的出口，当参数满足某个条件时，不再执行函数
        if num == 1:
            return

            # 自己调用自己
        sum_number(num - 1)

    sum_number(3)
    # 递归求和

    # 定义一个函数 sum_numbers
    # 能够接收一个 num 的整数参数
    # 计算 1 + 2 + ... num 的结果

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


# =========================================  函数 - hash()函数 =========================================
# 1.2.3内存相关 hash id ***
#
# 　　hash：获取一个对象（可哈希对象：int，str，Bool，tuple）的哈希值。
#     id:获取该对象的内存地址。

# hash()
# 字典：会将你的所有的key 在内存中转化成id
# flag = True
flag = False
if flag:

    dic = {"name": "alex", "kfdshjfhdskjfhsd": "123"}
    print(hash("name"))
    print(hash("name1"))
    print(hash("fdsmkfghsdlksld"))
    print(hash(1))
    print(hash(100))
    print(hash(100000000000))
    print(hash([1, 2, 3]))

# =========================================  函数 - 内置函数 =========================================
#
# flag = True
flag = False
if flag:
    """
    len()
    range()
    min()
    max()
    input()
    print()
    id()
    type()
    int()
    list()
    str()
    set()
    next()
    tuple()
    iter()
    bool()
    dict()
    globals()
    dir()
    enmurate()
    locals()
    open()
    send()
    """
    # 作用域相关  ******
    # globals() :返回一个字典：包含全部的全局变量。
    # locals() ： 返回一个字典：包含的是当前作用域 所有的变量。
    b = 2

    def func1():
        a = 1
        print(locals())
        print(globals())

    func1()

    # # exec 执行字符串类型的代码，不返回结果  代码流
    s3 = """for i in range(3):
        print(i)
    """
    print(exec(s1))
    exec(s3)

    # 1.2.3文件操作相关
    #
    # 　　open：函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。 *****
    #
    # 1.2.4模块相关__import__　 ***
    #
    # 　　__import__：函数用于动态加载类和函数 。

    # 1.2.5帮助
    #
    # 　　help：函数用于查看函数或模块用途的详细说明。 **
    # name = 'alex'
    # print(help(name))

    # 1.2.6调用相关
    #
    # 　　callable：函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；
    # 但如果返回False，调用对象ojbect绝对不会成功。  ***
    name = "alex"

    def func1():
        pass

    print(callable(name))  # False
    print(callable(func1))  # True # 可以被调用
    #
    # 1.2.7查看内置属性  ***
    #
    # 　　dir：函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
    # 如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
    # name = 'alex'
    # print(dir(name))

    # range：函数可创建一个整数对象，一般用在 for 循环中。
    #  python2x: range(3) ---> [0,1,2] 列表
    #            xrange(3) ---> 迭代器。
    #  python3x: range(3) ---> range(0,3) 可迭代对象

    # 　　next：内部实际使用了__next__方法，返回迭代器的下一个项目。
    # 　　iter：函数用来生成迭代器（讲一个可迭代对象，生成迭代器）。


# ========================================= 匿名函数 =========================================
# 基本形式 lambda 变量: 函数体
# 匿名函数  lambda表达式，
# 匿名函数 不单独使用，多与内置函数结合
# 普通函数 有且只有返回值的函数才可以用匿名函数进行简化，一行函数。
# 常用用法 ：在参数列表中最适合使用匿名函数，尤其是与key = 搭配
# flag = True
flag = False
if flag:
    ls = [(93, 88), (79, 100), (86, 71), (85, 85), (76, 94)]
    ls.sort()
    print(ls)  # [(76, 94), (79, 100), (85, 85), (86, 71), (93, 88)]
    ls.sort(key=lambda x: x[1])
    print(ls)  # [(86, 71), (85, 85), (93, 88), (76, 94), (79, 100)]
    ls = [(93, 88), (79, 100), (86, 71), (85, 85), (76, 94)]
    temp = sorted(ls, key=lambda x: x[0] + x[1], reverse=True)
    print(temp)  # [(93, 88), (79, 100), (85, 85), (76, 94), (86, 71)]
    # max() min()
    ls = [(93, 88), (79, 100), (86, 71), (85, 85), (76, 94)]
    n = max(ls, key=lambda x: x[1])
    print(n)  # (79, 100)
    n = min(ls, key=lambda x: x[1])
    print(n)  # (86, 71)

    func2 = lambda x: x ** 2
    print(func2(6))

    func2 = lambda x, y: x + y
    print(func2(1, 2))

    l2 = [(1, 1000), (2, 18), (4, 250), (3, 500)]
    print(sorted(l2, key=lambda x: x[1]))

    dic = {"k1": 10, "k2": 100, "k3": 30}
    # 1,利用内置函数匿名函数将dic按照值进行排序。
    print(sorted(dic, key=lambda x: dic[x]))
    print(sorted(dic.items(), key=lambda x: x[1]))
    # [1,5,7,4,8]
    # 利用内置函数匿名函数 计算列表的每个数的2倍。
    print(list(map(lambda x: x * 2, [1, 5, 7, 4, 8])))
    # [5,8,11,9,15]
    # 利用内置函数匿名函数，将值大于10的留下来。
    print(list(filter(lambda x: x > 10, [5, 8, 11, 9, 15])))

    # func = lambda x:x if x > 2 else x * 2

# ========================================= 动态交互 input() 输入 =========================================
# input接收的数据输出的是一个字符串
# flag = True
flag = False
if flag:
    x = input("请输入一个数字：")
    print(x, type(x))

# ========================================= eval() 去掉引号 =========================================
# input接收的数据输出的是一个字符串
# 不建议使用 ***
# flag = True
flag = False
if flag:
    x = input("请输入一个数字：")
    print(x, type(x))
    x = eval(x)
    print(x, type(x))

    # 1.2.1 字符串类型代码的执行 eval，exec，complie
    # eval: 执行字符串类型的代码，并返回最终结果
    s1 = "1+2+3"
    print(s1)
    s2 = "{'name':'alex'}"
    print(eval(s1), type(eval(s1)))
    print(eval(s2), type(eval(s2)))

# ========================================= print() 打印 =========================================
# flag = True
flag = False
if flag:
    print(1)  # 默认换行
    print(2)  # 默认换行
    print(123, end="")  # 换行控制end=
    print(123, end="留在这里")  # 换行控制end可自定义
    # 在默认情况下，print 函数输出内容之后，会自动在内容末尾增加换行
    print("*", end="---")
    print("*")
    # 　　input:函数接受一个标准输入数据，返回为 string 类型。
    # 　　print:打印输出。
    print("666")
    print(1, 2, 3, 4)  # 1 2 3 4
    print(*[1, 2, 3])  # 1 2 3

    def func1(*args, **kwargs):  # 函数的定义：*聚合。
        print(*args)  # (*(1,2,3,4))函数的执行： * 打散  print(1,2,3,4)
        # print(**kwargs)  # print(name='alex',age=1000) print会报错
        print(kwargs)

    func1(1, 2, 3, 4, name="alex", age=1000)
    print(1, 2, 3, sep="|")  # sep 打印多个内容是分隔符默认是空格
    print(1, end=" ")  # end：默认换行
    print(222)
    f = open("t1", encoding="utf-8", mode="w")
    print(666, "777", "888", file=f)

# ========================================= print() 组合输出 =========================================
# flag = True
flag = False
if flag:
    PI = 3.1415926
    E = 2.71828
    print("PI = ", PI, "E = ", E)

# ========================================= print() 占位输出 =========================================
# flag = True
flag = False
if flag:
    name = "xiaoming"
    age = 18
    """第一种方式 s为字符串，d为数字"""
    print("姓名为%s，年龄为%d" % (name, age))
    """第2种方式 s为字符串，d为数字"""
    print("姓名为%(name)s，年龄为%(age)d" % {"name": name, "age": age})
    """bug点，在格式化输出中，只想单纯表示一个%号时，应该用%%表示"""
    # msg = '我叫%s,今年%d岁，我的学习进度为%1' %(name,age)
    msg = "我叫%s,今年%d岁，我的学习进度为%%1" % (name, age)
    print(msg)


# ========================================= print() -格式化输出 =========================================
# flag = True
flag = False
if flag:
    # 定义字符串变量 name，输出 我的名字叫 小明，请多多关照！
    name = "大小明"
    print("我的名字叫 %s，请多多关照！" % name)

    # 定义整数变量 student_no，输出 我的学号是 000001
    student_no = 100123456
    print("我的学号是 %06d" % student_no)

    # 定义小数 price、weight、money，
    # 输出 苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元
    price = 8.5
    weight = 7.5
    money = price * weight
    print("苹果单价 %.2f 元／斤，购买了 %.3f 斤，需要支付 %.4f 元" % (price, weight, money))

    # 定义一个小数 scale，输出 数据比例是 10.00%
    scale = 0.8
    print("数据比例是 %.2f%%" % (scale * 100))

    # example 2
    PI = 3.1415926
    E = 2.71828
    print("PI = {0} , E = {1}".format(PI, E))  # 基本格式：“字符{0}字符{1}.format(v0,v1)”
    print("PI = {} , E = {}".format(PI, E))  # 按顺序分配
    print("PI = {1} , E = {0}".format(PI, E))  # 指定顺序分配
    print("PI = {0} , E = {0}".format(PI, E))  # 指定顺序分配

    print("我叫{name},今年{age},性别{sex}".format(age="28", name="zhangsna", sex="男"))
    # 填充输出
    print("PI = {0:_^20}".format(PI))  # 0代表占位符 ：表示对变量进行修饰 _表示填充的图案 ^表示中间 20表示输出的宽度
    print("PI = {0:*<20}".format(PI))  # 0代表占位符 ：表示对变量进行修饰 _表示填充的图案 <表示左对齐 20表示输出的宽度
    print("PI = {0:_>30}".format(PI))  # 0代表占位符 ：表示对变量进行修饰 _表示填充的图案 >表示右对齐 20表示输出的宽度
    # 数字千分位分隔符
    print("{0:,}".format(10000000))  # 数字千分位分隔符：在：后加，如果需要填充 ， 需要在最后
    print("{0:&>20,}".format(10000000))  # 第一步必须是填充
    # print("{0:,&>20}".format(10000000))  # 第一步必须是填充 不能先表示分隔符
    # 浮点数简化输出
    print("{0:.2f}".format(PI))  # 留两位小数
    print("{0:.3f}".format(PI))
    print("{0:.1%}".format(0.818727))  # 按百分号输出
    print("{0:.2%}".format(0.817819))
    print("{0:.2e}".format(0.818727))  # 科学计数法输出
    print("二进制{0:b},Unicode码{0:c},十进制{0:d},八进制{0:o},十六进制{0:x}".format(450))  # 整数的进制转换输出


# ========================================= type(变量) 类型判别 =========================================
# 使用type()可以查看一个变量的类型
# flag = True
flag = False
if flag:
    age = 20
    name = "Ada"
    print(type(age))
    print(type(name))


# ========================================= isinstance(变量,预判类型)  类型判别 =========================================
# isinstance(变量,预判类型) 承认继承
# 变量类型是预判类型的子类型，则为真，否则为假
# flag = True
flag = False
if flag:
    age = 20
    name = "zhangsan"
    print(isinstance(age, int))  # 承认继承
    print(isinstance(age, object))
    print(isinstance(name, object))  # object 是老祖宗


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


# ========================================= bytearry()   =========================================
# bytearry：返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
# flag = True
flag = False
if flag:

    # [97,110,103,115]
    ret = bytearray("alex", encoding="utf-8")
    print(id(ret))
    print(ret)  # bytearray(b'alex')
    print(ret[0])  # 97
    ret[0] = 65
    print(ret)  # bytearray(b'Alex')
    print(id(ret))


# ========================================= memoryview()   =========================================
#
# flag = True
flag = False
if flag:
    ret = memoryview(bytes("你好", encoding="utf-8"))
    print(len(ret))  # 6
    print(ret)  # <memory at 0x000001D3D6FCD048>  # [\xe4,\xbd,\xa0,\xe5,\xa5,\xbd]
    print(bytes(ret[:3]).decode("utf-8"))  # 你
    print(bytes(ret[3:]).decode("utf-8"))  # 好


# ========================================= all()  any()  =========================================
# all：可迭代对象中，全都是True才是True  ***  多做条件判断
# any：可迭代对象中，有一个True 就是True ***  多做条件判断
# flag = True
flag = False
if flag:
    """all(seq): 仅当seq中所有对象都为布尔真时返回True, 否则返回False"""
    """any(seq): 只要seq中任何一个对象为布尔真就返回True, 否则返回False"""
    # any() all()
    # any(x)判断x对象是否为空对象，如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true
    # all(x)如果all(x)参数x对象的所有元素不为0、''、False或者x为空对象，则返回True，否则返回False
    print(any([False, 1, 0, None]))  # True 0 False None 都是无
    print(all([False, 1, 0, None]))  # False


# ========================================= zip()  =========================================
# zip：函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。 *****
#     如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。
#     拉链方法  将多个iter 纵向组成一个个元组。
# flag = True
flag = False
if flag:

    l1 = [1, 2, 3, 5, 6, 7]
    tu1 = ("alex", "太白", "wusir", "女神")
    dic = {"name": "日天", "age": 28, "hobby": "tea", "weight": 100}
    print(zip(l1, tu1, dic))
    for i in zip(l1, tu1, dic):
        print(i)


# ========================================= filter()  =========================================
# filter：过滤· 迭代器。 *****
# flag = True
flag = False
if flag:

    l1 = [i for i in range(10)]

    def func1(x):
        return x % 2 == 0

    print(list(filter(func1, l1)))


# ========================================= map()  =========================================
# filter：过滤· 迭代器。 *****
# flag = True
flag = False
if flag:
    l1 = [1, 2, 3, 4]
    # print([i**2 for i in l1])
    def func(x):
        return x ** 2

    print(list(map(func, l1)))

    # print() sum reversed
    # key : min max map sorted filter zip

# ========================================= sorted()  =========================================
#  sorted：对所有可迭代的对象进行排序操作。 *****
# flag = True
flag = False
if flag:
    l1 = [2, 3, 5, 3, 1, 9, 8, 6]
    l1.sort()
    print(l1)
    print(sorted(l1))  # 形成了一个新列表
    print(l1)  # 原列表不变
    #
    l2 = [(1, 1000), (2, 18), (4, 250), (3, 500)]
    print(sorted(l2))

    def func1(x):
        return x[1]

    print(sorted(l2, key=func1, reverse=True))


# ========================================= repr()   =========================================
# repr()  json pickle序列化模块 特殊字符串，python字符串的区别
# flag = True
# flag = False
if flag:
    # repr:返回一个对象的string形式（原形毕露）。  *****
    print("alex")
    print(repr("ale,x"))
    print(repr("{'alex':'sb'}"))

    # 格式化输出 %r
    msg = "alex 是 %r的人" % ("德高望重")
    print(msg)


# =========================================  类型转换 =========================================
# 数字类型转字符串 str(数字类型)
# flag = True
flag = False
if flag:
    age = 20
    print("My age is " + str(age))
    # 仅有数字组成的字符串转数字 int() float()  eval()
    # int() 有去除空格的功能
    s1 = "20"
    s2 = "10.1"
    print(int(s1))  # 仅整型
    print(float(s1))
    print(float(s2))
    print(eval(s1))
    print(eval(s2))
    print(int("   5"), type(int("   5")))
    """*.example：整数加法计算器"""
    # 方法一
    content = input("请输入内容：").strip()  # 5+9 100 +99    22 + 34
    plus_index = content.find("+")
    num1 = content[:plus_index]  # '5'
    num2 = content[plus_index + 1 :]  # '9'
    result = int(num1) + int(num2)
    print(result)
    # 方法二
    content = input("请输入内容：").strip()
    num_list = content.split("+")
    result = int(num_list[0]) + int(num_list[1])
    print(result)

    # 　　int：函数用于将一个字符串或数字转换为整型。***
    print(int("123"))
    print(int(3.74))  # 取整 不是四舍五入
    print(int("0101", base=2))  # 将2进制的 0100 转化成十进制。结果为 4
    # 　　float：函数用于将整数和字符串转换成浮点数。 ***
    # print(type(3.14))
    # 　　　complex：函数用于创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。
    # 如果第一个参数为字符串，则不需要指定第二个参数。。


# =========================================  函数 - 阶乘 =========================================
#
# flag = True
flag = False
if flag:

    def sum1(n):
        s = 1
        for i in range(n, 0, -1):
            print(i)
            s *= i
        return s

    print(sum1(3))


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
    # 1
    def func4(l):
        if len(l) > 2:
            l1 = l[:2]
        else:
            l1 = l
        return l1

    # print(func4([1,]))

    # 2
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
# 写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
# 此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
# flag = True
flag = False
if flag:

    def func8(l):
        dic = {}
        for key, value in enumerate(l):
            dic[key] = value
        return dic

    print(func8([1, 2, 3]))


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
