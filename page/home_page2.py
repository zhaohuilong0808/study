"""
tpshop首页po文件
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle

"""
对象库层：
1.定义对象库层类，继承对象库层基类，记住导包
2.定义对象库层初始化方法，重写父类初始化方法
3.定义对象库层实例属性，当前py文件所代表的页面所有要操作的元素，都定义一个实例属性来表示
4.实例属性赋值，通过实例属性来管理定位信息，值的类型为元组(含2个元素)，一个元素为By类提供的定位方法，第二个元素为选中定位方式后所对应的值
5.定义对象库层实例方法，当前py文件所代表的页面所要用的元素，都定义一个对应的找元素实例方法
6.实现实例方法，通过继承方式调用基类中公用的元素定位方法，找到元素对象，并且返回
"""


class HonePage(BasePage):

    def __init__(self):
        super().__init__()
        # 登录超链接
        self.login_like = (By.CLASS_NAME, "red")
        # 搜索输入框
        self.search_input = (By.ID, "q")
        # 搜索按钮
        self.search_btn = (By.CSS_SELECTOR, ".ecsc-search-button")
        # 购物车链接
        self.cart_link = (By.CSS_SELECTOR, ".c-n")
        # 我的订单超链接
        self.my_order_like = (By.XPATH, '//*[text()="我的订单"]')

    # 找到登录超链接
    def find_login_like(self):
        return self.find_elt(self.login_like)

    # 找到搜索输入框
    def find_search_input(self):
        return self.find_elt(self.search_input)

    # 找到搜索按钮
    def find_search_btn(self):
        return self.find_elt(self.search_btn)

    # 找到去购物车页面元素
    def find_cart_like(self):
        return self.find_elt(self.cart_link)

    # 找到首页我的订单超链接元素
    def find_my_order_like(self):
        return self.find_elt(self.my_order_like)


"""
操作层：
1.定义操作层类，继承操作层基类，记住导包
2.定义操作层初始化方法，在初始化方法中创建对象库层对象，并定义一个实例属性来承接
3.定义操作层操作方法，当前py文件所代表的页面所有要操作的元素都定义一个操作方法，如输入、点击等，部分特殊的另外处理
4.实现操作层操作方法，通过第2步实例属性来调用对象库层的实例方法找到元素对象后执行常用元素操作方法
"""


class HoneHandle(BaseHandle):

    def __init__(self):
        # 创建对象库层对象
        self.home_page = HonePage()

    # 登录超链接点击
    def click_login_like(self):
        self.home_page.find_login_like().click()

    # 搜索输入框的输入
    def input_search_box(self, text):
        self.input_text(self.home_page.find_search_input(), text)

    # 搜索按钮点击
    def click_search_btn(self):
        self.home_page.find_search_btn().click()

    # 购物车点击操作
    def click_cart_link(self):
        self.home_page.find_cart_like().click()

    # 我的订单点击操作
    def click_order_like(self):
        self.home_page.find_my_order_like().click()


"""
1.定义业务层的类
2.定义初始化方法 ---->在初始化方法中,定义一个实例化属性来创建操作对象,方便后续调用实例方法
3.定义业务方法
4.实现业务方法
"""


class HomePeoxy:
    def __init__(self):
        self.home_handle = HoneHandle()

    # 1.跳转登录页面
    def test_login_page(self):
        # 在首页点击登录超链接
        self.home_handle.click_login_like()

    # 2.搜索商品
    def search_goods(self, text):
        # 1.输入商品搜索关键字
        self.home_handle.input_search_box(text)
        # 2.点击搜索按钮
        self.home_handle.click_search_btn()

    # 3.去购物车页面的操作方法
    def to_cart_page(self):
        # 1.点击购物车
        self.home_handle.click_cart_link()

    # 4.去订单管理页面的业务方法
    def to_order_page(self):
        # 1.在首页点击我的订单
        self.home_handle.click_order_like()
