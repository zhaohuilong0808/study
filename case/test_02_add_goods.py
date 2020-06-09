import logging
import unittest

from BeautifulReport import BeautifulReport
from parameterized import parameterized

from config import BASE_PATH
from page.goods_info_page4 import GiProxy
from page.home_page2 import HomePeoxy
from page.serch_goods_page3 import SgProxy
from utils import DriverUtils, build_testData

"""
测试用例：
1.定义测试类，记得继承unittest.TestCase
2.定义类级别的初始化方法
3.在类级别的初始化方法中定义一个cls.driver实例属性，用来创建的获取浏览器驱动对象
4.在类级别的初始化方法中定义对应业务层的实例属性，要完成一个完整的测试用例步骤，可能需要调用多个PO业务层中的业务方法，才能
形成一个完整测试操作步骤。
5.定义类级别的销毁的方法，调用工具类中关闭浏览器驱动的方法
6.定义测试方法，按手工测试步骤才执行(调用)对应PO业务层中的业务方法，通过初始化方法中定义好实例属性来进行方法调用
7.设计断言
8.在data目录定义json格式的测试数据
9.引入参数化，针对测试方法进行调整，@parameterized.expand方法来调用工具文件中读取数据文件方法来获取测试数据
10.修改测试方法参数，测试数据有多少个定义多少个参数，同时修改输入数据地方，使用参数来进行代替
"""


class TestAddGoods(unittest.TestCase):

    def save_img(self, ing_name):  # 报错截图
        self.driver.get_screenshot_as_file("{}/{}.png".format("../img", ing_name))

    @classmethod
    def setUpClass(cls):
        # 1.打开浏览器# 2.最大化窗口和隐式等待
        cls.driver = DriverUtils.get_driver()
        # 实例化首页业务层对象
        cls.home_proxy = HomePeoxy()
        # 实例化搜索结果页的业务层对象
        cls.sg_proxy = SgProxy()
        # 实例化商品详细页业务层对象
        cls.gi_proxy = GiProxy()

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        DriverUtils.quit_driver()

    def setUp(self):
        self.driver.get("http://localhost/")

    # 固定装饰器 test_add_cart必须是方法名
    @parameterized.expand(build_testData(BASE_PATH + "/data/test_add_cart.json"))
    @BeautifulReport.add_test_img("test_add_cart")
    def test_add_cart(self, goods_name):
        """
        搜索小米,添加获取结果
        """
        logging.info("------------->开始执行加入购物车的测试用例")

        # 4.搜索关键字点击搜索
        self.home_proxy.search_goods(goods_name)
        # 5.搜索页点击第一个商品进去详细页
        self.sg_proxy.to_info_paga()
        # 6.加入购物车并获取加入结果
        msg = self.gi_proxy.test_add_goods()
        # 7.断言
        self.assertIn("添加成功", msg)
