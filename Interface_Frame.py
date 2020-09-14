import unittest
import requests
import json
import HTMLTestRunner
import hashlib
from datetime import *


class port_test(unittest.TestCase):

    def setUp(self):
        # 测试固件
        self.url = "http://www.xxx.com"
    

    def test_login(self):
        # 用户登录测试代码
        password = hashlib.md5(b"#密码").hexdigest
        form = {"username":13111111111,"password":password,"serverid":000000000}
        r = requests.post(self.url,data = form)
        self.assertEqual(r.text["flag"],"success")


    def test_personinfo(self):
        # 信息查询测试代码
        form = requests.post(self.url,data = form)
        result = r.text["REALNAME"]
        self.assertEqual(result,"张三")


def suite():
    loginTestCase = unittest.makeSuite(port_test,"test")
    return loginTestCase


if __name__ == "__main__":
    now = date.today()
    report = open(str(now) + ".html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=report,title="测试报告",description="测试报告详情")
    runner.run(suite())
