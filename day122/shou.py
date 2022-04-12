#收集用例，生成报告

import os
import unittest

from BeautifulReport import BeautifulReport

dr = os.path.dirname(os.path.abspath(__file__)) #获取当前目录路径

s = unittest.TestLoader().discover(dr)          #收集当前目录下的用例

#执行测试用例，生成报告
bg = BeautifulReport(s)
bg.report("v1.0测试报告","py-unit.html")