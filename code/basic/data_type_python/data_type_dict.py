#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : data_type_dict.py
@author     : zgf
@brief      : 数据类型- dict
@attention  : life is short,I need python
"""


# =========================================  组合类型：字典（dict）-创建 =========================================
# 字典是可变类型
# 字典的键不能重复，字典的key只能用不可变类型，我们一般使用字符串，字典是一个可变类型。
# 1.不可变类型：数字、字符串、元组。 一旦确定，它自己就是它自己，变了就不是它了。
# 2.可变类型：列表、字典、集合。一旦确定，还可以随意增删改。
# 多个元素用逗号分割，每个元素按照key:value的形式，通过键-值的映射实现数据存储和查找
# 字典是一个无序的数据集合，使用print函数输出字典时，通常输出的顺序和定义的顺序是不一致的！python3.6之后，字典是有序的，

# 字典的底层实现
# 通过稀疏数组来实现值的存储与访问
# 字典的创建过程
# 第一步：创建一个散列表（稀疏数组 N >> n）第一步：通过hash()计算键的散列值
# 第二步：根据计算的散列值确定其在散列表中的位置 # 极个别时候，散列值会发生冲突，则内部有相应的解决冲突的办法
# 第三步：在该位置上存入值
# fromkeys()
# setdefault()
# updata()
# flag = True
flag = False
if flag:
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


# =========================================  组合类型：字典（dict）- 取值 =========================================
# 键值对的访问过程
# 第一步：计算要访问的键的散列值
# 第二步：根据计算的散列值，通过一定的规则，确定其在散列表中的位置
# 第三步：读取该位置上存储的值 如果存在，则返回该值 如果不存在，则报错KeyError
# flag = True
flag = False
if flag:
    """*.字典的取值"""
    print("[键]".center(50, "*"))
    # 字典的索引--通过字典[键]的形式来获取对应的值
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    print(students[201902])
    # 在取值的时候，如果指定的key不存在，程序会报错！

    # 变换迭代
    print("变换迭代".center(50, "*"))
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    # d.keys( ) d.values( )方法
    print("d.keys( ) ".center(50, "*"))
    print(list(students.keys()))
    for student in students.keys():
        print(student)
    print("d.values( ) ".center(50, "*"))
    print(list(students.values()))
    print("d.items( ) ".center(50, "*"))
    # d.items( )方法及字典的遍历
    print(list(students.items()))
    for k, v in students.items():
        print(k, v)

    """字典的查找操作"""
    print("d.get( ) ".center(50, "*"))
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
    print("len()".center(50, "*"))
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    print(len(students))


# =========================================  组合类型：字典（dict）- 删除 =========================================
# del
# clear()
# pop()
# popitem()
# flag = True
flag = False
if flag:
    """*.字典的删除键值对"""
    print("del ".center(50, "*"))
    # 再循环一个字典时，不能改变字典的大小
    # 通过del 变量名[待删除键]
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    del students[201903]
    print(students)

    # 通过变量名.pop(待删除键)
    print("pop()".center(50, "*"))
    # 在删除指定键值对的时候，如果指定的key不存在，程序会报错！
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    value = students.pop(201903)  # 删除键值对，同时获得删除键值对的值
    print(value)
    print(students)

    print("popitem()".center(50, "*"))
    # 变量名.popitem()随机删除一个键值对，并以元组返回删除键值对
    # python3.6之后字典是有序的，默认删除最后一个
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    key, value = students.popitem()
    print(key, value)
    print(students)

    print("clear()".center(50, "*"))
    # clear() 清空字典
    students.clear()
    print(students)


# =========================================  组合类型：字典（dict） - 修改 =========================================
# 字典的增加键值对 -- 变量名[新键] = 新值
# flag = True
flag = False
if flag:
    # 通过先索引后赋值的方式对相应的值进行修改
    # 如果key不存在，会新增键值对
    # 如果key存在，会修改已经存在的键值对
    students = {201901: "小明", 201902: "小红", 201903: "小强"}
    students[201902] = "小雪"
    print(students)

    print("setdefault()".center(50, "*"))
    # dic.setdefault() 有则不变，无责增加
    students.setdefault(201905, "新增小雪")
    print(students)

    # updata() 合并字典
    print("updata()".center(50, "*"))
    xiaoming_dict = {"name": "小明", "age": 18}
    temp_dict = {"height": 1.75, "age": 20}
    # 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
    xiaoming_dict.update(temp_dict)
    print(xiaoming_dict)


# =========================================  字典 - 快速查找 =========================================
# 字典的 快速查找
flag = True
# flag = False
if flag:
    import time

    # 列表方式
    print("列表方式".center(50, "*"))
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
    print("字典方式".center(50, "*"))
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


# =========================================   字典练习  =========================================
# 字典遍历
#
# flag = True
flag = False
if flag:
    # example1
    students = [{"name": "阿土"}, {"name": "小美"}]
    # 在学员列表中搜索指定的姓名
    find_name = "张三"
    for stu_dict in students:
        print(stu_dict)
        if stu_dict["name"] == find_name:
            print("找到了　%s" % find_name)
            # 如果已经找到，应该直接退出循环，而不再遍历后续的元素
            break
        # else:
        #     print("抱歉没有找到　%s" % find_name)
    else:
        # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
        # 还希望得到一个统一的提示！
        print("抱歉没有找到　%s" % find_name)
    print("循环结束")

    # example2
    xiaoming_dict = {"name": "小明", "qq": "123456", "phone": "10086"}
    # 迭代遍历字典
    # 变量k是每一次循环中，获取到的键值对的key
    for k in xiaoming_dict:
        print("%s - %s" % (k, xiaoming_dict[k]))

        # example3
        # 使用 多个键值对，存储 描述一个 物体 的相关信息 —— 描述更复杂的数据信息
        # 将 多个字典 放在 一个列表 中，再进行遍历
        card_list = [
            {"name": "张三", "qq": "12345", "phone": "110"},
            {"name": "李四", "qq": "54321", "phone": "10086"},
        ]
        for card_info in card_list:
            print(card_info)


# =========================================  字典转换 =========================================
#  list3 = [
#     {"name": "alex", "hobby": "抽烟"},
#     {"name": "alex", "hobby": "喝酒"},
#     {"name": "alex", "hobby": "烫头"},
#     {"name": "alex", "hobby": "Massage"},
#     {"name": "wusir", "hobby": "喊麦"},
#     {"name": "wusir", "hobby": "街舞"},
#     {"name": "wusir", "hobby": "唱歌"},
#     {"name": "太白", "hobby": "开车"},
# ]
# list4 = [
#     {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
#     {"name": "wusir", "hobby_list": ["喊麦", "街舞"]},
# ]
# # 将list3 这种数据类型转化成list4类型,你写的代码必须支持可拓展,
# # 比如list3 数据在加一个这样的字典{"name": "wusir", "hobby": "溜达"},
# 你的list4{"name": "wusir", "hobby_list": ["喊麦", "街舞", "溜达"],
# # 或者list3增加一个字典{"name": "太白", "hobby": "开车"},
# # 你的list4{"name": "太白", "hobby_list": ["开车"],
flag = True
# flag = False
if flag:
    list3 = [
        {"name": "alex", "hobby": "抽烟"},
        {"name": "alex", "hobby": "喝酒"},
        {"name": "alex", "hobby": "烫头"},
        {"name": "alex", "hobby": "Massage"},
        {"name": "wusir", "hobby": "喊麦"},
        {"name": "wusir", "hobby": "街舞"},
        {"name": "wusir", "hobby": "唱歌"},
        {"name": "太白", "hobby": "开车"},
    ]
    dic = {}
    for i in list3:
        if i["name"] not in dic:
            dic[i["name"]] = {
                "name": i["name"],
                "hobby_list": [
                    i["hobby"],
                ],
            }
        else:
            dic[i["name"]]["hobby_list"].append(i["hobby"])
    print(list(dic.values()))
