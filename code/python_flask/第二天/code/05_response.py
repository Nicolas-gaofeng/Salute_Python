# coding:utf-8

from flask import Flask, request, abort, Response, make_response


app = Flask(__name__)


@app.route("/index")
def index():
    # 1 使用元祖，返回自定义的响应信息
    #        响应体       状态码 响应头
    # return "index page", 400, [("Itcast", "pyton"), ("City", "shenzhen")]
    # return "index page", 400, {"Itcast1": "python1", "City1": "sz1"}
    # return "index page", 666, {"Itcast1": "python1", "City1": "sz1"}
    # return "index page", "666 itcast status", {"Itcast1": "python1", "City1": "sz1"}
    # return "index page", "666 itcast status"

    # 2 使用make_response 来构造响应信息
    resp = make_response("index page 2")
    resp.status = "999 itcast"  # 设置状态码
    resp.headers["city"] = "sz"  # 设置响应头
    return resp


if __name__ == '__main__':
    app.run(debug=True)
