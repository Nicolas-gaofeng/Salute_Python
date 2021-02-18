# coding:utf-8

from flask import Flask, current_app, redirect, url_for
# import demo

# 创建flask的应用对象
# __name__表示当前的模块名字
#           模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)


@app.route("/index")
def index():
    """定义的视图函数"""
    return "hello flask"


# 通过methods限定访问方式
@app.route("/post_only", methods=["GET", "POST"])
def post_only():
    return "post only page"


@app.route("/hello", methods=["POST"])
def hello():
    return "hello 1"


@app.route("/hello", methods=["GET"])
def hello2():
    return "hello 2"


@app.route("/hi1")
@app.route("/hi2")
def hi():
    return "hi page"


@app.route("/login")
def login():
    # url = "/"
    # 使用url_for的函数，通过视图函数的名字找到视图对应的url路径
    url = url_for("index")

    return redirect(url)


@app.route("/register")
def register():
    # url = "/"
    url = url_for("index")
    return redirect(url)


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    # 启动flask程序
    app.run(debug=True)