## 1. mini-web框架-路由支持正则

```python
import pymysql
import time
import os
import re

template_root = "./templates"

# 用来存放url路由映射
# url_route = {
#   "/index.py":index_func,
#   "/center.py":center_func
# }
g_url_route = dict()


def route(url):
    def func1(func):
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        g_url_route[url]=func
        def func2(file_name):
            return func(file_name)
        return func2
    return func1

@route(r"/index.html")
def index(file_name, url=None):
    """返回index.html需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        # data_from_mysql = "暂时没有数据，请等待学习mysql吧，学习完mysql之后，这里就可以放入mysql查询到的数据了"
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select * from info;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        html_template = """
            <tr>
                <td>%d</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                </td>
                </tr>"""

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[1])


        content = re.sub(r"\{%content%\}", html, content)

        return content


@route(r"/center.html")
def center(file_name, url=None):
    """返回center.html需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        # data_from_mysql = "暂时没有数据,,,,~~~~(>_<)~~~~ "
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,j.note_info from info as i inner join focus as j on i.id=j.info_id;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        html_template = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                </td>
            </tr>
            """

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[0], info[0])

        content = re.sub(r"\{%content%\}", html, content)

        return content


# ------- 添加 -------
@route(r"/update/(\d*)\.html")
def update(file_name, url):
    """显示 更新页面的内容"""
    try:
        template_file_name = template_root + "/update.html"
        f = open(template_file_name)
    except Exception as ret:
        return "%s,,,没有找到%s" % (ret, template_file_name)
    else:
        content = f.read()
        f.close()

        ret = re.match(url, file_name)
        if ret:
            stock_code = ret.group(1)

        # 将提取到的股票编码返回到浏览器中,以检查是否能够正确的提取url的数据
        return stock_code


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    try:
        for url, call_func in g_url_route.items():
            print(url)
            ret = re.match(url, file_name)
            if ret:
                return call_func(file_name, url)
                break
        else:
            return "没有访问的页面--->%s" % file_name

    except Exception as ret:
        return "%s" % ret

    else:
        return str(environ) + '-----404--->%s\n'
```

## 2. mini-web框架-mysql-增

my_web.py(修改)

```python
import pymysql
import time
import os
import re
import sys
from urllib.parse import unquote

template_root = "./templates"

# 用来存放url路由映射
# url_route = {
#   "/index.py":index_func,
#   "/center.py":center_func
# }
g_url_route = dict()


def route(url):
    def func1(func):
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        g_url_route[url]=func
        def func2(file_name):
            return func(file_name)
        return func2
    return func1


@route(r"/index.html")
def index(file_name, url=None):
    """返回index.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        # data_from_mysql = "暂时没有数据，请等待学习mysql吧，学习完mysql之后，这里就可以放入mysql查询到的数据了"
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select * from info;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        html_template = """
            <tr>
                <td>%d</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                </td>
                </tr>"""

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[1])


        content = re.sub(r"\{%content%\}", html, content)

        return content


@route(r"/center.html")
def center(file_name, url=None):
    """返回center.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        # data_from_mysql = "暂时没有数据,,,,~~~~(>_<)~~~~ "
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,j.note_info from info as i inner join focus as j on i.id=j.info_id;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        html_template = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                </td>
            </tr>
            """

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[0], info[0])

        content = re.sub(r"\{%content%\}", html, content)

        return content


@route(r"/update/(\d*)\.html")
def update(file_name, url):
    """显示 更新页面的内容"""
    try:
        template_file_name = template_root + "/update.html"
        f = open(template_file_name)
    except Exception as ret:
        return "%s,,,没有找到%s" % (ret, template_file_name)
    else:
        content = f.read()
        f.close()

        ret = re.match(url, file_name)
        if ret:
            stock_code = ret.group(1)
        else:
            stock_code = 0

        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        # 会出现sql注入，怎样修改呢？ 参数化
        sql = """select focus.note_info from focus inner join info on focus.info_id=info.id where info.code=%s;""" % stock_code
        cursor.execute(sql)
        stock_note_info = cursor.fetchone()
        cursor.close()
        db.close()

        content = re.sub(r"\{%code%\}", stock_code, content)
        content = re.sub(r"\{%note_info%\}", str(stock_note_info[0]), content)

        return content


@route(r"/update/(\d*)/(.*)\.html")
def update_note_info(file_name, url):
    """进行数据的真正更新"""
    stock_code = 0
    stock_note_info = ""

    ret = re.match(url, file_name)
    if ret:
        stock_code = ret.group(1)
        stock_note_info = ret.group(2)
        stock_note_info = unquote(stock_note_info)

    db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cursor = db.cursor()
    # 会出现sql注入，怎样修改呢？ 参数化
    sql = """update focus inner join info on focus.info_id=info.id set focus.note_info="%s" where info.code=%s;""" % (stock_note_info, stock_code)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    return "修改成功"


# ------ 添加 -------
@route(r"/add/(\d*)\.html")
def add(file_name, url):
    """添加关注"""

    stock_code = 0

    ret = re.match(url, file_name)
    if ret:
        stock_code = ret.group(1)

    db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cursor = db.cursor()

    # 判断是否已经关注
    sql = """select * from focus inner join info on focus.info_id=info.id where info.code=%s;""" % (stock_code)
    cursor.execute(sql)
    if cursor.fetchone():
        cursor.close()
        db.close()
        return "已经关注过了，请不要重复关注"

    # 如果没有关注，那么就进行关注
    sql = """insert into focus (info_id) select id from info where code="%s";""" % (stock_code)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    return "关注成功"


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    try:
        for url, call_func in g_url_route.items():
            print(url)
            ret = re.match(url, file_name)
            if ret:
                return call_func(file_name, url)
                break

        else:
            return "没有访问的页面--->%s" % file_name

    except Exception as ret:
        return "%s" % ret

    else:
        return str(environ) + '-----404--->%s\n'
```

## 3. mini-web框架-mysql-删

my_web.py(修改)

```python
import pymysql
import time
import os
import re
import sys
from urllib.parse import unquote

template_root = "./templates"

# 用来存放url路由映射
# url_route = {
#   "/index.py":index_func,
#   "/center.py":center_func
# }
g_url_route = dict()


def route(url):
    def func1(func):
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        g_url_route[url]=func
        def func2(file_name):
            return func(file_name)
        return func2
    return func1


@route(r"/index.html")
def index(file_name, url=None):
    """返回index.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        # data_from_mysql = "暂时没有数据，请等待学习mysql吧，学习完mysql之后，这里就可以放入mysql查询到的数据了"
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select * from info;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        html_template = """
            <tr>
                <td>%d</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                </td>
                </tr>"""

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[1])


        content = re.sub(r"\{%content%\}", html, content)

        return content


@route(r"/center.html")
def center(file_name, url=None):
    """返回center.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        # data_from_mysql = "暂时没有数据,,,,~~~~(>_<)~~~~ "
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,j.note_info from info as i inner join focus as j on i.id=j.info_id;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        html_template = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                </td>
            </tr>
            """

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[0], info[0])

        content = re.sub(r"\{%content%\}", html, content)

        return content


@route(r"/update/(\d*)\.html")
def update(file_name, url):
    """显示 更新页面的内容"""
    try:
        template_file_name = template_root + "/update.html"
        f = open(template_file_name)
    except Exception as ret:
        return "%s,,,没有找到%s" % (ret, template_file_name)
    else:
        content = f.read()
        f.close()

        ret = re.match(url, file_name)
        if ret:
            stock_code = ret.group(1)
        else:
            stock_code = 0

        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        # 会出现sql注入，怎样修改呢？ 参数化
        sql = """select focus.note_info from focus inner join info on focus.info_id=info.id where info.code=%s;""" % stock_code
        cursor.execute(sql)
        stock_note_info = cursor.fetchone()
        cursor.close()
        db.close()

        content = re.sub(r"\{%code%\}", stock_code, content)
        content = re.sub(r"\{%note_info%\}", str(stock_note_info[0]), content)

        return content


@route(r"/update/(\d*)/(.*)\.html")
def update_note_info(file_name, url):
    """进行数据的真正更新"""
    stock_code = 0
    stock_note_info = ""

    ret = re.match(url, file_name)
    if ret:
        stock_code = ret.group(1)
        stock_note_info = ret.group(2)
        stock_note_info = unquote(stock_note_info)

    db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cursor = db.cursor()
    # 会出现sql注入，怎样修改呢？ 参数化
    sql = """update focus inner join info on focus.info_id=info.id set focus.note_info="%s" where info.code=%s;""" % (stock_note_info, stock_code)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    return "修改成功"


@route(r"/add/(\d*)\.html")
def add(file_name, url):
    """添加关注"""

    stock_code = 0

    ret = re.match(url, file_name)
    if ret:
        stock_code = ret.group(1)

    db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cursor = db.cursor()

    # 判断是否已经关注
    sql = """select * from focus inner join info on focus.info_id=info.id where info.code=%s;""" % (stock_code)
    cursor.execute(sql)
    if cursor.fetchone():
        cursor.close()
        db.close()
        return "已经关注过了，请不要重复关注"

    # 如果没有关注，那么就进行关注
    sql = """insert into focus (info_id) select id from info where code="%s";""" % (stock_code)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    return "关注成功"


# ------ 添加 -------
@route(r"/del/(\d*)\.html")
def delete(file_name, url):
    """取消关注"""

    stock_code = 0

    ret = re.match(url, file_name)
    if ret:
        stock_code = ret.group(1)

    db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cursor = db.cursor()

    # 判断是否已经关注
    sql = """select * from focus inner join info on focus.info_id=info.id where info.code=%s;""" % (stock_code)
    cursor.execute(sql)
    if not cursor.fetchone():
        cursor.close()
        db.close()
        return "并没有关注，为什么要取消关注呢？不理解，啦啦啦。。。"

    # 如果有关注，那么就进行取消关注
    sql = """delete from focus where info_id = (select id from info where code="%s");""" % (stock_code)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    return "取消关注成功"


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    try:
        for url, call_func in g_url_route.items():
            print(url)
            ret = re.match(url, file_name)
            if ret:
                return call_func(file_name, url)
                break

        else:
            return "没有访问的页面--->%s" % file_name

    except Exception as ret:
        return "%s" % ret

    else:
        return str(environ) + '-----404--->%s\n'
```

## 4. mini-web框架-mysql-改

my_web.py(修改)

```python
import pymysql
import time
import os
import re
import sys

template_root = "./templates"

# 用来存放url路由映射
# url_route = {
#   "/index.py":index_func,
#   "/center.py":center_func
# }
g_url_route = dict()


def route(url):
    def func1(func):
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        g_url_route[url]=func
        def func2(file_name):
            return func(file_name)
        return func2
    return func1


@route(r"/index.html")
def index(file_name, url=None):
    """返回index.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        # data_from_mysql = "暂时没有数据，请等待学习mysql吧，学习完mysql之后，这里就可以放入mysql查询到的数据了"
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select * from info;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        html_template = """
            <tr>
                <td>%d</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                </td>
                </tr>"""

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[1])


        content = re.sub(r"\{%content%\}", html, content)

        return content


@route(r"/center.html")
def center(file_name, url=None):
    """返回center.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        # data_from_mysql = "暂时没有数据,,,,~~~~(>_<)~~~~ "
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,j.note_info from info as i inner join focus as j on i.id=j.info_id;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        html_template = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                </td>
            </tr>
            """

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[0], info[0])

        content = re.sub(r"\{%content%\}", html, content)

        return content


@route(r"/update/(\d*)\.html")
def update(file_name, url):
    """显示 更新页面的内容"""
    try:
        template_file_name = template_root + "/update.html"
        f = open(template_file_name)
    except Exception as ret:
        return "%s,,,没有找到%s" % (ret, template_file_name)
    else:
        content = f.read()
        f.close()

        ret = re.match(url, file_name)
        if ret:
            stock_code = ret.group(1)
        else:
            stock_code = 0

        # ------ 添加 -------
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        # 会出现sql注入，怎样修改呢？ 参数化
        sql = """select focus.note_info from focus inner join info on focus.info_id=info.id where info.code=%s;""" % stock_code
        cursor.execute(sql)
        stock_note_info = cursor.fetchone()
        cursor.close()
        db.close()

        # ------ 修改 -------
        content = re.sub(r"\{%code%\}", stock_code, content)
        content = re.sub(r"\{%note_info%\}", str(stock_note_info[0]), content)

        return content


# ------ 添加 -------
@route(r"/update/(\d*)/(.*)\.html")
def update_note_info(file_name, url):
    """进行数据的真正更新"""
    stock_code = 0
    stock_note_info = ""

    ret = re.match(url, file_name)
    if ret:
        stock_code = ret.group(1)
        stock_note_info = ret.group(2)

    db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cursor = db.cursor()
    # 会出现sql注入，怎样修改呢？ 参数化
    sql = """update focus inner join info on focus.info_id=info.id set focus.note_info="%s" where info.code=%s;""" % (stock_note_info, stock_code)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    return "修改成功"


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    try:
        for url, call_func in g_url_route.items():
            print(url)
            ret = re.match(url, file_name)
            if ret:
                return call_func(file_name, url)
                break

        else:
            return "没有访问的页面--->%s" % file_name

    except Exception as ret:
        return "%s" % ret

    else:
        return str(environ) + '-----404--->%s\n'
```

## 5. mini-web框架-url编码

python3对url编解码

```python
import urllib.parse
# Python3 url编码
print(urllib.parse.quote("天安门"))
# Python3 url解码
print(urllib.parse.unquote("%E5%A4%A9%E5%AE%89%E9%97%A8"))
```

my_web.py(修改)

```python
import pymysql
import time
import os
import re
import sys
# ------- 添加 --------
from urllib.parse import unquote

template_root = "./templates"

# 用来存放url路由映射
# url_route = {
#   "/index.py":index_func,
#   "/center.py":center_func
# }
g_url_route = dict()


def route(url):
    def func1(func):
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        g_url_route[url]=func
        def func2(file_name):
            return func(file_name)
        return func2
    return func1


@route(r"/index.html")
def index(file_name, url=None):
    """返回index.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        # data_from_mysql = "暂时没有数据，请等待学习mysql吧，学习完mysql之后，这里就可以放入mysql查询到的数据了"
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select * from info;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        html_template = """
            <tr>
                <td>%d</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                </td>
                </tr>"""

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[1])


        content = re.sub(r"\{%content%\}", html, content)

        return content


@route(r"/center.html")
def center(file_name, url=None):
    """返回center.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        # data_from_mysql = "暂时没有数据,,,,~~~~(>_<)~~~~ "
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,j.note_info from info as i inner join focus as j on i.id=j.info_id;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        html_template = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                </td>
            </tr>
            """

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[0], info[0])

        content = re.sub(r"\{%content%\}", html, content)

        return content


@route(r"/update/(\d*)\.html")
def update(file_name, url):
    """显示 更新页面的内容"""
    try:
        template_file_name = template_root + "/update.html"
        f = open(template_file_name)
    except Exception as ret:
        return "%s,,,没有找到%s" % (ret, template_file_name)
    else:
        content = f.read()
        f.close()

        ret = re.match(url, file_name)
        if ret:
            stock_code = ret.group(1)
        else:
            stock_code = 0

        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        # 会出现sql注入，怎样修改呢？ 参数化
        sql = """select focus.note_info from focus inner join info on focus.info_id=info.id where info.code=%s;""" % stock_code
        cursor.execute(sql)
        stock_note_info = cursor.fetchone()
        cursor.close()
        db.close()

        content = re.sub(r"\{%code%\}", stock_code, content)
        content = re.sub(r"\{%note_info%\}", str(stock_note_info[0]), content)

        return content


@route(r"/update/(\d*)/(.*)\.html")
def update_note_info(file_name, url):
    """进行数据的真正更新"""
    stock_code = 0
    stock_note_info = ""

    ret = re.match(url, file_name)
    if ret:
        stock_code = ret.group(1)
        stock_note_info = ret.group(2)
        stock_note_info = unquote(stock_note_info)  # ------ 添加 -------

    db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cursor = db.cursor()
    # 会出现sql注入，怎样修改呢？ 参数化
    sql = """update focus inner join info on focus.info_id=info.id set focus.note_info="%s" where info.code=%s;""" % (stock_note_info, stock_code)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    return "修改成功"


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    try:
        for url, call_func in g_url_route.items():
            print(url)
            ret = re.match(url, file_name)
            if ret:
                return call_func(file_name, url)
                break

        else:
            return "没有访问的页面--->%s" % file_name

    except Exception as ret:
        return "%s" % ret

    else:
        return str(environ) + '-----404--->%s\n'
```

## 6. logging日志模块

![img](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218115826.jpeg)

![img](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218115831.jpeg)

开发过程中出现bug是必不可免的，你会怎样debug？从第1行代码开始看么？还是有个文件里面记录着哪里错了更方便呢！！！log日志

Python中有个logging模块可以完成相关信息的记录，在debug时用它往往事半功倍

### 6.1 日志级别

日志一共分成5个等级，从低到高分别是：

1. DEBUG
2. INFO
3. WARNING
4. ERROR
5. CRITICAL

说明:

- DEBUG：详细的信息,通常只出现在诊断问题上
- INFO：确认一切按预期运行
- WARNING：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
- ERROR：更严重的问题,软件没能执行一些功能
- CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行

这5个等级，也分别对应5种打日志的方法： debug 、info 、warning 、error 、critical。默认的是WARNING，当在WARNING或之上时才被跟踪。

### 6.2 日志输出

有两种方式记录跟踪，一种输出控制台，另一种是记录到文件中，如日志文件。

#### 6.2.1 将日志输出到控制台

比如，log1.py 如下：

```python
import logging  

logging.basicConfig(level=logging.WARNING,  
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  

# 开始使用log功能
logging.info('这是 loggging info message')  
logging.debug('这是 loggging debug message')  
logging.warning('这是 loggging a warning message')  
logging.error('这是 an loggging error message')  
logging.critical('这是 loggging critical message')
```

运行结果

```python
2017-11-06 23:07:35,725 - log1.py[line:9] - WARNING: 这是 loggging a warning message
2017-11-06 23:07:35,725 - log1.py[line:10] - ERROR: 这是 an loggging error message
2017-11-06 23:07:35,725 - log1.py[line:11] - CRITICAL: 这是 loggging critical message
```

**说明**

> 通过logging.basicConfig函数对日志的输出格式及方式做相关配置，上面代码设置日志的输出等级是WARNING级别，意思是WARNING级别以上的日志才会输出。另外还制定了日志输出的格式。
>
> 注意，只要用过一次log功能再次设置格式时将失效，实际开发中格式肯定不会经常变化，所以刚开始时需要设定好格式

#### 6.2.2 将日志输出到文件

我们还可以将日志输出到文件，只需要在logging.basicConfig函数中设置好输出文件的文件名和写文件的模式。

log2.py 如下：

```python
import logging  

logging.basicConfig(level=logging.WARNING,  
                    filename='./log.txt',  
                    filemode='w',  
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  
# use logging  
logging.info('这是 loggging info message')  
logging.debug('这是 loggging debug message')  
logging.warning('这是 loggging a warning message')  
logging.error('这是 an loggging error message')  
logging.critical('这是 loggging critical message')
```

运行效果

```python
python@ubuntu: cat log.txt 
2017-11-06 23:10:44,549 - log2.py[line:10] - WARNING: 这是 loggging a warning message
2017-11-06 23:10:44,549 - log2.py[line:11] - ERROR: 这是 an loggging error message
2017-11-06 23:10:44,549 - log2.py[line:12] - CRITICAL: 这是 loggging critical message
```

#### 6.2.3 既要把日志输出到控制台， 还要写入日志文件

这就需要一个叫作Logger 的对象来帮忙，下面将对他进行详细介绍，现在这里先学习怎么实现把日志既要输出到控制台又要输出到文件的功能。

```python
import logging  

# 第一步，创建一个logger  
logger = logging.getLogger()  
logger.setLevel(logging.INFO)  # Log等级总开关  

# 第二步，创建一个handler，用于写入日志文件  
logfile = './log.txt'  
fh = logging.FileHandler(logfile, mode='a')  # open的打开模式这里可以进行参考
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关  

# 第三步，再创建一个handler，用于输出到控制台  
ch = logging.StreamHandler()  
ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关  

# 第四步，定义handler的输出格式  
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  

# 第五步，将logger添加到handler里面  
logger.addHandler(fh)  
logger.addHandler(ch)  

# 日志  
logger.debug('这是 logger debug message')  
logger.info('这是 logger info message')  
logger.warning('这是 logger warning message')  
logger.error('这是 logger error message')  
logger.critical('这是 logger critical message')
```

运行时终端的输出结果:

```python
2017-11-06 23:14:04,731 - log3.py[line:28] - WARNING: 这是 logger warning message
2017-11-06 23:14:04,731 - log3.py[line:29] - ERROR: 这是 logger error message
2017-11-06 23:14:04,731 - log3.py[line:30] - CRITICAL: 这是 logger critical message
```

在log.txt中，有如下数据：

```python
2017-11-06 23:14:04,731 - log3.py[line:27] - INFO: 这是 logger info message
2017-11-06 23:14:04,731 - log3.py[line:28] - WARNING: 这是 logger warning message
2017-11-06 23:14:04,731 - log3.py[line:29] - ERROR: 这是 logger error message
2017-11-06 23:14:04,731 - log3.py[line:30] - CRITICAL: 这是 logger critical message
```

### 6.3 日志格式说明

logging.basicConfig函数中，可以指定日志的输出格式format，这个参数可以输出很多有用的信息，如下:

- %(levelno)s: 打印日志级别的数值
- %(levelname)s: 打印日志级别名称
- %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
- %(filename)s: 打印当前执行程序名
- %(funcName)s: 打印日志的当前函数
- %(lineno)d: 打印日志的当前行号
- %(asctime)s: 打印日志的时间
- %(thread)d: 打印线程ID
- %(threadName)s: 打印线程名称
- %(process)d: 打印进程ID
- %(message)s: 打印日志信息

在工作中给的常用格式如下:

```python
format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
```

这个格式可以输出日志的打印时间，是哪个模块输出的，输出的日志级别是什么，以及输入的日志内容。