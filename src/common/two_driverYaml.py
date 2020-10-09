import yaml
from appium import webdriver
import time
import os
import multiprocessing

devices_list = ['7HX0219919013653', '876188d']


def driver_cap(udid, port):
    # yaml路径
    a = os.path.dirname(os.path.realpath(__file__))
    yaml_path = os.path.join(a, "driverInfo.yaml")
    with open(yaml_path, "r", encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    try:
        android_dic = {}
        android_dic['platformName'] = data['platformName']
        android_dic['platformVersion'] = str(data['platformVersion'])
        android_dic['deviceName'] = data['deviceName']
        android_dic['appPackage'] = data['appPackage']
        android_dic['appActivity'] = data['appActivity']
        android_dic['udid'] = udid
        android_dic['unicodeKeyboard'] = data['unicodeKeyboard']
        android_dic['resetKeyboard'] = data['resetKeyboard']
        android_dic['noReset'] = data['noReset']
        android_dic['ip'] = data['ip']
        driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', android_dic)
        time.sleep(20)
        return driver
    except Exception as e:
        raise e


desired_process = []  # 存储多设备

for i in range(len(devices_list)):
    port = 4723 + 2 * i
    desired = multiprocessing.Process(target=driver_cap, args=(devices_list[i], port))
    desired_process.append(desired)  # 将设备添加到里面，ip和端口

if __name__ == '__main__':
    for desired in desired_process:
        desired.start()

    for desired in desired_process:
        desired.join()


