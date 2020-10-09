# -*- coding:utf-8 -*-
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import logging
import logging.config

CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

android_dic = {"platformName": "Android",
               "deviceName": "7HX0219919013653",
               "platformVersion": "10",
               "udid": "7HX0219919013653",
               # "app": "D:\\reworld_2.0.1_debug20-08-01.apk",
               # Appium 自动决定获取安装app需要的权限
               # "autoGrantPermissions": "true",
               # "newCommandTimeout": "100",
               "appPackage": "com.locojoy.restart",
               "appActivity": "com.locojoy.restart.MainActivity",
               "automationName": "uiautomator2",
               "noReset": "true",
               "unicodeKeyboard": "true",
               "resetKeyboard": "true"}
logging.info('start app~~~~~~~')
driver = webdriver.Remote("http://localhost:4723/wd/hub", android_dic)
time.sleep(20)
"""toast元素定位"""
# driver.find_element_by_id("com.codereview.reworldhaiwai:id/home2LottieMy").click()
# time.sleep(1)
# driver.find_element_by_id("com.codereview.reworldhaiwai:id/tx_tourish").click()
# time.sleep(1)
# driver.find_element_by_id("com.codereview.reworldhaiwai:id/phone").send_keys("2250297167@qq.com")
# driver.find_element_by_id("com.codereview.reworldhaiwai:id/password").send_keys("qwe121235")
# driver.find_element_by_id("com.codereview.reworldhaiwai:id/login").click()
#
# error_message = "Incorrect account or password"
# message = '//*[@text = \'{}\']'.format(error_message)
# toast_element = WebDriverWait(driver, 5).until(lambda x:x.find_element_by_xpath(message))
# print(toast_element.text)

"""h5定位"""
TouchAction(driver).tap(x=931, y=2058).perform()
time.sleep(4)
# 打印H5界面的上下文
contexts = driver.contexts
print(contexts)
# 切换到webview页面
driver.switch_to.context('WEBVIEW_com.locojoy.restart')
# 点击购买
driver.find_element_by_xpath('//*[@id="index"]/div[4]/div[1]/div/div[1]/span').click()
time.sleep(2)
