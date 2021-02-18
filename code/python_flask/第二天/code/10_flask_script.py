# coding:utf-8

from flask import Flask
from flask_script import Manager   # 启动命令的管理类


app = Flask(__name__)

# 创建Manager管理类的对象
manager = Manager(app)


@app.route("/index")
def index():
    return "index page"


if __name__ == '__main__':
    # app.run(debug=True)
    # 通过管理对象来启动flask
    manager.run()
