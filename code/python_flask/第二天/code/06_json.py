# coding:utf-8

from flask import Flask, jsonify
import json


app = Flask(__name__)


@app.route("/index")
def index():
    # json就是字符串
    data = {
        "name": "python",
        "age": 24
    }
    # # json.dumps(字典）  将python的字典转换为json字符串
    # # json.loads(字符串）  将字符串转换为python中的字典
    #
    # json_str = json.dumps(data)
    #
    # return json_str, 200, {"Content-Type": "application/json"}

    # jsonify帮助转为json数据，并设置响应头 Content-Type 为application/json
    # return jsonify(data)

    return jsonify(city="sz", country="china")


if __name__ == '__main__':
    app.run(debug=True)

