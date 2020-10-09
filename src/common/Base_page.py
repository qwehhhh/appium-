# coding:utf-8
"""
重写UI页面定位元素方法，所有元素设置为显性等待
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_page():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        """重写find_element方法，全部显性等待"""
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def send_keys(self, value, *loc):
        """重写输入方法，先清空所有输入框内容，然后在输入"""
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e