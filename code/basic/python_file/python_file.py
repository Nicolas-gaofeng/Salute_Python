#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@author     : zgf
@brief      : 文件操作
"""

# ========================================= 文件操作 =========================================
# 编码方式：utf-8,gbk,GB2312....
#    操作方式：只读，只写，写读，读写，追加 等。
#    报错原因：
#         UnicodeDecodeError: 'gb2312' codec can't decode byte 0xa6 in position 2: illegal multibyte sequence
#         编码不一致，存储文件时编码与打开文件时编码不一致。
#         r'd:\护士主妇空姐私密联系方式.txt'  路径问题
#         1，在路径的最前面，+ r
#         2，每个\ 变成 \\
#     绝对路径： d:\护士主妇空姐私密联系方式.txt 从根目录开始找
#     相对路径： 当前目录，当前文件夹。
# flag = True
flag = False
if flag:
    pass

# ========================================= 文件操作-读 =========================================
# 程序与文件在同一文件夹，可简化成文件名
# 打开模式
# "r"  只读模式，如文件不存在，报错
# "w" 覆盖写模式，如文件不存在，则创建；如文件存在，则完全覆盖原文件
# "x" 创建写模式，如文件不存在，则创建；如文件存在，报错
# "a"  追加写模式，如文件不存在，则创建；如文件存在，则在原文件后追加内容
# "b" 二进制文件模式，不能单独使用，需要配合使用如"rb"，"wb"，"ab"，该模式不需指定encoding
# "t" 文本文件模式，默认值，需配合使用 如"rt"，"wt"，"at"，一般省略，简写成如"r"，"w"，"a"
# "+"，与"r","w","x","a"配合使用，在原功能基础上，增加读写功能
# 打开模式缺省，默认为只读模式

# 字符编码
# 万国码 utf-8
# 包含全世界所有国家需要用到的字符
#
# 中文编码 gbk
# 专门解决中文编码问题
#
# windows系统下，如果缺省，则默认为gbk（所在区域的编码）
# 为清楚起见，除了处理二进制文件，建议不要缺省encoding

# 文件比较大时，read()和readlines()占用内存过大，不建议使用
# flag = True
flag = False
if flag:
    # r 对于r模式 mode可以默认不写
    # 全部读取
    f = open("README", encoding="GB2312", mode="r")
    content = f.read()
    print(content)
    f.close()
    with open("README", "r", encoding="utf") as f:
        for text in f:  # f本身就是一个可迭代对象，每次迭代读取一行内容
            print(text, end="")
            #
    f = open("README", encoding="utf-8", mode="r")
    content = f.read(10)  # r 模式，按照字符读取。
    print(content)
    f.close()
    """读取文件后文件指针会改变"""
    f = open("README", encoding="utf-8", mode="r")
    content = f.read()  # r 模式，按照字符读取。
    print(content)
    print(len(content))

    print("-" * 50)

    text = f.read()
    print(text)
    print(len(text))

    f.close()
    """逐行进行读取——f.readline()"""
    f = open("README", encoding="utf-8", mode="r")
    print(f.readline())  #
    print(f.readline())  #
    print(f.readline())  #
    print(f.readline())  #
    print(f.readline())  #
    print(f.readline())  #
    f.close()

    f = open("README", encoding="utf-8", mode="r")
    while True:
        text = f.readline()
        # 判断是否读取到内容
        if not text:
            break
        print(text, end="")  # 保留原文的换行，使print()的换行不起作用
    f.close()

    """按行读取，返回一个list"""
    f = open("README", encoding="utf-8", mode="r")
    content = f.readlines()
    print(content)
    f.close()

    with open("三国演义片头曲_gbk.txt", "r", encoding="gbk") as f:
        for text in f.readlines():
            print(text)  # 不想换行则用print(text, end="")
    #
    """  循环读取 """
    print("*" * 50)
    f = open("README", encoding="utf-8", mode="r")
    for line in f:
        print(line.strip())
    f.close()

    # rb 文件操作中凡是 带b字母，都是与非文字类文件相关的。
    f = open("美女1.jpg", mode="rb")
    content = f.read()
    print(content)
    f.close()

    f = open("文件操作1", mode="rb")
    content = f.read(9)  # rb 模式 n 按照字节读取。
    print(content)
    f.close()
    # r+ 读写：先读后追加。
    f = open("文件操作1", encoding="utf-8", mode="r+")
    content = f.read()
    print(content)
    f.write("666")
    f.close()

    f = open("文件操作1", encoding="utf-8", mode="r+")
    content = f.read(3)
    print(content)
    f.write("666")
    f.close()

    # 不读直接写会怎样：直接从开始覆盖
    f = open("文件操作1", encoding="utf-8", mode="r+")
    f.write("深圳你好")
    f.close()


# ========================================= 文件操作-写 =========================================
#  w
# 没有文件，创建文件也要写。
# 有文件，先清空，后写入。
# 如需换行，末尾加换行符\n
# flag = True
flag = False
if flag:
    """f.write()"""
    # 向文件写入一个字符串或字节流（二进制）——
    # 文件不存在则立刻创建一个
    # 如果文件存在，新写入内容会覆盖掉原内容，一定要注意！！！
    f = open("文件操作2", encoding="utf-8", mode="w")
    f.write("深圳市南山区，福田区，罗湖区。。。")
    f.close()

    # wb
    f = open("美女1.jpg", mode="rb")
    content = f.read()
    print(content)
    #
    f1 = open(" 美女2.jpg", mode="wb")
    f1.write(content)
    f.close()
    f1.close()

    # w+: 写读

    f = open("文件操作2", encoding="utf-8", mode="w+")
    f.write("深圳市南山区，福田区，罗湖区。。。")
    f.seek(3)  # 调整光标
    content = f.read()
    print(content)
    f.close()

    # 其他方法：writable
    f = open("文件操作1", encoding="utf-8")
    if f.writable():
        content = f.read()
        print(content)
    f.close()

    # tell 告知光标的位置  *****
    f = open("文件操作1", encoding="utf-8")
    f.seek(0, 2)  # 按照字节去移动光标
    print(f.tell())
    f.close()

    # truncate 要在writable模式下进行截取。
    # r+ a+ ..不能在w模式下使用，对原文件进行截取
    f = open("文件操作1", encoding="utf-8", mode="r+")
    print(f.truncate(6))
    f.close()


# ========================================= 文件操作-写 f.seek() =========================================
# seek 调整光标到开始，seek(0)  调整光标到结尾seek(0,2) *****
# flag = True
flag = False
if flag:

    f = open("文件操作1", encoding="utf-8")
    f.seek(6)  # 按照字节去移动光标
    content = f.read()
    print(content)
    f.close()

    f = open("文件操作1", mode="rb")
    print(f.read())
    f.seek(6)  # 按照字节去移动光标
    content = f.read()
    print(content)
    f.close()


# ========================================= 文件操作-写 a =========================================
"""追加 a"""
# 如果文件存在，新写入内容会覆盖掉原内容，一定要注意！！！
# 没有文件，创建文件也要写。
# 有文件,直接在文件的最后面追加。
# flag = True
flag = False
if flag:

    f = open("文件操作3", encoding="utf-8", mode="a")
    f.write("\n南方水土好。。。")
    f.close()


# ========================================= 文件操作-写 a+ =========================================
# 若文件不存在，则创建 指针在末尾，添加新内容，不会清空原内容
# flag = True
flag = False
if flag:
    with open("浪淘沙_北戴河.txt", "a+", encoding="gbk") as f:
        f.seek(0, 0)  # 指针移到开始
        print(f.read())  # 读取内容

    with open("浪淘沙_北戴河.txt", "a+", encoding="gbk") as f:
        text = ["萧瑟秋风今又是，\n", "换了人间。\n"]
        f.writelines(text)  # 指针在最后,追加新内容，
        f.seek(0, 0)  # 指针移到开始
        print(f.read())  # 读取内容


# ========================================= 文件操作-既读又写 r+ =========================================
"""r+"""
# 如果文件名不存在，则报错
# 指针在开始
# 要把指针移到末尾才能开始写，否则会覆盖前面内容
# flag = True
flag = False
if flag:
    with open("浪淘沙_北戴河.txt", "r+", encoding="gbk") as f:
        #     for line in f:
        #         print(line)   # 全部读一遍后，指针到达结尾
        f.seek(0, 2)  # 或者可以将指针移到末尾f.seek(偏移字节数,位置（0：开始；1：当前位置；2：结尾）)
        text = ["萧瑟秋风今又是，\n", "换了人间。\n"]
        f.writelines(text)


# ========================================= 文件操作-  w+ =========================================
"""w+"""
# 若文件不存在，则创建
# 若文件存在，会立刻清空原内容！！！
# flag = True
flag = False
if flag:
    with open("浪淘沙_北戴河.txt", "w+", encoding="gbk") as f:
        text = ["萧瑟秋风今又是，\n", "换了人间。\n"]  # 清空原内容
        f.writelines(text)  # 写入新内容，指针在最后
        f.seek(0, 0)  # 指针移到开始
        print(f.read())  # 读取内容

# ========================================= 文件操作-f.writelines() =========================================
#
# flag = True
flag = False
if flag:
    """将一个元素为字符串的列表整体写入文件——f.writelines()"""

    ls = ["春天刮着风", "秋天下着雨", "春风秋雨多少海誓山盟随风远去"]
    with open("恋曲1980.txt", "w", encoding="utf-8") as f:
        f.writelines(ls)
    ls = ["春天刮着风\n", "秋天下着雨\n", "春风秋雨多少海誓山盟随风远去\n"]
    with open("恋曲1980.txt", "w", encoding="utf-8") as f:
        f.writelines(ls)


# ========================================= 文件操作-json格式=========================================
# 常被用来存储字典类型
# 写入——dump()
# 读取——load()
# flag = True
flag = False
if flag:
    import json
    scores = {"Petter": {"math": 96, "physics": 98},
              "Paul": {"math": 92, "physics": 99},
              "Mary": {"math": 98, "physics": 97}}
    with open("score.json", "w", encoding="utf-8") as f:  # 写入整个对象
        # indent 表示字符串换行+缩进 ensure_ascii=False 显示中文
        json.dump(scores, f, indent=4, ensure_ascii=False)

    with open("score.json", "r", encoding="utf-8") as f:
        scores = json.load(f)  # 加载整个对象
        for k, v in scores.items():
            print(k, v)


    # ========================================= 文件操作-复制文件 =========================================
#
# flag = True
flag = False
if flag:
    # 1. 打开
    file_read = open("README")
    file_write = open("REAMDE[复件]", "w")
    # 2. 读、写
    text = file_read.read()
    file_write.write(text)
    # 3. 关闭
    file_read.close()
    file_write.close()

    """复制大文件"""
    # 1. 打开
    file_read = open("README")
    file_write = open("REAMDE[复件]", "w")
    # 2. 读、写
    while True:
        # 读取一行内容
        text = file_read.readline()
        # 判断是否读取到内容
        if not text:
            break
        file_write.write(text)
    # 3. 关闭
    file_read.close()
    file_write.close()

# ========================================= 文件操作-主动关闭文件句柄 =========================================
#   """with 打开文件"""
# with open("文件路径", "打开模式", encoding="操作文件的字符编码") as f:
#     "对文件进行相应的读写操作"
# 使用with 块的好处：执行完毕后，自动对文件进行close操作。
# flag = True
flag = False
if flag:

    # 1，主动关闭文件句柄
    with open("文件操作2", encoding="utf-8") as f1:
        print(f1.read())
    # 2，开启多个文件句柄。
    with open("文件操作2", encoding="utf-8") as f1, open(
        "文件操作3", encoding="utf-8", mode="w"
    ) as f2:
        print(f1.read())
        f2.write("666666")
