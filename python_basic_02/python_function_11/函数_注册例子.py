# -*- coding: utf-8 -*-

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


def register():
    while 1:
        username = input('请输入用户名:').strip()
        with open('register', encoding='utf-8',) as f1:
            for line in f1:
               uname,pwd = line.strip().split('|')  # [诸葛,123]
               if username == uname:
                   print('此用户名已存在，请重新输入')
                   break
            else:
                password = input('请输入密码:').strip()
                with open('register', encoding='utf-8', mode='a') as f2:
                    f2.write('\n{}|{}'.format(username,password))
                    return True
register()
