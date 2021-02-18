## 1. 关于Flask

### 1.1 从 Hello World 开始

**Flask程序运行过程：**

所有Flask程序必须有一个程序实例。

Flask调用视图函数后，会将视图函数的返回值作为响应的内容，返回给客户端。一般情况下，响应内容主要是字符串和状态码。

当客户端想要获取资源时，一般会通过浏览器发起HTTP请求。此时，Web服务器使用WSGI（Web Server Gateway Interface）协议，把来自客户端的所有请求都交给Flask程序实例。WSGI是为 Python 语言定义的Web服务器和Web应用程序之间的一种简单而通用的接口，它封装了接受HTTP请求、解析HTTP请求、发送HTTP，响应等等的这些底层的代码和操作，使开发者可以高效的编写Web应用。

程序实例使用Werkzeug来做路由分发（URL请求和视图函数之间的对应关系）。根据每个URL请求，找到具体的视图函数。 在Flask程序中，路由的实现一般是通过程序实例的route装饰器实现。route装饰器内部会调用add_url_route()方法实现路由注册。

调用视图函数，获取响应数据后，把数据传入HTML模板文件中，模板引擎负责渲染响应数据，然后由Flask返回响应数据给浏览器，最后浏览器处理返回的结果显示给客户端。

**示例：**

新建文件hello.py:

```python
# 导入Flask类
from flask import Flask

#Flask类接收一个参数__name__
app = Flask(__name__)

# 装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    return 'Hello World'

# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run()
```

**查看视图函数中的路由：**

![装饰器路由](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151406.png)

**给路由传参示例：**

有时我们需要将同一类URL映射到同一个视图函数处理，比如：使用同一个视图函数 来显示不同用户的个人信息。

```python
# 路由传递的参数默认当做string处理，这里指定int，尖括号中冒号后面的内容是动态的
@app.route('/user/<int:id>')
def hello_itcast(id):
    return 'hello itcast %d' %id
```

![给路由传参](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151412.png)

**返回状态码示例：**

return后面可以自主定义状态码(即使这个状态码不存在)。当客户端的请求已经处理完成，由视图函数决定返回给客户端一个状态码，告知客户端这次请求的处理结果。

```python
@app.route('/')
def hello_itcast():
    return 'hello itcast',999
```

![999](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151419.png)

**abort函数:**

如果在视图函数执行过程中，出现了异常错误，我们可以使用abort函数立即终止视图函数的执行。通过abort函数，可以向前端返回一个http标准中存在的错误状态码，表示出现的错误信息。

使用abort抛出一个http标准中不存在的自定义的状态码，没有实际意义。如果abort函数被触发，其后面的语句将不会执行。其类似于python中raise。

```python
from flask import Flask,abort
@app.route('/')
def hello_itcast():
    abort(404)
    return 'hello itcast',999
```

**捕获异常：**

在Flask中通过装饰器来实现捕获异常，errorhandler()接收的参数为异常状态码。视图函数的参数，返回的是错误信息。

```python
@app.errorhandler(404)
def error(e):
    return '您请求的页面不存在了，请确认后再次访问！%s'%e
```

![捕获异常](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151426.png)

**重定向redirect示例**

```python
from flask import redirect
@app.route('/')
def hello_itcast():
    return redirect('http://www.itcast.cn')
```

![302](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151433.png)

**正则URL示例：**

正则URL是为了匹配指定的URL，而匹配指定的URL则可以达到限制访问，以及优化访问路径的目的。

```python
from flask import Flask
from werkzeug.routing import BaseConverter

class Regex_url(BaseConverter):
    def __init__(self,url_map,*args):
        super(Regex_url,self).__init__(url_map)
        self.regex = args[0]

app = Flask(__name__)
app.url_map.converters['re'] = Regex_url

@app.route('/user/<re("[a-z]{3}"):id>')
def hello_itcast(id):
    return 'hello %s' %id
```

**设置cookie和获取cookie**

```python
from flask import Flask,make_response
@app.route('/cookie')
def set_cookie():
    resp = make_response('this is to set cookie')
    resp.set_cookie('username', 'itcast')
    return resp
```

![设置cookie](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151440.png)

```python
from flask import Flask,request
#获取cookie
@app.route('/request')
def resp_cookie():
    resp = request.cookies.get('username')
    return resp
```

![获取cookie](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151447.png)

### 1.2 扩展

上下文：相当于一个容器，保存了Flask程序运行过程中的一些信息。

Flask中有两种上下文，请求上下文和应用上下文。

**请求上下文(request context)**

request和session都属于请求上下文对象。

request：封装了HTTP请求的内容，针对的是http请求。举例：user = request.args.get('user')，获取的是get请求的参数。

session：用来记录请求会话中的信息，针对的是用户信息。举例：session['name'] = user.id，可以记录用户信息。还可以通过session.get('name')获取用户信息。

**应用上下文(application context)**

current_app和g都属于应用上下文对象。

current_app:表示当前运行程序文件的程序实例。我们可以通过current_app.name打印出当前应用程序实例的名字。

![应用上下文](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151456.png)

g:处理请求时，用于临时存储的对象，每次请求都会重设这个变量。比如：我们可以获取一些临时请求的用户信息。

- 当调用app = Flask(_*name_*)的时候，创建了程序应用对象app；
- request 在每次http请求发生时，WSGI server调用Flask.call()；然后在Flask内部创建的request对象；
- app的生命周期大于request和g，一个app存活期间，可能发生多次http请求，所以就会有多个request和g。
- 最终传入视图函数，通过return、redirect或render_template生成response对象，返回给客户端。

**区别：** 请求上下文：保存了客户端和服务器交互的数据。 应用上下文：在flask程序运行过程中，保存的一些配置信息，比如程序文件名、数据库的连接、用户信息等。

**请求钩子**

在客户端和服务器交互的过程中，有些准备工作或扫尾工作需要处理，比如：在请求开始时，建立数据库连接；在请求结束时，指定数据的交互格式。为了让每个视图函数避免编写重复功能的代码，Flask提供了通用设施的功能，即请求钩子。

请求钩子是通过装饰器的形式实现，Flask支持如下四种请求钩子：

before_first_request：在处理第一个请求前运行。

before_request：在每次请求前运行。

after_request：如果没有未处理的异常抛出，在每次请求后运行。

teardown_request：在每次请求后运行，即使有未处理的异常抛出。

**Flask装饰器路由的实现：**

Flask有两大核心：Werkzeug和Jinja2。Werkzeug实现路由、调试和Web服务器网关接口。Jinja2实现了模板。

Werkzeug是一个遵循WSGI协议的python函数库。其内部实现了很多Web框架底层的东西，比如request和response对象；与WSGI规范的兼容；支持Unicode；支持基本的会话管理和签名Cookie；集成URL请求路由等。

Werkzeug库的routing模块负责实现URL解析。不同的URL对应不同的视图函数，routing模块会对请求信息的URL进行解析，匹配到URL对应的视图函数，以此生成一个响应信息。

routing模块内部有Rule类（用来构造不同的URL模式的对象）、Map类（存储所有的URL规则）、MapAdapter类（负责具体URL匹配的工作）；

**Flask-Script扩展命令行**

通过使用Flask-Script扩展，我们可以在Flask服务器启动的时候，通过命令行的方式传入参数。而不仅仅通过app.run()方法中传参，比如我们可以通过python hello.py runserver --host ip地址，告诉服务器在哪个网络接口监听来自客户端的连接。默认情况下，服务器只监听来自服务器所在计算机发起的连接，即localhost连接。

我们可以通过python hello.py runserver --help来查看参数。

```python
from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)

@app.route('/')
def index():
    return '床前明月光'

if __name__ == "__main__":
    manager.run()
```

![命令行](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151504.png)