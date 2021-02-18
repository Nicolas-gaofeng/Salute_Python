## 1. 数据库

### 1.1 数据库的设置

Web应用中普遍使用的是关系模型的数据库，关系型数据库把所有的数据都存储在表中，表用来给应用的实体建模，表的列数是固定的，行数是可变的。它使用结构化的查询语言。关系型数据库的列定义了表中表示的实体的数据属性。比如：商品表里有name、price、number等。 Flask本身不限定数据库的选择，你可以选择SQL或NOSQL的任何一种。也可以选择更方便的SQLALchemy，类似于Django的ORM。SQLALchemy实际上是对数据库的抽象，让开发者不用直接和SQL语句打交道，而是通过Python对象来操作数据库，在舍弃一些性能开销的同时，换来的是开发效率的较大提升。

SQLAlchemy是一个关系型数据库框架，它提供了高层的ORM和底层的原生数据库的操作。flask-sqlalchemy是一个简化了SQLAlchemy操作的flask扩展。

### 1.2 数据库安装

**安装服务端**

```
sudo apt-get install mysql-server
```

**安装客户端**

```
sudo apt-get install mysql-client
sudo apt-get install libmysqlclient-dev
```

### 1.3 数据库的基本命令

**登录数据库**

```
mysql -u root -p
```

**创建数据库，并设定编码**

```
create database <数据库名> charset=utf8;
```

**显示所有数据库**

```
show databases;
```

**在Flask中使用mysql数据库，需要安装一个flask-sqlalchemy的扩展。**

```
pip install flask-sqlalchemy
```

要连接mysql数据库，仍需要安装flask-mysqldb

```
pip install flask-mysqldb
```

**使用Flask-SQLAlchemy管理数据库**

使用Flask-SQLAlchemy扩展操作数据库，首先需要建立数据库连接。数据库连接通过URL指定，而且程序使用的数据库必须保存到Flask配置对象的SQLALCHEMY_DATABASE_URI键中。

**对比下Django和Flask中的数据库设置：**

Django的数据库设置：

![Django中设置数据库](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151744.png)

Flask的数据库设置：

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test3'

**常用的SQLAlchemy字段类型**

| 类型名       | python中类型      | 说明                                                |
| ------------ | ----------------- | --------------------------------------------------- |
| Integer      | int               | 普通整数，一般是32位                                |
| SmallInteger | int               | 取值范围小的整数，一般是16位                        |
| BigInteger   | int或long         | 不限制精度的整数                                    |
| Float        | float             | 浮点数                                              |
| Numeric      | decimal.Decimal   | 普通整数，一般是32位                                |
| String       | str               | 变长字符串                                          |
| Text         | str               | 变长字符串，对较长或不限长度的字符串做了优化        |
| Unicode      | unicode           | 变长Unicode字符串                                   |
| UnicodeText  | unicode           | 变长Unicode字符串，对较长或不限长度的字符串做了优化 |
| Boolean      | bool              | 布尔值                                              |
| Date         | datetime.date     | 时间                                                |
| Time         | datetime.datetime | 日期和时间                                          |
| LargeBinary  | str               | 二进制文件                                          |

**常用的SQLAlchemy列选项**

| 选项名      | 说明                                              |
| ----------- | ------------------------------------------------- |
| primary_key | 如果为True，代表表的主键                          |
| unique      | 如果为True，代表这列不允许出现重复的值            |
| index       | 如果为True，为这列创建索引，提高查询效率          |
| nullable    | 如果为True，允许有空值，如果为False，不允许有空值 |
| default     | 为这列定义默认值                                  |

**常用的SQLAlchemy关系选项**

| 选项名         | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| backref        | 在关系的另一模型中添加反向引用                               |
| primary join   | 明确指定两个模型之间使用的联结条件                           |
| uselist        | 如果为False，不使用列表，而使用标量值                        |
| order_by       | 指定关系中记录的排序方式                                     |
| secondary      | 指定多对多中记录的排序方式                                   |
| secondary join | 在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件 |

## 2. 数据库基本操作

在Flask-SQLAlchemy中，插入、修改、删除操作，均由数据库会话管理。会话用db.session表示。在准备把数据写入数据库前，要先将数据添加到会话中然后调用commit()方法提交会话。

数据库会话是为了保证数据的一致性，避免因部分更新导致数据不一致。提交操作把会话对象全部写入数据库，如果写入过程发生错误，整个会话都会失效。

数据库会话也可以回滚，通过db.session.rollback()方法，实现会话提交数据前的状态。

在Flask-SQLAlchemy中，查询操作是通过query对象操作数据。最基本的查询是返回表中所有数据，可以通过过滤器进行更精确的数据库查询。

**将数据添加到会话中示例：**

```base
user = User(name='python')
db.session.add(user)
db.session.commit()
```

**在视图函数中定义模型类**

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/Flask_test'

#设置每次请求结束后会自动提交数据库中的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    us = db.relationship('User', backref='role')

    #repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s'% self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s'%self.name
if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    db.session.add_all([ro1,ro2])
    db.session.commit()
    us1 = User(name='wang',email='wang@163.com',pswd='123456',role_id=ro1.id)
    us2 = User(name='zhang',email='zhang@189.com',pswd='201512',role_id=ro2.id)
    us3 = User(name='chen',email='chen@126.com',pswd='987654',role_id=ro2.id)
    us4 = User(name='zhou',email='zhou@163.com',pswd='456789',role_id=ro1.id)
    db.session.add_all([us1,us2,us3,us4])
    db.session.commit()
    app.run(debug=True)
```

**常用的SQLAlchemy查询过滤器**

|   过滤器    |                       说明                       |
| :---------: | :----------------------------------------------: |
|  filter()   |      把过滤器添加到原查询上，返回一个新查询      |
| filter_by() |    把等值过滤器添加到原查询上，返回一个新查询    |
|    limit    |         使用指定的值限定原查询返回的结果         |
|  offset()   |       偏移原查询返回的结果，返回一个新查询       |
| order_by()  | 根据指定条件对原查询结果进行排序，返回一个新查询 |
| group_by()  | 根据指定条件对原查询结果进行分组，返回一个新查询 |

**常用的SQLAlchemy查询执行器**

|      方法      |                     说明                     |
| :------------: | :------------------------------------------: |
|     all()      |         以列表形式返回查询的所有结果         |
|    first()     |  返回查询的第一个结果，如果未查到，返回None  |
| first_or_404() |  返回查询的第一个结果，如果未查到，返回404   |
|     get()      |   返回指定主键对应的行，如不存在，返回None   |
|  get_or_404()  |   返回指定主键对应的行，如不存在，返回404    |
|    count()     |              返回查询结果的数量              |
|   paginate()   | 返回一个Paginate对象，它包含指定范围内的结果 |

**创建表：**

```python
db.create_all()
```

**删除表**

```python
db.drop_all()
```

**插入一条数据**

```python
ro1 = Role(name='admin')
db.session.add(ro1)
db.session.commit()
#再次插入一条数据
ro2 = Role(name='user')
db.session.add(ro2)
db.session.commit()
```

**一次插入多条数据**

```python
us1 = User(name='wang',email='wang@163.com',pswd='123456',role_id=ro1.id)
us2 = User(name='zhang',email='zhang@189.com',pswd='201512',role_id=ro2.id)
us3 = User(name='chen',email='chen@126.com',pswd='987654',role_id=ro2.id)
us4 = User(name='zhou',email='zhou@163.com',pswd='456789',role_id=ro1.id)
db.session.add_all([us1,us2,us3,us4])
db.session.commit()
```

**查询:filter_by精确查询**

返回名字等于wang的所有人

```python
User.query.filter_by(name='wang').all()
```

![精确查询](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151801.png)

**first()返回查询到的第一个对象**

```python
User.query.first()
```

**all()返回查询到的所有对象**

```python
User.query.all()
```

![查询所有](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151808.png)

**filter模糊查询，返回名字结尾字符为g的所有数据。**

```python
User.query.filter(User.name.endswith('g')).all()
```

![结尾为g](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151819.png)

**get()，参数为主键，如果主键不存在没有返回内容**

```python
User.query.get()
```

**逻辑非，返回名字不等于wang的所有数据。**

```python
User.query.filter(User.name!='wang').all()
```

![逻辑非](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151825.png)

**逻辑与，需要导入and*，返回and*()条件满足的所有数据。**

```python
from sqlalchemy import and_
User.query.filter(and_(User.name!='wang',User.email.endswith('163.com'))).all()
```

![and_](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151837.png)

**逻辑或，需要导入or_**

```python
from sqlalchemy import or_
User.query.filter(or_(User.name!='wang',User.email.endswith('163.com'))).all()
```

![or_](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151852.png)

**not_ 相当于取反**

```python
from sqlalchemy import not_
User.query.filter(not_(User.name=='chen')).all()
```

![not_](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151858.png)

**查询数据后删除**

```python
user = User.query.first()
db.session.delete(user)
db.session.commit()
User.query.all()
```

**更新数据**

```python
user = User.query.first()
user.name = 'dong'
db.session.commit()
User.query.first()
```

![更新数据](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151905.png)

**使用update**

```python
User.query.filter_by(name='zhang').update({'name':'li'})
```

![更新数据](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151912.png)

关联查询示例：角色和用户的关系是一对多的关系，一个角色可以有多个用户，一个用户只能属于一个角色。

**查询角色的所有用户：**

```python
#查询roles表id为1的角色
ro1 = Role.query.get(1)
#查询该角色的所有用户
ro1.us
```

![查询admin的所有user](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151920.png)

**查询用户所属角色：**

```python
#查询users表id为3的用户
us1 = User.query.get(3)
#查询用户属于什么角色
us1.role
```

![查询用户所属角色](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151926.png)

## 3. 自定义模型类

**定义模型**

模型表示程序使用的数据实体，在Flask-SQLAlchemy中，模型一般是Python类，继承自db.Model，db是SQLAlchemy类的实例，代表程序使用的数据库。

类中的属性对应数据库表中的列。id为主键，是由Flask-SQLAlchemy管理。db.Column类构造函数的第一个参数是数据库列和模型属性类型。

**如下示例：定义了两个模型类，作者和书名。**

```
#coding=utf-8
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#设置连接数据
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test1'

#设置每次请求结束后会自动提交数据库中的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#设置成 True，SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#实例化SQLAlchemy对象
db = SQLAlchemy(app)

#定义模型类-作者
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    email = db.Column(db.String(64))
    au_book = db.relationship('Book',backref='author')
    def __str__(self):
        return 'Author:%s' %self.name

#定义模型类-书名
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    info = db.Column(db.String(32),unique=True)
    leader = db.Column(db.String(32))
    au_book = db.Column(db.Integer,db.ForeignKey('author.id'))
    def __str__(self):
        return 'Book:%s,%s'%(self.info,self.lead)
```

**创建表 db.create_all()**

![生成表](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151939.png)

**查看author表结构 desc author**

![查看author](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151944.png)

**查看books表结构 desc books**

![查看books](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151950.png)

```python
#coding=utf-8
from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/test1'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']='s'

db = SQLAlchemy(app)

#创建表单类，用来添加信息
class Append(Form):
    au_info = StringField(validators=[DataRequired()])
    bk_info = StringField(validators=[DataRequired()])
    submit = SubmitField(u'添加')


@app.route('/',methods=['GET','POST'])
def index():
    #查询所有作者和书名信息
    author = Author.query.all()
    book = Book.query.all()
    #创建表单对象
    form = Append()
    if form.validate_on_submit():
        #获取表单输入数据
        wtf_au = form.au_info.data
        wtf_bk = form.bk_info.data
        #把表单数据存入模型类
        db_au = Author(name=wtf_au)
        db_bk = Book(info=wtf_bk)
        #提交会话
        db.session.add_all([db_au,db_bk])
        db.session.commit()
        #添加数据后，再次查询所有作者和书名信息
        author = Author.query.all()
        book = Book.query.all()
        return render_template('index.html',author=author,book=book,form=form)
    else:
        if request.method=='GET':
            render_template('index.html', author=author, book=book,form=form)
    return render_template('index.html',author=author,book=book,form=form)

#删除作者
@app.route('/delete_author<id>')
def delete_author(id):
    #精确查询需要删除的作者id
    au = Author.query.filter_by(id=id).first()
    db.session.delete(au)
    #直接重定向到index视图函数
    return redirect(url_for('index'))

#删除书名
@app.route('/delete_book<id>')
def delete_book(id):
    #精确查询需要删除的书名id
    bk = Book.query.filter_by(id=id).first()
    db.session.delete(bk)
    #直接重定向到index视图函数
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    #生成数据
    au_xi = Author(name='我吃西红柿',email='xihongshi@163.com')
    au_qian = Author(name='萧潜',email='xiaoqian@126.com')
    au_san = Author(name='唐家三少',email='sanshao@163.com')
    bk_xi = Book(info='吞噬星空',lead='罗峰')
    bk_xi2 = Book(info='寸芒',lead='李杨')
    bk_qian = Book(info='飘渺之旅',lead='李强')
    bk_san = Book(info='冰火魔厨',lead='融念冰')
    #把数据提交给用户会话
    db.session.add_all([au_xi,au_qian,au_san,bk_xi,bk_xi2,bk_qian,bk_san])
    #提交会话
    db.session.commit()
    app.run(debug=True)
```

**生成数据后，查看数据：**

![生成数据](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218151958.png)

**模板页面示例：**

```python
   <h1>玄幻系列</h1>
    <form method="post">
        {{ form.csrf_token }}
        <p>作者：{{ form.au_info }}</p>
        <p>书名：{{ form.bk_info }}</p>
        <p>{{ form.submit }}</p>
    </form>
    <ul>
        <li>{% for x in author %}</li>
        <li>{{ x }}</li><a href='/delete_author{{ x.id }}'>删除</a>
        <li>{% endfor %}</li>
    </ul>
    <hr>
    <ul>
        <li>{% for x in book %}</li>
        <li>{{ x }}</li><a href='/delete_book{{ x.id }}'>删除</a>
        <li>{% endfor %}</li>
    </ul>
```

**添加数据后，查看数据：**

![添加数据](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152004.png)

## 4. 数据库迁移

在开发过程中，需要修改数据库模型，而且还要在修改之后更新数据库。最直接的方式就是删除旧表，但这样会丢失数据。

更好的解决办法是使用数据库迁移框架，它可以追踪数据库模式的变化，然后把变动应用到数据库中。

在Flask中可以使用Flask-Migrate扩展，来实现数据迁移。并且集成到Flask-Script中，所有操作通过命令就能完成。

为了导出数据库迁移命令，Flask-Migrate提供了一个MigrateCommand类，可以附加到flask-script的manager对象上。

首先要在虚拟环境中安装Flask-Migrate。

```python
pip install flask-migrate
```

**文件：database.py**

```python
#coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager

app = Flask(__name__)
manager = Manager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/Flask_test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#第一个参数是Flask的实例，第二个参数是Sqlalchemy数据库实例
migrate = Migrate(app,db) 

#manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
manager.add_command('db',MigrateCommand)

#定义模型Role
class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    def __repr__(self):
        return 'Role:'.format(self.name)

#定义用户
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    def __repr__(self):
        return 'User:'.format(self.username)
if __name__ == '__main__':
    manager.run()
```

**创建迁移仓库**

```base
#这个命令会创建migrations文件夹，所有迁移文件都放在里面。
python database.py db init
```

![数据迁移](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152014.png)

**创建迁移脚本**

自动创建迁移脚本有两个函数，upgrade()函数把迁移中的改动应用到数据库中。downgrade()函数则将改动删除。自动创建的迁移脚本会根据模型定义和数据库当前状态的差异，生成upgrade()和downgrade()函数的内容。对比不一定完全正确，有可能会遗漏一些细节，需要进行检查

```base
#创建自动迁移脚本
python database.py db migrate -m 'initial migration'
```

![迁移脚本](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152021.png)

**更新数据库**

```base
python database.py db upgrade
```

**回退数据库**

回退数据库时，需要指定回退版本号，由于版本号是随机字符串，为避免出错，建议先使用**python database.py db history**命令查看历史版本的具体版本号，然后复制具体版本号执行回退。

```base
python database.py db downgrade 版本号
```

![回退脚本](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152028.png)

## 5. Flask—Mail

在开发过程中，很多应用程序都需要通过邮件提醒用户，Flask的扩展包Flask-Mail通过包装了Python内置的smtplib包，可以用在Flask程序中发送邮件。

Flask-Mail连接到简单邮件协议（Simple Mail Transfer Protocol,SMTP）服务器，并把邮件交给服务器发送。

![邮箱认证](https://gitee.com/zgf1366/pic_store/raw/master/img/20210218152036.png)

如下示例，通过开启QQ邮箱SMTP服务设置，发送邮件。

```python
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
#配置邮件：服务器／端口／传输层安全协议／邮箱名／密码
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = '371673381@qq.com',
    MAIL_PASSWORD = 'goyubxohbtzfbidd',
)

mail = Mail(app)

@app.route('/')
def index():
 # sender 发送方，recipients 接收方列表
    msg = Message("This is a test ",sender='371673381@qq.com', recipients=['shengjun@itcast.cn','371673381@qq.com'])
    #邮件内容
    msg.body = "Flask test mail"
    #发送邮件
    mail.send(msg)
    print "Mail sent"
    return "Sent　Succeed"

if __name__ == "__main__":
    app.run()
```