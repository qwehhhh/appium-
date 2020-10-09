# coding:utf-8
"""
配置手机信息
"""
from appium import webdriver
import time


class driver_info():
    def get_driver(self):
        try:
            self.android_dic = {}
            self.android_dic['platformName'] = 'Android'
            self.android_dic['platformVersion'] = '10'
            self.android_dic['devicesName'] = '7HX0219919013653'
            self.android_dic['appPackage'] = 'com.codereview.reworldhaiwai'
            self.android_dic['appActivity'] = 'com.locojoy.restart.MainActivity'
            self.android_dic['udid'] = '7HX0219919013653'
            self.android_dic['unicodeKeyboard'] = 'true'
            self.android_dic['resetKeyboard'] = 'true'
            self.android_dic['noReset'] = 'true'
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.android_dic)
            time.sleep(30)
            return self.driver
        except Exception as e:
            raise e