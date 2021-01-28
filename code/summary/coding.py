#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : coding.py
@author     : zgf
@brief      : python编码
@attention  : life is short,I need python
"""


# =========================================  字符编码 - str和bytes类型相互转换工具类 =========================================
# python3,str和bytes类型相互转换工具类
# gbk的bytes utf-8的bytes---> 英文字母、数字、特殊字符可以互相转化，他们引用的都是ascii
# flag = True
flag = False
if flag:

    def to_str_utf8(bytes_or_str):
        """
        str --- > bytes : encode 编码
        """
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode("UTF-8")
        else:
            value = bytes_or_str
        return value

    def to_str_gbk(bytes_or_str):
        """
        str --- > bytes : encode 编码
        """
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode("gbk")
        else:
            value = bytes_or_str
        return value

    def to_bytes_utf8(bytes_or_str):
        """
        bytes ---> str : decode 解码
        """
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode("UTF-8")
        else:
            value = bytes_or_str
        return value

    def to_bytes_gbk(bytes_or_str):
        """
        bytes ---> str : decode 解码
        """
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode("gbk")
        else:
            value = bytes_or_str
        return value

    str_string = u"中国"
    value = to_bytes_utf8(str_string)
    print(type(value))  # <class 'bytes'>
    value1 = to_bytes_gbk(str_string)
    print(type(value1))  # <class 'bytes'>
    value = to_str_utf8(value)
    print(type(value))  # <class 'str'>
    value = to_str_gbk(value1)
    print(type(value))  # <class 'str'>


# =========================================  字符编码 =========================================
# 将中文字库，英文字母、数字、特殊字符等转化成计算机可识别的二进制数
# 每个单一字符对应一个唯一的互不重复的二进制编码
# Python 中使用的是Unicode编码
# 你想将一部分内容（字符串）写入文件，或者通过网络socket传输，这样这部分内容（字符串）必须转化成bytes才可以进行
# 平时你代码中，使用字符串。
flag = True
# flag = False
if flag:
    """ord(字符)"""
    # 输入字符找该字符编码 unicode  的位置(将字符转化为Unicode码)
    print(ord("1"))
    print(ord("a"))
    print(ord("*"))
    print(ord("中"))
    print(ord("国"))

    """chr(Unicode码)"""
    # 输入位置数字找出其对应的字符（将Unicode码转化为字符） unicode
    print(chr(97))
    print(chr(20013))
    print(chr(1010))
    print(chr(10000))
    print(chr(12345))
    print(chr(23456))

    """ascii(字符)"""
    # ascii:是ascii码中的返回该值，不是则返回他在unicode的位置（16进制。）
    print(ascii("a"))
    print(ascii("中"))  # '\u4e2d'
