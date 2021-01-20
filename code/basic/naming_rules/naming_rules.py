#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : naming_rules.py
@author     : zgf
@brief      : python命名规则
@attention  : life is short,I need python
"""

# =========================================  文件命名说明 =========================================
# a. 命名文件名时建议只使用 小写字母、数字 和 下划线
# b. 文件名不能以数字开始
# flag = True
flag = False
if flag:
    pass


# =========================================  类命名说明 =========================================
# 驼峰体（推荐：类名） 变量名由多个单词组成：单词首字母大写
# 单词与单词之间没有下划线
# flag = True
flag = False
if flag:

    class AgeOfStudent:
        def func(self, i):
            pass


# =========================================  变量命名说明 =========================================
# 变量名 = 值  : 等号（=）用来给变量赋值 （=）左边是一个变量名 （=）右边是存储在变量中的值
# 变量定义之后，后续就可以直接使用了
# 变量名只能是字母/数字或下划线的任意组合，并严格区分大小写
# 变量名的第一个字符不能是数字; 变量名中间不能有空格;  关键字不能作为变量
# flag = True
flag = False
if flag:
    python_is_第一名 = True
    set_student = "张三"  # 命名1：下划线命名法 变量名由多个单词组成：用_连接多个单词
    list_teacher = "李四"  # 变量名尽可能有实际意义，表征数据的某种特性
    AgeOfStudent = [17, 18, 19]  # 命名2：驼峰体（推荐：类名） 变量名由多个单词组成：单词首字母大写
    print(AgeOfStudent)
    print(python_is_第一名)  # 尽量避免用中文和拼音做变量名
    print(set_student)
    print(list_teacher)
    # 全局变量命名
    gl_num = 10
    gl_title = "黑马程序员"
    gl_name = "小明"

    def demo():
        # 如果局部变量的名字和全局变量的名字相同
        # pycharm会在局部变量下方显示一个灰色的虚线
        num = 99
        print("%d" % num)
        print("%s" % gl_title)
        print("%s" % gl_name)

    demo()


# =========================================  模块命名说明 =========================================
# 与包的规范同。如mymodule。
# 单词与单词之间没有下划线
# flag = True
flag = False
if flag:
    import 模块名1 as 模块别名


# =========================================  包命名说明 =========================================
# 命名方式 和变量名一致，小写字母 + _
# 应该是简短的、小写的名字。如果下划线可以改善可读性可以加入。如mypackage。
# flag = True
flag = False
if flag:
    pass


# =========================================  函数命名说明 =========================================
# 函数名应该为小写，可以用下划线风格单词以增加可读性。如：myfunction，my_example_function。
# flag = True
flag = False
if flag:

    def myfunction():
        pass

    myfunction()


# =========================================  常量命名说明 =========================================
# 常量即不变的量 如π、e
# 全部用大写字母表示
# 一般放在文件最上面
# flag = True
flag = False
if flag:
    PI = 3.1415926
    MAX_ITERATION = 1000
    print(PI)
    print(MAX_ITERATION)
