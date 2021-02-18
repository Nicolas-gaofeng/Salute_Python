# coding:utf-8

import unittest
from login import app
import json


class TestLogin(unittest.TestCase):
    """定义测试案例"""
    def setUp(self):
        """在执行具体的测试方法前，先被调用"""
        # 可以使用python的http标准客户端进行测试
        # urllib  urllib2  requests

        # 使用flask提供的测试客户端进行测试
        self.client = app.test_client()

    def test_empty_name_password(self):
        """测试模拟场景，用户名或密码不完整"""
        # 使用客户端向后端发送post请求, data指明发送的数据，会返回一个响应对象
        response = self.client.post("/login", data={})

        # respoonse.data是响应体数据
        resp_json = response.data

        # 按照json解析
        resp_dict = json.loads(resp_json)

        # 使用断言进行验证
        self.assertIn("code", resp_dict)

        code = resp_dict.get("code")
        self.assertEqual(code, 1)

        # 测试只传name
        response = self.client.post("/login", data={"name": "admin"})

        # respoonse.data是响应体数据
        resp_json = response.data

        # 按照json解析
        resp_dict = json.loads(resp_json)

        # 使用断言进行验证
        self.assertIn("code", resp_dict)

        code = resp_dict.get("code")
        self.assertEqual(code, 1)

    def test_wrong_name_password(self):
        """测试用户名或密码错误"""
        # 使用客户端向后端发送post请求, data指明发送的数据，会返回一个响应对象
        response = self.client.post("/login", data={"name": "admin", "password": "itcast"})

        # respoonse.data是响应体数据
        resp_json = response.data

        # 按照json解析
        resp_dict = json.loads(resp_json)

        # 使用断言进行验证
        self.assertIn("code", resp_dict)

        code = resp_dict.get("code")
        self.assertEqual(code, 2)


if __name__ == '__main__':
    unittest.main()