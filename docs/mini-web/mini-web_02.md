## 1. mini web框架-4-路由

dynamic/my_web.py

```python
import time
import os
import re

template_root = "./templates"

# ----------更新----------
# 用来存放url路由映射
# url_route = {
#   "/index.py": index_func,
#   "/center.py": center_func
# }
g_url_route = dict()

# ----------更新----------
def route(url):
    def func1(func):
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        g_url_route[url] = func
        def func2(file_name):
            return func(file_name)
        return func2
    return func1


@route("/index.py")  # ----------更新----------
def index(file_name):
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

        data_from_mysql = "暂时没有数据，请等待学习mysql吧，学习完mysql之后，这里就可以放入mysql查询到的数据了"
        content = re.sub(r"\{%content%\}", data_from_mysql, content)

        return content


@route("/center.py")  # ----------更新----------
def center(file_name):
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

        data_from_mysql = "暂时没有数据,,,,~~~~(>_<)~~~~ "
        content = re.sub(r"\{%content%\}", data_from_mysql, content)

        return content


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    # ----------更新----------
    try:
        return g_url_route[file_name](file_name)
    except Exception as ret:
        return "%s" % ret
```

## 2. 伪静态、静态和动态的区别

目前开发的网站其实真正意义上都是动态网站，只是URL上有些区别，一般URL分为静态URL、动态URL、伪静态URL，他们的区别是什么?

静态URL

静态URL类似 域名/news/2012-5-18/110.html 我们一般称为`真静态URL`，每个网页有真实的物理路径，也就是真实存在服务器里的。

- 优点是：

  > 网站打开速度快，因为它不用进行运算；另外网址结构比较友好，利于记忆。

- 缺点是：

  > 最大的缺点是如果是中大型网站，则产生的页面特别多，不好管理。至于有的开发者说占用硬盘空间大，我觉得这个可有忽略不计，占用不了多少空间的，况且目前硬盘空间都比较大。还有的开发者说会伤硬盘，这点也可以忽略不计。

- 一句话总结:

  > 静态网站对SEO的影响：静态URL对SEO肯定有加分的影响，因为打开速度快，这个是本质。

动态URL

动态URL类似 域名/NewsMore.asp?id=5 或者 域名/DaiKuan.php?id=17，带有？号的URL，我们一般称为动态网址，每个URL只是一个逻辑地址，并不是真实物理存在服务器硬盘里的。

- 优点是：

  > 适合中大型网站，修改页面很方便，因为是逻辑地址，所以占用硬盘空间要比纯静态网站小。

- 缺点是：

  > 因为要进行运算，所以打开速度稍慢，不过这个可有忽略不计，目前有服务器缓存技术可以解决速度问题。最大的缺点是URL结构稍稍复杂，不利于记忆。

- 一句话总结:

  > 动态URL对SEO的影响：目前百度SE已经能够很好的理解动态URL，所以对SEO没有什么减分的影响（特别复杂的URL结构除外）。所以你无论选择动态还是静态其实都无所谓，看你选择的程序和需求了。

伪静态URL

伪静态URL类似 域名/course/74.html 这个URL和真静态URL类似。他是通过伪静态规则把动态URL伪装成静态网址。也是逻辑地址，不存在物理地址。

- 优点是：

  > URL比较友好，利于记忆。非常适合大中型网站，是个折中方案。

- 缺点是：

  > 设置麻烦，服务器要支持重写规则，小企业网站或者玩不好的就不要折腾了。另外进行了伪静态网站访问速度并没有变快，因为实质上它会额外的进行运算解释，反正增加了服务器负担，速度反而变慢，不过现在的服务器都很强大，这种影响也可以忽略不计。还有可能会造成动态URL和静态URL都被搜索引擎收录，不过可以用robots禁止掉动态地址。

- 一句话总结:

  > 对SEO的影响：和动态URL一样，对SEO没有什么减分影响。

## 3. mini-web框架-实现伪静态url

readme.txt(新建)

```sql
运行方式如下:
python3 web_server.py 7890 my_web:application
```

web_server.py(部分更新)

```python
import select
import time
import socket
import sys
import re
import multiprocessing


class WSGIServer(object):
    """定义一个WSGI服务器的类"""

    def __init__(self, port, documents_root, app):

        # 1. 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2. 绑定本地信息
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        # 3. 变为监听套接字
        self.server_socket.listen(128)

        # 设定资源文件的路径
        self.documents_root = documents_root

        # 设定web框架可以调用的函数(对象)
        self.app = app

    def run_forever(self):
        """运行服务器"""

        # 等待对方链接
        while True:
            new_socket, new_addr = self.server_socket.accept()
            # 创建一个新的进程来完成这个客户端的请求任务
            new_socket.settimeout(3)  # 3s
            new_process = multiprocessing.Process(target=self.deal_with_request, args=(new_socket,))
            new_process.start()
            new_socket.close()

    def deal_with_request(self, client_socket):
        """以长链接的方式，为这个浏览器服务器"""

        while True:
            try:
                request = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                print("========>", ret)
                client_socket.close()
                return

            # 判断浏览器是否关闭
            if not request:
                client_socket.close()
                return

            request_lines = request.splitlines()
            for i, line in enumerate(request_lines):
                print(i, line)

            # 提取请求的文件(index.html)
            # GET /a/b/c/d/e/index.html HTTP/1.1
            ret = re.match(r"([^/]*)([^ ]+)", request_lines[0])
            if ret:
                print("正则提取数据:", ret.group(1))
                print("正则提取数据:", ret.group(2))
                file_name = ret.group(2)
                if file_name == "/":
                    file_name = "/index.html"

            # 如果不是以.html结尾的文件,都认为是普通的文件
            # 如果是.html结尾的请求,那么就让web框架进行处理
            if not file_name.endswith(".html"):  # --------- 进行了更新-------

                # 读取文件数据
                try:
                    print(self.documents_root+file_name)
                    f = open(self.documents_root+file_name, "rb")
                except:
                    response_body = "file not found, 请输入正确的url"

                    response_header = "HTTP/1.1 404 not found\r\n"
                    response_header += "Content-Type: text/html; charset=utf-8\r\n"
                    response_header += "Content-Length: %d\r\n" % (len(response_body))
                    response_header += "\r\n"

                    response = response_header + response_body

                    # 将header返回给浏览器
                    client_socket.send(response.encode('utf-8'))

                else:
                    content = f.read()
                    f.close()

                    response_body = content

                    response_header = "HTTP/1.1 200 OK\r\n"
                    response_header += "Content-Length: %d\r\n" % (len(response_body))
                    response_header += "\r\n"

                    # 将header返回给浏览器
                    client_socket.send(response_header.encode('utf-8') + response_body)

            # 以.py结尾的文件，就认为是浏览需要动态的页面
            else:
                # 准备一个字典，里面存放需要传递给web框架的数据
                env = dict()
                env['PATH_INFO'] = file_name  # 例如 index.py

                # 存web返回的数据
                response_body = self.app(env, self.set_response_headers)

                # 合并header和body
                response_header = "HTTP/1.1 {status}\r\n".format(status=self.headers[0])
                response_header += "Content-Type: text/html; charset=utf-8\r\n"
                response_header += "Content-Length: %d\r\n" % len(response_body.encode("utf-8"))
                for temp_head in self.headers[1]:
                    response_header += "{0}:{1}\r\n".format(*temp_head)

                response = response_header + "\r\n"

                response += response_body

                client_socket.send(response.encode('utf-8'))


    def set_response_headers(self, status, headers):
        """这个方法，会在 web框架中被默认调用"""
        response_header_default = [
            ("Data", time.time()),
            ("Server", "ItCast-python mini web server")
        ]

        # 将状态码/相应头信息存储起来
        # [字符串, [xxxxx, xxx2]]
        self.headers = [status, response_header_default + headers]


# 设置静态资源访问的路径
g_static_document_root = "./static"
# 设置动态资源访问的路径
g_dynamic_document_root = "./dynamic"

def main():
    """控制web服务器整体"""
    # python3 xxxx.py 7890
    if len(sys.argv) == 3:
        # 获取web服务器的port
        port = sys.argv[1]
        if port.isdigit():
            port = int(port)
        # 获取web服务器需要动态资源时，访问的web框架名字
        web_frame_module_app_name = sys.argv[2]
    else:
        print("运行方式如: python3 xxx.py 7890 my_web_frame_name:application")
        return

    print("http服务器使用的port:%s" % port)

    # 将动态路径即存放py文件的路径，添加到path中，这样python就能够找到这个路径了
    sys.path.append(g_dynamic_document_root)

    ret = re.match(r"([^:]*):(.*)", web_frame_module_app_name)
    if ret:
        # 获取模块名
        web_frame_module_name = ret.group(1)
        # 获取可以调用web框架的应用名称
        app_name = ret.group(2)

    # 导入web框架的主模块
    web_frame_module = __import__(web_frame_module_name)
    # 获取那个可以直接调用的函数(对象)
    app = getattr(web_frame_module, app_name) 

    # print(app)  # for test

    # 启动http服务器
    http_server = WSGIServer(port, g_static_document_root, app)
    # 运行http服务器
    http_server.run_forever()


if __name__ == "__main__":
    main()
```

my_web.py(部分修改)

```python
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


@route("/index.html")  # ------- 修改------
def index(file_name):
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

        data_from_mysql = "暂时没有数据，请等待学习mysql吧，学习完mysql之后，这里就可以放入mysql查询到的数据了"
        content = re.sub(r"\{%content%\}", data_from_mysql, content)

        return content


@route("/center.html")  # ------- 修改------
def center(file_name):
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

        data_from_mysql = "暂时没有数据,,,,~~~~(>_<)~~~~ "
        content = re.sub(r"\{%content%\}", data_from_mysql, content)

        return content


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    try:
        return g_url_route[file_name](file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        return str(environ) + '-----404--->%s\n'
```

## 4. 准备数据

1. 创建数据库

```sql
create database stock_db charset=utf8;
```

2. 选择数据库

```sql
use stock_db;
```

3. 导入数据

`stock_db.sql`在课件中

```sql
source stock_db.sql
```

4. 表结构如下

```sql
mysql> desc focus;
+-----------+------------------+------+-----+---------+----------------+
| Field     | Type             | Null | Key | Default | Extra          |
+-----------+------------------+------+-----+---------+----------------+
| id        | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| note_info | varchar(200)     | YES  |     |         |                |
| info_id   | int(10) unsigned | YES  | MUL | NULL    |                |
+-----------+------------------+------+-----+---------+----------------+
mysql> desc info;
+----------+------------------+------+-----+---------+----------------+
| Field    | Type             | Null | Key | Default | Extra          |
+----------+------------------+------+-----+---------+----------------+
| id       | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| code     | varchar(6)       | NO   |     | NULL    |                |
| short    | varchar(10)      | NO   |     | NULL    |                |
| chg      | varchar(10)      | NO   |     | NULL    |                |
| turnover | varchar(255)     | NO   |     | NULL    |                |
| price    | decimal(10,2)    | NO   |     | NULL    |                |
| highs    | decimal(10,2)    | NO   |     | NULL    |                |
| time     | date             | YES  |     | NULL    |                |
+----------+------------------+------+-----+---------+----------------+
```

## 5. mini-web框架-从mysql中查询数据

my_web.py(更新)

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


@route("/index.html")
def index(file_name):
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

        # --------添加---------
        # data_from_mysql = "暂时没有数据，请等待学习mysql吧，学习完mysql之后，这里就可以放入mysql查询到的数据了"
        db = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
        cursor = db.cursor()
        sql = """select * from info;"""
        cursor.execute(sql)
        data_from_mysql = cursor.fetchall()
        cursor.close()
        db.close()

        content = re.sub(r"\{%content%\}", str(data_from_mysql), content)

        return content


@route("/center.html")
def center(file_name):
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

        data_from_mysql = "暂时没有数据,,,,~~~~(>_<)~~~~ "
        content = re.sub(r"\{%content%\}", data_from_mysql, content)

        return content


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    try:
        return g_url_route[file_name](file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        return str(environ) + '-----404--->%s\n'
```

## 6. mini-web框架-组装数据为html格式

my_web.py(更新)

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

@route("/index.html")
def index(file_name):
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


@route("/center.html")
def center(file_name):
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


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    try:
        return g_url_route[file_name](file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        return str(environ) + '-----404--->%s\n'
```