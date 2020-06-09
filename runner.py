# 1.导包
import time
import unittest
from config import BASE_PATH
from utils import DriverUtils
from BeautifulReport import BeautifulReport

# 2.组织测试套件
suite = unittest.TestLoader().discover(BASE_PATH + "/case", "test*.py")

# 3.定义测试报告文件名
report_file = "{}-report".format(time.strftime("%Y%m%d%H%M%S"))

# 将关闭浏览器的开关关掉
DriverUtils.chck_open_key(False)

# 4.使用BeautifulReport批量运行用例生成测试报告
BeautifulReport(suite).report(filename=report_file, description="webAutoTest", log_path="./report")

# 将关闭浏览器开关打开
DriverUtils.chck_open_key(True)
DriverUtils.quit_driver()
