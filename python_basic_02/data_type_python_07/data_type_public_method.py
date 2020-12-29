#!/usz/bin/env python
# -*- coding:utf-8 -*-


"""
@file       : data_type_public_method.py
@author     : zgf
@brief      : 容器公共方法
@attention  : life is short,I need python
"""


# =========================================  遍历 for -else =========================================
# 要判断某一个字典中是否存在指定的值
# - 如果存在，提示并且退出循环
# - 如果不存在，在循环整体结束后，希望得到一个统一的提示
# flag = True
flag = False
if flag:
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
