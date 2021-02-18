## 1. 测试与部署

### 1.1 蓝图Blueprint

**为什么学习蓝图？**

我们学习Flask框架，是从写单个文件，执行hello world开始的。我们在这单个文件中可以定义路由、视图函数、定义模型等等。但这显然存在一个问题：随着业务代码的增加，将所有代码都放在单个程序文件中，是非常不合适的。这不仅会让代码阅读变得困难，而且会给后期维护带来麻烦。

如下示例：我们在一个文件中写入多个路由，这会使代码维护变得困难。

```python
    from flask import Flask    
    app = Flask(__name__)    
    @app.route('/')
    def index():
        return 'index'

    @app.route('/list')
    def list():
        return 'list'

    @app.route('/detail')
    def detail():
        return 'detail'

    @app.route('/')
    def admin_home():
        return 'admin_home'

    @app.route('/new')
    def new():
        return 'new'

    @app.route('/edit')
    def edit():
        return 'edit'
```

**问题：一个程序执行文件中，功能代码过多。**就是让代码模块化。根据具体不同功能模块的实现，划分成不同的分类，降低各功能模块之间的耦合度。python中的模块制作和导入就是基于实现功能模块的封装的需求。

**尝试用模块导入的方式解决：** 我们把上述一个py文件的多个路由视图函数给拆成两个文件：app.py和admin.py文件。app.py文件作为程序启动文件，因为admin文件没有应用程序实例app，在admin文件中要使用app.route路由装饰器，需要把app.py文件的app导入到admin.py文件中。

```python
# 文件app.py
from flask import Flask
# 导入admin中的内容
from admin import *
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/list')
def list():
    return 'list'

@app.route('/detail')
def detail():
    return 'detail'

if __name__ == '__main__':
    app.run()

# 文件admin.py    
from app import app
@app.route('/')
def admin_home():
    return 'admin_home'

@app.route('/new')
def new():
    return 'new'

@app.route('/edit')
def edit():
    return 'edit'
```

**启动app.py文件后，我们发现admin.py文件中的路由都无法访问。** 也就是说，python中的模块化虽然能把代码给拆分开，但不能解决路由映射的问题。

![模块导入](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152102.png)

**什么是蓝图？**

蓝图：用于实现单个应用的视图、模板、静态文件的集合。

蓝图就是模块化处理的类。

简单来说，蓝图就是一个存储操作路由映射方法的容器，主要用来实现客户端请求和URL相互关联的功能。 在Flask中，使用蓝图可以帮助我们实现模块化应用的功能。

**蓝图的运行机制：**

蓝图是保存了一组将来可以在应用对象上执行的操作。注册路由就是一种操作,当在程序实例上调用route装饰器注册路由时，这个操作将修改对象的url_map路由映射列表。当我们在蓝图对象上调用route装饰器注册路由时，它只是在内部的一个延迟操作记录列表defered_functions中添加了一个项。当执行应用对象的 register_blueprint() 方法时，应用对象从蓝图对象的 defered_functions 列表中取出每一项，即调用应用对象的 add_url_rule() 方法，这将会修改程序实例的路由映射列表。

**蓝图的使用：**

一、创建蓝图对象。

```python
#Blueprint必须指定两个参数，admin表示蓝图的名称，__name__表示蓝图所在模块
admin = Blueprint('admin',__name__)
```

二、注册蓝图路由。

```python
@admin.route('/')
def admin_index():
    return 'admin_index'
```

三、在程序实例中注册该蓝图。

```python
app.register_blueprint(admin,url_prefix='/admin')
```

**文件目录：**

![目录文件](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152110.png)

**程序执行文件/test4/test.py**

```
from flask import Flask
#导入蓝图对象
from login import logins
from user import users

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
#注册蓝图，第一个参数logins是蓝图对象，url_prefix参数默认值是根路由，如果指定，会在蓝图注册的路由url中添加前缀。
app.register_blueprint(logins,url_prefix='')
app.register_blueprint(users,url_prefix='')

if __name__ == '__main__':
    app.run(debug=True)
```

**创建蓝图：/test4/user.py**

```python
from flask import Blueprint,render_template
#创建蓝图，第一个参数指定了蓝图的名字。
users = Blueprint('user',__name__)

@users.route('/user')
def user():
    return render_template('user.html')
```

**创建蓝图：/test4/login.py**

```python
from flask import Blueprint,render_template
#创建蓝图
logins = Blueprint('login',__name__)

@logins.route('/login')
def login():
    return render_template('login.html')
```

**运行/test4/test.py文件**

![蓝图路由](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152118.png)

**动态路由示例(作者--图书)：**

文件目录：Flask_test4/delete.py

```python
from flask import Blueprint,redirect,url_for
app_au = Blueprint('app_au',__name__)
app_bk = Blueprint('app_bk',__name__)

from test4 import *

@app_au.route('/delete_au<id>')
def delete_au(id):
    del_au = Author.query.filter_by(id=id).first()
    db.session.delete(del_au)
    db.session.commit()
    return redirect(url_for('index'))

@app_bk.route('/delete_bk<id>')
def delete_bk(id):
    del_bk = Book.query.filter_by(id=id).first()
    db.session.delete(del_bk)
    db.session.commit()
    return redirect(url_for('index'))
```

文件目录：Flask_test4/test4.py

```python
#coding=utf-8
#目的：创建两个模型类型，实现数据库的连接和数据的操作
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
#导入delete文件中的蓝图对象
from delete import app_au,app_bk

app = Flask(__name__)
#对数据库连接的基本设置
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:mysql@localhost/test0'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#把应用程序的实例和SQLAlchemy进行关联
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'a'

#自定义表单，实现数据的输入保存操作
class Append(FlaskForm):
    author = StringField(validators=[DataRequired()])
    book = StringField(validators=[DataRequired()])
    submit = SubmitField(u'提交')

#自定义模型类
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)

    def __repr__(self):
        return 'author:%s'%self.name

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    info = db.Column(db.String(32),unique=True)
    def __repr__(self):
        return 'book:%s'%self.info

@app.route('/',methods=['GET','POST'])
def index():
    au = Author.query.all()
    bk = Book.query.all()
    form = Append()
    if form.validate_on_submit():
        #从表单中获取数据
        wtf_au = form.author.data
        wtf_bk = form.book.data
        #把数据存入模型类中
        db_au = Author(name=wtf_au)
        db_bk = Book(info=wtf_bk)
        #添加到数据库操作
        db.session.add_all([db_au,db_bk])
        db.session.commit()
        au = Author.query.all()
        bk = Book.query.all()
        return render_template('index.html',au=au,bk=bk,form=form)

    if request.method == 'GET':
        return render_template('index.html',au=au,bk=bk,form=form)

#注册蓝图
app.register_blueprint(app_au)
app.register_blueprint(app_bk)

if __name__ == '__main__':    
    print app.url_map
    app.run(debug=True)
```

查看蓝图路由：蓝图路由可以分为两块，"."前面的是蓝图名称，"."后面的是视图函数名。

![蓝图url_prefix](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152129.png)

### 1.2 单元测试

**为什么要测试？**

Web程序开发过程一般包括以下几个阶段：[需求分析，设计阶段，实现阶段，测试阶段]。其中测试阶段通过人工或自动来运行测试某个系统的功能。目的是检验其是否满足需求，并得出特定的结果，以达到弄清楚预期结果和实际结果之间的差别的最终目的。

**测试的分类：**

测试从软件开发过程可以分为：单元测试、集成测试、系统测试等。在众多的测试中，与程序开发人员最密切的就是单元测试，因为单元测试是由开发人员进行的，而其他测试都由专业的测试人员来完成。所以我们主要学习单元测试。

**什么是单元测试？**

程序开发过程中，写代码是为了实现需求。当我们的代码通过了编译，只是说明它的语法正确，功能能否实现则不能保证。 因此，当我们的某些功能代码完成后，为了检验其是否满足程序的需求。可以通过编写测试代码，模拟程序运行的过程，检验功能代码是否符合预期。

单元测试就是开发者编写一小段代码，检验目标代码的功能是否符合预期。通常情况下，单元测试主要面向一些功能单一的模块进行。

举个例子：一部手机有许多零部件组成，在正式组装一部手机前，手机内部的各个零部件，CPU、内存、电池、摄像头等，都要进行测试，这就是单元测试。

在Web开发过程中，单元测试实际上就是一些“断言”（assert）代码。

断言就是判断一个函数或对象的一个方法所产生的结果是否符合你期望的那个结果。 python中assert断言是声明布尔值为真的判定，如果表达式为假会发生异常。单元测试中，一般使用assert来断言结果。

**断言方法的使用：**

![断言](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152136.png)

断言语句类似于：

```python
if not expression:
    raise AssertionError
```

**常用的断言方法：**

```bash
assertEqual     如果两个值相等，则pass
assertNotEqual  如果两个值不相等，则pass
assertTrue      判断bool值为True，则pass
assertFalse     判断bool值为False，则pass
assertIsNone    不存在，则pass
assertIsNotNone 存在，则pass
```

**如何测试？**

简单的测试用例：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，

```python
def fibo(x):
    if x == 0:
        resp = 0
    elif x == 1:
        resp = 1
    else:
        return fibo(x-1) + fibo(x-2)
    return resp
assert fibo(5) == 5
```

![fibo](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152144.png)

**单元测试的基本写法：**

**首先**，定义一个类，继承自unittest.TestCase

```python
import unittest
class TestClass(unitest.TestCase):
    pass
```

**其次**，在测试类中，定义两个测试方法

```python
import unittest
class TestClass(unittest.TestCase):

    #该方法会首先执行，方法名为固定写法
    def setUp(self):
        pass

    #该方法会在测试代码执行完后执行，方法名为固定写法
    def tearDown(self):
        pass
```

**最后**，在测试类中，编写测试代码

```python
import unittest
class TestClass(unittest.TestCase):

    #该方法会首先执行，相当于做测试前的准备工作
    def setUp(self):
        pass

    #该方法会在测试代码执行完后执行，相当于做测试后的扫尾工作
    def tearDown(self):
        pass
    #测试代码
    def test_app_exists(self):
        pass
```

**发送邮件测试：**

```
#coding=utf-8
import unittest
from Flask_day04 import app
class TestCase(unittest.TestCase):
    # 创建测试环境，在测试代码执行前执行
    def setUp(self):
        self.app = app
        # 激活测试标志
        app.config['TESTING'] = True
        self.client = self.app.test_client()

    # 在测试代码执行完成后执行
    def tearDown(self):
        pass

    # 测试代码
    def test_email(self):
        resp = self.client.get('/')
        print resp.data
        self.assertEqual(resp.data,'Sent　Succeed')
```

**数据库测试：**

```
#coding=utf-8
import unittest
from author_book import *

#自定义测试类，setUp方法和tearDown方法会分别在测试前后执行。以test_开头的函数就是具体的测试代码。

class DatabaseTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/test0'
        self.app = app
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    #测试代码
    def test_append_data(self):
        au = Author(name='itcast')
        bk = Book(info='python')
        db.session.add_all([au,bk])
        db.session.commit()
        author = Author.query.filter_by(name='itcast').first()
        book = Book.query.filter_by(info='python').first()
        #断言数据存在
        self.assertIsNotNone(author)
        self.assertIsNotNone(book)
```

### 1.3 部署

当我们执行下面的hello.py时，使用的flask自带的服务器，完成了web服务的启动。在生产环境中，flask自带的服务器，无法满足性能要求，我们这里采用Gunicorn做wsgi容器，来部署flask程序。Gunicorn（绿色独角兽）是一个Python WSGI的HTTP服务器。从Ruby的独角兽（Unicorn ）项目移植。该Gunicorn服务器与各种Web框架兼容，实现非常简单，轻量级的资源消耗。Gunicorn直接用命令启动，不需要编写配置文件，相对uWSGI要容易很多。

区分几个概念：

**WSGI：**全称是Web Server Gateway Interface（web服务器网关接口），它是一种规范，它是web服务器和web应用程序之间的接口。它的作用就像是桥梁，连接在web服务器和web应用框架之间。

**uwsgi：**是一种传输协议，用于定义传输信息的类型。

**uWSGI：**是实现了uwsgi协议WSGI的web服务器。

我们的部署方式： nginx + gunicorn + flask

```python
# hello.py

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return '<h1>hello world</h1>'

if __name__ == '__main__':
    app.run(debug=True)
```

**使用Gunicorn：**

web开发中，部署方式大致类似。简单来说，前端代理使用Nginx主要是为了实现分流、转发、负载均衡，以及分担服务器的压力。Nginx部署简单，内存消耗少，成本低。Nginx既可以做正向代理，也可以做反向代理。

正向代理：请求经过代理服务器从局域网发出，然后到达互联网上的服务器。

特点：服务端并不知道真正的客户端是谁。

反向代理：请求从互联网发出，先进入代理服务器，再转发给局域网内的服务器。

特点：客户端并不知道真正的服务端是谁。

区别：正向代理的对象是客户端。反向代理的对象是服务端。

**安装gunicorn**

```
pip install gunicorn
```

**查看命令行选项：** 安装gunicorn成功后，通过命令行的方式可以查看gunicorn的使用信息。

```bash
$gunicorn -h
```

**直接运行：**

```bash
#直接运行，默认启动的127.0.0.1::8000
gunicorn 运行文件名称:Flask程序实例名
```

**指定进程和端口号：** -w: 表示进程（worker）。 -b：表示绑定ip地址和端口号（bind）。

```bash
$gunicorn -w 4 -b 127.0.0.1:5001 运行文件名称:Flask程序实例名
```

**安装Nginx**

```bash
$ sudo apt-get install nginx
```

**Nginx配置：**

默认安装到/usr/local/nginx/目录，进入目录。

启动nginx：

```
#启动
sudo sbin/nginx
#查看
ps aux | grep nginx
#停止
sudo sbin/nginx -s stop
```

打开/usr/local/nginx/conf/nginx.conf文件

```
server {
    # 监听80端口
    listen 80;
    # 本机
    server_name localhost; 
    # 默认请求的url
    location / {
        #请求转发到gunicorn服务器
        proxy_pass http://127.0.0.1:5001; 
        #设置请求头，并将头信息传递给服务器端 
        proxy_set_header Host $host; 
    }
}
```

### 1.4 Restful

2000年，Roy Thomas Fielding博士在他的博士论文《Architectural Styles and the Design of Network-based Software Architectures》中提出了几种软件应用的架构风格，REST作为其中的一种架构风格在这篇论文中进行了概括性的介绍。

REST:Representational State Transfer的缩写，翻译：“具象状态传输”。一般解释为“表现层状态转换”。

REST是设计风格而不是标准。是指客户端和服务器的交互形式。我们需要关注的重点是如何设计REST风格的网络接口。

- REST的特点：
- 具象的。一般指表现层，要表现的对象就是资源。比如，客户端访问服务器，获取的数据就是资源。比如文字、图片、音视频等。
- 表现：资源的表现形式。txt格式、html格式、json格式、jpg格式等。浏览器通过URL确定资源的位置，但是需要在HTTP请求头中，用Accept和Content-Type字段指定，这两个字段是对资源表现的描述。
- 状态转换：客户端和服务器交互的过程。在这个过程中，一定会有数据和状态的转化，这种转化叫做状态转换。其中，GET表示获取资源，POST表示新建资源，PUT表示更新资源，DELETE表示删除资源。HTTP协议中最常用的就是这四种操作方式。
  - RESTful架构：
  - 每个URL代表一种资源；
  - 客户端和服务器之间，传递这种资源的某种表现层；
  - 客户端通过四个http动词，对服务器资源进行操作，实现表现层状态转换。

## 2. 如何设计符合RESTful风格的API

### 2.1 域名：

将api部署在专用域名下：

```bash
http://api.example.com
```

或者将api放在主域名下：

```bash
http://www.example.com/api/
```

### 2.2 版本：

将API的版本号放在url中。

```bash
http://www.example.com/app/1.0/info
http://www.example.com/app/1.2/info
```

### 2.3 路径：

路径表示API的具体网址。每个网址代表一种资源。 资源作为网址，网址中不能有动词只能有名词，一般名词要与数据库的表名对应。而且名词要使用复数。

错误示例：

```bash
http://www.example.com/getGoods
http://www.example.com/listOrders
```

正确示例：

```bash
#获取单个商品
http://www.example.com/app/goods/1
#获取所有商品
http://www.example.com/app/goods
```

### 2.4 使用标准的HTTP方法：

对于资源的具体操作类型，由HTTP动词表示。 常用的HTTP动词有四个。

```bash
GET     SELECT ：从服务器获取资源。
POST    CREATE ：在服务器新建资源。
PUT     UPDATE ：在服务器更新资源。
DELETE  DELETE ：从服务器删除资源。
```

示例：

```bash
#获取指定商品的信息
GET http://www.example.com/goods/ID
#新建商品的信息
POST http://www.example.com/goods
#更新指定商品的信息
PUT http://www.example.com/goods/ID
#删除指定商品的信息
DELETE http://www.example.com/goods/ID
```

### 2.5 过滤信息：

如果资源数据较多，服务器不能将所有数据一次全部返回给客户端。API应该提供参数，过滤返回结果。 实例：

```bash
#指定返回数据的数量
http://www.example.com/goods?limit=10
#指定返回数据的开始位置
http://www.example.com/goods?offset=10
#指定第几页，以及每页数据的数量
http://www.example.com/goods?page=2&per_page=20
```

### 2.6 状态码：

服务器向用户返回的状态码和提示信息，常用的有：

```bash
200 OK  ：服务器成功返回用户请求的数据
201 CREATED ：用户新建或修改数据成功。
202 Accepted：表示请求已进入后台排队。
400 INVALID REQUEST ：用户发出的请求有错误。
401 Unauthorized ：用户没有权限。
403 Forbidden ：访问被禁止。
404 NOT FOUND ：请求针对的是不存在的记录。
406 Not Acceptable ：用户请求的的格式不正确。
500 INTERNAL SERVER ERROR ：服务器发生错误。
```

### 2.7 错误信息：

一般来说，服务器返回的错误信息，以键值对的形式返回。

```bash
{
    error:'Invalid API KEY'
}
```

### 2.8 响应结果：

针对不同结果，服务器向客户端返回的结果应符合以下规范。

```bash
#返回商品列表
GET    http://www.example.com/goods
#返回单个商品
GET    http://www.example.com/goods/cup
#返回新生成的商品
POST   http://www.example.com/goods
#返回一个空文档
DELETE http://www.example.com/goods
```

### 2.9 使用链接关联相关的资源：

在返回响应结果时提供链接其他API的方法，使客户端很方便的获取相关联的信息。

### 2.10 其他：

服务器返回的数据格式，应该尽量使用JSON，避免使用XML。

## 3. 性能

### 3.1 不同角度的网站性能

**普通用户认为的网站性能**

网站性能对于普通用户来说，最直接的体现就是响应时间。用户在浏览器上直观感受到的网站响应速度，即从客户端发送请求，到服务器返回响应内容的时间。

做为网站开发人员来说，网站性能通常会和普通的用户理解的不一样。

普通用户感受到的网站性能，并不只是由网站服务器决定的。它还包括客户端计算机和服务器通信的时间，网站服务器处理响应的时间，客户端浏览器构造请求解析响应数据的时间。甚至，不同的计算机性能、不同浏览器解析HTML的速度、不同网络运营商提供的网络带宽房屋的差异，这些都会导致用户感受到响应时间，可能大于网站服务器处理请求的时间。

**开发人员认为的网站性能**

开发人员关注的主要是服务器应用程序本身，以及相关配套系统的性能。包括并发处理能力、系统稳定性、响应延迟等技术指标。

对性能优化的主要手段，包括使用缓存加速数据读取，使用集群提高数据吞吐能力，使用异步消息加快请求响应，使用代码改善程序性能。

**运维人员认为的网站性能**

运维人员关注的主要是服务器基础设施和资源利用率。如服务器硬件的配置、网络运营商的带宽、数据中心的网络架构等。主要优化手段有使用高性价比的服务器、建设优化骨干网络、利用虚拟化技术优化资源利用等。

### 3.2 性能的指标

从开发人员的角度，网站性能的指标主要有并发数和响应时间。

**并发数**

并发数是指系统能够处理请求的数量，对于网站服务器而言，并发数也就是网站并发用户数，指同时提交请求的用户数目。

与并发数相对应的还有网站在线用户数（登录用户数）和网站用户数（一般指注册用户数）。他们的关系一般是：网站用户数>网站用户在线数>网站用户并发数

**响应时间**

响应时间是最重要的性能指标，直接反映了系统的快慢。

**常见的系统操作响应时间**

| 操作                              | 响应时间 |
| --------------------------------- | -------- |
| 打开一个网站                      | 几秒     |
| 在数据库中查询一条记录（有索引）  | 十几毫秒 |
| 机械磁盘一次寻址定位              | 4毫秒    |
| 从机械磁盘顺序读取1MB数据         | 2毫秒    |
| 从SSD磁盘顺序读取1MB数据          | 0.3毫秒  |
| 从远程分布式缓存Redis读取一个数据 | 0.5毫秒  |
| 从内存中读取1MB数据               | 十几微秒 |
| 网络传输2KB数据                   | 1微秒    |

### 3.3 性能的优化

对于开发人员来说，网站性能优化一般包括Web前端性能优化、应用服务器性能优化、存储服务器性能优化三类。

**Web前端性能优化**

**1、减少http请求** http协议是无状态的应用层协议，意味着每次http请求都需要建立通信链路、进行数据传输，而在服务器端，每个http请求都需要启动独立的线程去处理。减少http请求的数目可有效提高访问性能。

减少http的主要手段是合并CSS、合并javascript、合并图片。

**2、使用浏览器缓存** 对一个网站而言，CSS、javascript、logo、图标，这些静态资源文件更新的频率都比较低，而这些文件又几乎是每次http请求都需要的。如果将这些文件缓存在浏览器中，可以极好的改善性能。通过设置http头中的cache-control和expires的属性，可设定浏览器缓存，缓存时间可以自定义。

**3、启用压缩** 在服务器端对文件进行压缩，在浏览器端对文件解压缩，可有效减少通信传输的数据量。如果可以的话，尽可能的将外部的脚本、样式进行合并，多个合为一个。文本文件的压缩效率可达到80%以上，因此HTML、CSS、javascript文件启用GZip压缩可达到较好的效果。但是压缩对服务器和浏览器产生一定的压力，在网络带宽良好，而服务器资源不足的情况下要综合考虑。

**4、CSS放在页面最上部，javascript放在页面最下面** 浏览器会在下载完成全部CSS之后才对整个页面进行渲染，因此最好的做法是将CSS放在页面最上面，让浏览器尽快下载CSS。 Javascript则相反，浏览器在加载javascript后立即执行，有可能会阻塞整个页面，造成页面显示缓慢，因此javascript最好放在页面最下面。

**应用服务器优化**

应用服务器也就是处理网站业务的服务器，网站的业务代码都部署在这里，主要优化方案有缓存、异步、集群等。

**1、合理使用缓存**

当网站遇到性能瓶颈时，第一个解决方案一般是缓存。在整个网站应用中，缓存几乎无处不在，无论是客户端，还是应用服务器，或是数据库服务器。在客户端和服务器的交互中，无论是数据、文件都可以缓存，合理使用缓存对网站性能优化非常重要。

缓存一般用来存放那些读写次数比较高，变化较少的数据，比如网站首页的信息、商品的信息等。应用程序读取数据时，一般是先从缓存中读取，如果读取不到或数据已失效，再访问磁盘数据库，并将数据再次写入缓存。

缓存的基本原理是将数据存储在相对有较高访问速度的存储介质中，比如内存。一方面缓存访问速度快，另一方面，如果缓存的数据是需要经过计算处理得到的，那使用缓存还可以减少服务器处理数据的计算时间。

使用缓存并不是没有缺陷：内存资源是比较宝贵的，不可能将所有数据都缓存，一般频繁修改的数据不建议使用缓存，这会导致数据不一致。

网站数据缓存一般遵循二八定律，即80%的访问都在20%的数据上。所以，一般将这20%的数据缓存，可以起到改善系统性能，提高服务器读取效率。

**2、异步操作**

使用消息队列将调用异步化，可以改善网站系统的性能。

在不使用消息队列的情况下，用户的请求直接写入数据库，在高并发的情况下，会对数据库造成非常大的压力，也会延迟响应时间。

在使用消息队列后，用户请求的数据会发送给消息队列服务器，消息队列服务器会开启进程，将数据异步写入数据库。消息队列服务器的处理速度远超过数据库，因此用户的响应延迟可得到改善。

消息队列可以将短时间内的高并发产生的事务消息，存储在消息队列中，从而提高网站的并发处理能力。在电商网站的促销活动中，合理使用消息队列，可以抵御短时间内用户高并发的冲击。

![异步消息队列](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152510.png)

**3、使用集群**

在网站高并发访问的情况下，使用负载均衡技术，可以为一个应用构建由多台服务器组成的服务器集群，将并发访问请求，分发到多台服务器上处理，避免单一服务器因负载过大，而导致响应延迟。

**4、代码优化**

网站的业务逻辑代码主要部署在应用服务器上，需要处理复杂的并发事务。合理优化业务代码，也可以改善网站性能。

任何web网站都会遇到多用户的并发访问，大型网站的并发用户会达到数万。每个用户请求都会创建一个独立的系统进程去处理。由于线程比进程更轻量，占用资源更少，所以，目前主流的web应用服务器都采用多线程的方式，处理并发用户的请求，因此，网站开发多数都是多线程编程。

使用多线程的另一个原因是服务器有多个CPU，现在手机都到了8核CPU的时代，一般的服务器至少是16核CPU，要想最大限度的使用这些CPU，必须启动多线程。

那么，启动多少线程合适呢？

启动线程数和CPU内核数量成正比，和IO等待时间成正比。如果都是计算型的任务，那么线程数最多不要超过CPU内核数，因为启动再多，CPU也来不及调用。如果任务是等待读写磁盘、网络响应，那么多启动线程会提高任务并发度，提高服务器性能。

或者用个简化的公式来描述：

启动线程数 = (任务执行时间/(任务执行事件 - IO等待时间)) * CPU内核数

**5、存储优化**

数据的读写是网站处理并发访问的另一瓶颈。使用缓存虽然可以解决一部分数据读写压力，但很多时候，磁盘仍然是系统最严重的瓶颈。而且磁盘是网站最重要的资产，磁盘的可用性和容错性也至关重要。

机械硬盘和固态硬盘 机械硬盘是目前最常用的硬盘，通过马达带动磁头到指定磁盘的位置访问数据，每次访问数据都需要移动磁头，在读取连续数据和随机访问上，磁头移动的次数相差巨大，因此机械硬盘的性能表现差别巨大，读写效率较低。而在网站应用中，大多数数据的访问都是随机的，在这种情况下，固态硬盘具有更高的性能。但目前固态硬盘在工艺上、数据可靠性上还有待提升，因此固态硬盘的使用尚未普及，从发展趋势看，取代机械硬盘应该是迟早的事情。

**总结：**

网站性能优化是在用户高并发访问，网站遇到问题时的解决方案。所以网站性能优化的主要内容是改善高并发用户访问情况下的网站响应速度。

网站性能优化的最终目的是改善用户的体验。但性能优化本身也是需要综合考虑的。比如说，性能提高一倍，服务器数量也要增加一倍，这样的优化是否可以考虑？

技术是由业务驱动的，离开业务的支撑，任何性能优化都是空中楼阁。