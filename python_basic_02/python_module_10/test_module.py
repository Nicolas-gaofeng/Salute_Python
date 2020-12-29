#!/usz/bin/env python
# -*- coding:utf-8 -*-

"""
@file       : test_module.py
@author     : zgf
@brief      : 模块
@attention  : life is short,I need python
"""


# ========================================= 模块 =========================================
# 模块1
# 文件夹内多个py文件，再加一个__init__.py文件（内容可为空）
# 已经被封装好 无需自己再“造轮子” 声明导入后，拿来即用
# 广义模块分类
# 1、Python 内置
#  时间库time\  随机库random\  容器数据类型collection\  迭代器函数itertools
# 2、第三方库
#  数据分析numpy、pandas\  数据可视化matplotlib\  机器学习scikit-learn\  深度学习Tensorflow
# 3、自定义文件
# 单独py文件
# 包——多个py文件
# 导入整个模块——import 模块名  --调用方式：模块名.函数名或类名
# flag = True
flag = False
if flag:
    import test_module_3

    test_module_3.print_line("-", 50)
    print(test_module_3.name)


# ========================================= 模块 =========================================
# 模块2
# flag = True
flag = False
if flag:
    import test_module_1
    import test_module_2

    test_module_1.say_hello()
    test_module_2.say_hello()
    dog = test_module_1.Dog()
    print(dog)
    cat = test_module_2.Cat()
    print(cat)


# ========================================= 模块 =========================================
#  import同时指定别名
# flag = True
flag = False
if flag:
    import test_module_1 as DogModule
    import test_module_2 as CatModule

    DogModule.say_hello()
    CatModule.say_hello()

    dog = DogModule.Dog()
    print(dog)

    cat = CatModule.Cat()
    print(cat)


# ========================================= 模块 from_import导入 =========================================
# 从模块中导入类或函数——from 模块 import 类名或函数名 -- 调用方式：函数名或类名
# flag = True
flag = False
if flag:
    from test_module_1 import Dog
    from test_module_2 import say_hello

    say_hello()

    wangcai = Dog()
    print(wangcai)

    """# 注意事项"""
    # from test_module_1 import say_hello
    from test_module_2 import say_hello as module2_say_hello
    from test_module_1 import say_hello

    say_hello()
    module2_say_hello()

    """导入全部"""
    print("import * 导入全部".center(50, "*"))
    # 导入模块中所有的类和函数——from 模块 import *
    # 调用方式：函数名或类名
    from test_module_1 import *
    from test_module_2 import *

    print(title)
    say_hello()
    wangcai = Dog()
    print(wangcai)


# ========================================= 模块  模块的查找路径  =========================================
# 模块搜索查找顺序：
# flag = True
flag = False
if flag:
    # 1、内存中已经加载的模块
    # 2、内置模块
    # Python 启动时，解释器会默认加载一些 modules 存放在sys.modules中
    # sys.modules 变量包含一个由当前载入(完整且成功导入)到解释器的模块组成的字典, 模块名作为键, 它们的位置作为值
    import sys

    print(len(sys.modules))
    print("math" in sys.modules)
    print("numpy" in sys.modules)
    for k, v in list(sys.modules.items())[:20]:
        print(k, ":", v)
    # 3、sys.path路径中包含的模块
    # sys.path的第一个路径是当前执行文件所在的文件夹
    # 若需将不在该文件夹内的模块导入，需要将模块的路径添加到sys.path
    import sys
    print(sys.path)


# ========================================= 模块 __name__  =========================================
# 全局变量、函数、类，注意：直接执行的代码不是向外界提供的工具！
# flag = True
flag = False
if flag:
    def say_hello():
        print("你好你好，我是 say hello")

    # 如果直接执行模块，__main__
    if __name__ == "__main__":
        print(__name__)

        # 文件被导入时，能够直接执行的代码不需要被执行！
        print("小明开发的模块")
        say_hello()
