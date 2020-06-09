"""
购物车页面--三次封装
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class Ctpage(BasePage):

    def __init__(self):
        super().__init__()
        # 1.定义操作元素属性
        # 全选复选框
        self.check_all = (By.CSS_SELECTOR, ".checkCartAll")
        # 2.去结算
        self.to_settle = (By.CSS_SELECTOR, ".gwc-qjs")

    # 2.定义找到元素的方法
    # 找单选框元素
    def find_check_all(self):
        return self.find_elt(self.check_all)

    # 找去结算的超链接
    def find_to_settle(self):
        return self.find_elt(self.to_settle)


# 操作层
class Cthandle(BaseHandle):

    def __init__(self):
        self.ct_page = Ctpage()

    # 判断勾选框是否勾选,勾选不点击.不勾选点击
    def click_all(self):
        if self.ct_page.find_check_all().is_selected() is False:
            self.ct_page.find_check_all().click()

    # 点击去结算
    def click_to_settle(self):
        self.ct_page.find_to_settle().click()


# 业务层
class CtProxy:

    def __init__(self):
        self.ct_handle = Cthandle()

    # 去结算页面
    def to_submit_page(self):
        # 1.勾选全选按钮
        self.ct_handle.click_all()
        # 2.点击去结算
        self.ct_handle.click_to_settle()
