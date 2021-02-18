# coding:utf-8

from flask import Flask, render_template, flash


app = Flask(__name__)

flag = True

app.config["SECRET_KEY"] = "SDHFOSDF"


@app.route("/")
def index():

    if flag:
        # 添加闪现信息
        flash("hello1")
        flash("hello2")
        flash("hello3")
        global flag
        flag = False

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
