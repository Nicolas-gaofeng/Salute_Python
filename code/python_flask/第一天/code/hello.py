# coding:utf-8

from flask import Flask, current_app
# import demo

# 创建flask的应用对象
# __name__表示当前的模块名字
#           模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__,
            static_url_path="/python",  # 访问静态资源的url前缀, 默认值是static
            static_folder="static",  # 静态文件的目录，默认就是static
            template_folder="templates",  # 模板文件的目录，默认是templates
            )
# app = Flask("__main__")
# app = Flask("abcdefg")

# 配置参数的使用方式
# 1. 使用配置文件
# app.config.from_pyfile("config.cfg")

# 2. 使用对象配置参数
class Config(object):
    DEBUG = True
    ITCAST = "python"


app.config.from_object(Config)

# # 3. 直接操作config的字典对象
# app.config["DEBUG"] = True


@app.route("/")
def index():
    """定义的视图函数"""
    # a = 1 / 0
    # 读取配置参数
    # 1. 直接从全局对象app的config字典中取值
    # print(app.config.get("ITCAST"))
    # 2. 通过current_app获取参数
    print(current_app.config.get("ITCAST"))

    return "hello flask"


if __name__ == '__main__':
    # 启动flask程序
    # app.run()
    app.run(host="0.0.0.0", port=5000, debug=True)