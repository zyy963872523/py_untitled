import unittest

from 基础语法.lodin import londin

class Testlood(unittest.TestCase):

    def test_denglu(self):
        actual = londin("zhang","123")
        self.assertEqual("登陆成功",actual)
        print("123132")