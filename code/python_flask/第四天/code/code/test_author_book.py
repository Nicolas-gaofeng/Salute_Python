# coding:utf-8


import unittest
from author_book import Author, db, app


class TestDatabase(unittest.TestCase):
    """测试数据库的案例"""
    def setUp(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/flask_test"
        db.drop_all()
        db.create_all()

    def test_author(self):
        """测试添加作者的案例"""
        author = Author(name="itcast", email="itcast@itcast.cn")
        db.session.add(author)
        db.session.commit()

        ret_author = Author.query.filter_by(name="itcast").first()

        self.assertIsNotNone(ret_author)

        self.assertEqual(ret_author.name, "itcast")

    def tearDown(self):
        """在所有测试方法执行后，被调用"""
        # 清除记录的测试任务
        db.session.remove()
        # 清除数据库数据
        db.drop_all()


if __name__ == '__main__':
    unittest.main()