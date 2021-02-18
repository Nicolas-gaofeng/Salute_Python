## 1. HTTP通信与Web框架

### 1.1 流程

客户端将请求打包成HTTP的请求报文（HTTP协议格式的请求数据）

采用TCP传输发送给服务器端

服务器接收到请求报文后按照HTTP协议进行解析

服务器根据解析后获知的客户端请求进行逻辑执行

服务器将执行后的结果封装成HTTP的响应报文（HTTP协议格式的响应数据）

采用刚才的TCP连接将响应报文发送给客户端

客户端按照HTTP协议解析响应报文获取结果数据

### 1.2 细节

客户端不一定是浏览器，也可以是PC软件、手机APP、程序

根据服务器端的工作，将其分为两部分：

服务器：与客户端进行tcp通信，接收、解析、打包、发送http格式数据

业务程序：根据解析后的请求数据执行逻辑处理，形成要返回的数据交给服务器

服务器与Python业务程序的配合使用WSGI协议

### 1.3 Web框架

能够被服务器调用起来，根据客户端的不同请求执行不同的逻辑处理形成要返回的数据的 程序

 

核心：实现路由和视图（业务逻辑处理）

 

### 1.4 框架的轻重

重量级的框架：为方便业务程序的开发，提供了丰富的工具、组件，如Django

 

轻量级的框架：只提供Web框架的核心功能，自由、灵活、高度定制，如Flask、Tornado

 

### 1.5 明确Web开发的任务

视图开发：根据客户端请求实现业务逻辑（视图）编写

模板、数据库等其他的都是为了帮助视图开发，不是必备的

## 2. 认识Flask

### 2.1 简介

Flask诞生于2010年，是Armin ronacher（人名）用Python语言基于Werkzeug工具箱编写的轻量级Web开发框架。它主要面向需求简单的小应用。

 

Flask本身相当于一个内核，其他几乎所有的功能都要用到扩展（邮件扩展Flask-Mail，用户认证Flask-Login），都需要用第三方的扩展来实现。比如可以用Flask-extension加入ORM、窗体验证工具，文件上传、身份验证等。Flask没有默认使用的数据库，你可以选择MySQL，也可以用NoSQL。其 WSGI 工具箱采用 Werkzeug（路由模块） ，模板引擎则使用 Jinja2 。

可以说Flask框架的核心就是Werkzeug和Jinja2。

Python最出名的框架要数Django，此外还有Flask、Tornado等框架。虽然Flask不是最出名的框架，但是Flask应该算是最灵活的框架之一，这也是Flask受到广大开发者喜爱的原因。

通过对比来了解Flask：

**Django**：

Python Web框架里比较有名当属Django，Django功能全面，它提供一站式解决方案，集成了MVT（Model-View-Template）和ORM，以及后台管理。但是缺点也很明显，它偏重。就像是一个装潢好的房子，它提供好了你要用的东西，直接拿来用就可以。

![Django的特点](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151231.jpg)

**Flask：**

Flask相对于Django而言是轻量级的Web框架。和Django不同，Flask轻巧、简洁，通过定制第三方扩展来实现具体功能。

可定制性，通过扩展增加其功能，这是Flask最重要的特点。Flask的两个主要核心应用是Werkzeug和模板引擎Jinja。

![Django的特点](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151241.jpg)

## 3. 关于Flask

### 3.1 了解框架

Flask作为Web框架，它的作用主要是为了开发Web应用程序。那么我们首先来了解下Web应用程序。Web应用程序 (World Wide Web)诞生最初的目的，是为了利用互联网交流工作文档。

![HTTP请求过程](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151326.png)

- 一切从客户端发起请求开始。
  - 所有Flask程序都必须创建一个程序实例。
  - 当客户端想要获取资源时，一般会通过浏览器发起HTTP请求。
  - 此时，Web服务器使用一种名为WEB服务器网关接口的WSGI（Web Server Gateway Interface）协议，把来自客户端的请求都交给Flask程序实例。
  - Flask使用Werkzeug来做路由分发（URL请求和视图函数之间的对应关系）。根据每个URL请求，找到具体的视图函数。
  - 在Flask程序中，路由一般是通过程序实例的装饰器实现。通过调用视图函数，获取到数据后，把数据传入HTML模板文件中，模板引擎负责渲染HTTP响应数据，然后由Flask返回响应数据给浏览器，最后浏览器显示返回的结果。

### 3.2 为什么要用Web框架？

web网站发展至今，特别是服务器端，涉及到的知识、内容，非常广泛。这对程序员的要求会越来越高。如果采用成熟，稳健的框架，那么一些基础的工作，比如，网络操作、数据库访问、会话管理等都可以让框架来处理，那么程序开发人员可以把精力放在具体的业务逻辑上面。使用Web框架开发Web应用程序可以降低开发难度，提高开发效率。

总结一句话：避免重复造轮子。

### 3.3 Flask框架的诞生：

Flask诞生于2010年，是Armin ronacher（人名）用Python语言基于Werkzeug工具箱编写的轻量级Web开发框架。它主要面向需求简单的小应用。

Flask本身相当于一个内核，其他几乎所有的功能都要用到扩展（邮件扩展Flask-Mail，用户认证Flask-Login），都需要用第三方的扩展来实现。比如可以用Flask-extension加入ORM、窗体验证工具，文件上传、身份验证等。Flask没有默认使用的数据库，你可以选择MySQL，也可以用NoSQL。其 WSGI 工具箱采用 Werkzeug（路由模块） ，模板引擎则使用 Jinja2 。

可以说Flask框架的核心就是Werkzeug和Jinja2。

Python最出名的框架要数Django，此外还有Flask、Tornado等框架。虽然Flask不是最出名的框架，但是Flask应该算是最灵活的框架之一，这也是Flask受到广大开发者喜爱的原因。

**Flask扩展包：**

- Flask-SQLalchemy：操作数据库；
- Flask-migrate：管理迁移数据库；
- Flask-Mail:邮件；
- Flask-WTF：表单；
- Flask-script：插入脚本；
- Flask-Login：认证用户状态；
- Flask-RESTful：开发REST API的工具；
- Flask-Bootstrap：集成前端Twitter Bootstrap框架；
- Flask-Moment：本地化日期和时间；

**Flask官方文档：**

[中文文档](http://docs.jinkan.org/docs/flask/)

[英文文档](http://flask.pocoo.org/docs/0.11/)

## 4. 安装环境

使用虚拟环境安装Flask，可以避免包的混乱和版本的冲突，虚拟环境是Python解释器的副本，在虚拟环境中你可以安装扩展包，为每个程序单独创建的虚拟环境，可以保证程序只能访问虚拟环境中的包。而不会影响系统中安装的全局Python解释器，从而保证全局解释器的整洁。

虚拟环境使用virtualenv创建，可以查看系统是否安装了virtualenv：

```bash
$ virtualenv --version
```

**安装虚拟环境(须在联网状态下)**

```bash
$ sudo pip install virtualenv
$ sudo pip install virtualenvwrapper
```

**安装完虚拟环境后，如果提示找不到mkvirtualenv命令，须配置环境变量：**

```bash
# 1、创建目录用来存放虚拟环境
mkdir $HOME/.virtualenvs

# 2、打开~/.bashrc文件，并添加如下：
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

# 3、运行
source ~/.bashrc
```

**创建虚拟环境(ubuntu里须在联网状态下)**

```bash
$ mkvirtualenv Flask_py
```

**进入虚拟环境**

```bash
$ workon Flask_py
```

**退出虚拟环境**

如果所在环境为真实环境，会提示deactivate：未找到命令

```bash
$ deactivate Flask_py
```

### 4.1 安装Flask

```bash
指定Flask版本安装
$ pip install flask==0.10.1
```

Mac系统：

```bash
$ easy_install flask==0.10.1
```

### 4.2 安装Flask依赖包

安装依赖包（须在虚拟环境中）： 依赖就是开发以及程序运行需要使用的环境的集合。包括软件、插件等。我们一般会把需要使用的依赖给保存在一个文件中，命名为requirements的txt文件。如果在其它环境中要运行我们的项目，直接通过指令可以一次性安装所有依赖。

安装依赖包（须在虚拟环境中）：

```bash
$ pip install -r requirements.txt
```

生成依赖包（须在虚拟环境中）：

```bash
$ pip freeze > requirements.txt
```

**在ipython中测试安装是否成功**

```bash
$ from flask import Flask
```

![安装成功](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151339.png)

![安装成功](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151343.png)