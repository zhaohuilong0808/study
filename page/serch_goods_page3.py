"""
商品搜索页
"""
from selenium.webdriver.common.by import By

from base.base_page import BaseHandle, BasePage


# 对象库层
class SgPage(BasePage):
    # 定义初始化方法
    def __init__(self):
        super().__init__()

        # 加入购物车超链接
        # self.to_gi_like = (By.CSS_SELECTOR, '[onclick*="+104"]')
        self.to_gi_like = (By.XPATH, "//*[text()='加入购物车']")
    # 定义找到元素的实例方法
    def find_go_like(self):
        return self.find_elt(self.to_gi_like)


# 操作层
class Sghandle(BaseHandle):

    def __init__(self):
        self.sg_page = SgPage()

    # 加入购物车点击详情
    def click_gi_like(self):
        self.sg_page.find_go_like().click()


# 业务层
class SgProxy:

    def __init__(self):
        self.sg_handle = Sghandle()

    # 去购物车页面
    def to_info_paga(self):
        # 点击加入购物车链接
        self.sg_handle.click_gi_like()
