# 1.导包
import logging
import time
import unittest
from page.cat_page5 import CtProxy
from page.home_page2 import HomePeoxy
from page.order_page7 import OrderPage
from page.order_pay_page8 import OpPage
from page.submit_order6 import SmoPage
from utils import DriverUtils


# 2.定义测试类

class TestSubmit_Order(unittest.TestCase):
    def save_img(self, ing_name):  # 报错截图
        self.driver.get_screenshot_as_file("{}/{}.png".format("../img", ing_name))

    # a.定义类级别方法打开浏览器
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_driver()

        # b.在类级别方法中需要创建好对应要使用的业务层类对象
        cls.home_proxy = HomePeoxy()
        cls.cart_proxy = CtProxy()
        cls.subo_page = SmoPage()
        # 实例化我的订单页面的对象
        cls.order_page = OrderPage()
        # 实例化支付订单页面对象
        cls.op_page = OpPage()

    # c.恢复方法级别初始化fixture
    def setUp(self):
        self.driver.get("http://localhost/")

    # 3.定义测试方法
    def test_01_submit_order(self):
        """
        点击购物车,结算,提交订单,打印结果
        """
        # d.连续调用多个业务层的实例方法.组织完整文案测试用例的操作步骤
        logging.info("-------->执行提交订单测试用例")
        # 1.在首页点击我的购物车
        self.home_proxy.to_cart_page()
        # 2.在购物车点击去结算
        self.cart_proxy.to_submit_page()
        # 3.在提交订单页面点击获取提交结果
        mag = self.subo_page.test_submit_order()
        # e.进行断言
        self.assertIn("订单提交成功", mag)

    # 4.测试订单支付
    def test_02_ordder_pay(self):
        """
        订单支付
        """
        # a.点击我的订单
        self.home_proxy.to_order_page()
        # b.点击待付款和立即支付
        self.order_page.to_order_pay_page()
        # c.选中支付方式确认支付
        msg = self.op_page.test_pay()
        # d.断言
        self.assertIn("我们将在第一时间", msg)

    # f.定义类级别销毁的fixture,关闭浏览器
    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_driver()
