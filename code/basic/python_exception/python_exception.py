#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@author     : zgf
@brief      : 异常
"""

# ========================================= 异常 =========================================
# 简单的异常捕获
# 当异常发生的时候，如果不预先设定处理方法，程序就会中断
# try_except提高程序的稳定性和可靠性
# 如果try内代码块顺利执行，except不被触发
# 如果try内代码块发生错误，触发except,执行except内代码块
# flag = True
flag = False
if flag:
    try:
        # 不能确定正确执行的代码
        num = int(input("请输入一个整数："))
    except:
        # 错误的处理代码
        print("请输入正确的整数")

    print("-" * 50)


# ========================================= 异常 =========================================
# 捕获错误类型
# 除0运算——ZeroDivisionError
# 值错误——ValueError
# 找不到可读文件——FileNotFoundError
# 索引错误——IndexError  下标超出序列边界
# 类型错误——TypeError 传入对象类型与要求不符
# NameError 使用一个未被定义的变量
# KeyError 试图访问字典里不存在的键
# flag = True
flag = False
if flag:
    try:
        # 提示用户输入一个整数
        num = int(input("输入一个整数："))

        # 使用 8 除以用户输入的整数并且输出
        result = 8 / num

        print(result)
    except ZeroDivisionError:
        print("除0错误")
    except ValueError:
        print("请输入正确的整数")


# ========================================= 异常 =========================================
# 捕获未知错误类型
# 传入一个调用者不期望的值，即使这个值的类型是正确的
# flag = True
flag = False
if flag:
    try:
        # 提示用户输入一个整数
        num = int(input("输入一个整数："))

        # 使用 8 除以用户输入的整数并且输出
        result = 8 / num

        print(result)
    except ValueError:
        print("请输入正确的整数")
    except Exception as result:
        print("未知错误 %s" % result)


# ========================================= 异常 =========================================
# 完整的异常语法
# try_except_else
# 如果try 模块执行，则else模块也执行
# 可以将else 看做try成功的额外奖赏
# 不论try模块是否执行，finally最后都执行
# flag = True
flag = False
if flag:
    try:
        # 提示用户输入一个整数
        num = int(input("输入一个整数："))

        # 使用 8 除以用户输入的整数并且输出
        result = 8 / num

        print(result)
    except ValueError:
        print("请输入正确的整数")
    except Exception as result:
        print("未知错误 %s" % result)
    else:
        print("尝试成功")
    finally:
        print("无论是否出现错误都会执行的代码")

    print("-" * 50)


# ========================================= 异常 =========================================
# 异常的传递
# flag = True
flag = False
if flag:
    def demo1():
        return int(input("输入整数："))


    def demo2():
        return demo1()


    # 利用异常的传递性，在主程序捕获异常
    try:
        print(demo2())
    except Exception as result:
        print("未知错误 %s" % result)


# ========================================= 异常 =========================================
# 抛出异常
# flag = True
flag = False
if flag:
    def input_password():

        # 1. 提示用户输入密码
        pwd = input("请输入密码：")

        # 2. 判断密码长度 >= 8，返回用户输入的密码
        if len(pwd) >= 8:
            return pwd

        # 3. 如果 < 8 主动抛出异常
        print("主动抛出异常")
        # 1> 创建异常对象 - 可以使用错误信息字符串作为参数
        ex = Exception("密码长度不够")

        # 2> 主动抛出异常
        raise ex


    # 提示用户输入密码
    try:
        print(input_password())
    except Exception as result:
        print(result)
