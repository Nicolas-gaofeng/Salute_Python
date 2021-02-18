# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db_python04"

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


class Role(db.Model):
    """用户角色/身份表"""
    __tablename__ = "tbl_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    users = db.relationship("User", backref="role")

    def __repr__(self):
        """定义之后，可以让显示对象的时候更直观"""
        return "Role object: name=%s" % self.name


# 表名的常见规范
# ihome -> ih_user   数据库名缩写_表名
# tbl_user  tbl_表名
# 创建数据库模型类
class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_users"  # 指明数据库的表名

    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，会默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        return "User object: name=%s" % self.name


if __name__ == '__main__':
    # 清除数据库里的所有数据
    db.drop_all()

    # 创建所有的表
    db.create_all()

    # 创建对象
    role1 = Role(name="admin")
    # session记录对象任务
    db.session.add(role1)
    # 提交任务到数据库中
    db.session.commit()

    role2 = Role(name="stuff")
    db.session.add(role2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)

    # 一次保存多条数据
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()









