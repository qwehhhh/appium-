import yaml
from appium import webdriver
import time
import os
# yaml路径
a = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(a, "driverInfo.yaml")
with open(yaml_path, "r", encoding='utf-8') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)


def driver_cap():
    try:
        android_dic = {}
        android_dic['platformName'] = data['platformName']
        android_dic['platformVersion'] = str(data['platformVersion'])
        android_dic['deviceName'] = data['deviceName']
        android_dic['skipServerInstallation'] = data['skipServerInstallation']
        android_dic['skipDeviceInitialization'] = data['skipDeviceInitialization']
        android_dic['appPackage'] = data['appPackage']
        android_dic['appActivity'] = data['appActivity']
        android_dic['unicodeKeyboard'] = data['unicodeKeyboard']
        android_dic['resetKeyboard'] = data['resetKeyboard']
        android_dic['noReset'] = data['noReset']
        android_dic['ip'] = data['ip']
        driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', android_dic)
        time.sleep(20)
        return driver
    except Exception as e:
        raise e

