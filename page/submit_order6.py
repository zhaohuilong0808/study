"""
提交订单---简化版
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, wait


# 1.把页面当成一个类
# 2.把页面要操作的元素当成类的实例属性
# 3.把页面操作方法当成类的实例方法
class SmoPage(BasePage):

    def __init__(self):
        super().__init__()
        # 提交订单
        self.submit_order = (By.CSS_SELECTOR, ".Sub-orders")
        # 提交订单结果
        self.submit_order_result = (By.CSS_SELECTOR, ".erhuh h3")
        # 收货地址
        self.recive_address = (By.XPATH, "//*[text()='寄送至']")

        # 将页面操作方法当成类的实例方法

    def test_submit_order(self):
        # WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*self.recive_address))
        wait(self.recive_address)
        # time.sleep(8)
        # 1.点击提交订单
        self.find_elt(self.submit_order).click()
        # 2.获取提交订单的结果并且返回
        return self.find_elt(self.submit_order_result).text
