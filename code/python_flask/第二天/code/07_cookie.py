# coding:utf-8

from flask import Flask, make_response, request


app = Flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    # 设置cookie, 默认有效期是临时cookie，浏览器关闭就失效
    resp.set_cookie("Itcast", "Python")
    resp.set_cookie("Itcast1", "Python1")
    # max_age设置有效期，单位：秒
    resp.set_cookie("Itcast2", "Python1", max_age=3600)
    resp.headers["Set-Cookie"] = "Itcast3=Python3; Expires=Sat, 18-Nov-2017 04:36:04 GMT; Max-Age=3600; Path=/"
    return resp


@app.route("/get_cookie")
def get_cookie():
    c = request.cookies.get("Itcast")
    return c


@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("del success")
    # 删除cookie
    resp.delete_cookie("Itcast1")
    return resp


if __name__ == '__main__':
    app.run(debug=True)

