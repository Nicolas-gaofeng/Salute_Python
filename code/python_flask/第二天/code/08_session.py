# coding:utf-8

from flask import Flask, session, current_app


app = Flask(__name__)

# flask的session需要用到的秘钥字符串
app.config["SECRET_KEY"] = "dhsodfhisfhosdhf29fy989"


# flask默认把session保存到了cookie中

@app.route("/login")
def login():
    # 设置session数据
    session["name"] = "python"
    session["mobile"] = "18611111111"
    return "login success"


@app.route("/index")
def index():
    # 获取session数据
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(debug=True)

