# coding:utf-8

from flask import Blueprint


# 1. 创建蓝图对象
app_goods = Blueprint("goods", __name__)


# 2. 创建蓝图的视图函数
@app_goods.route("/get_goods")
def get_goods():
    return "get goods page"
