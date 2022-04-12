import unittest

from day122.loginn import londin

# londin("123","213")
class Testlood(unittest.TestCase):
        #前置
    def setUp(self) -> None:
        print("每个用例执行前都要执行我")

        #后置清理
    def tearDown(self) -> None:
        print("每个用例执行后-清理")

    def test_denglu(self):
        actual = londin("zhang","123")
        print(actual)
        self.assertEqual("登陆成功",actual)

    def test_shibai(self):

        actul = londin("错误","111")
        self.assertEqual("登陆失败",actul)

