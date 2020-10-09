"""
测试报告生成
"""
from HTMLTestRunner_cn import HTMLTestRunner
import os
import sys
# print(sys.path)
sys.path.append('C:\\Users\\Administrator\\.jenkins\\workspace\\reworld_appiumtest\\Reworld\\test_run')
sys.path.append('C:\\Users\\Administrator\\.jenkins\\workspace\\reworld_appiumtest\\Reworld')
sys.path.append('D:\\pycharm\\PyCharm 2020.1\\plugins\\python\\helpers\\pycharm_display')
sys.path.append('D:\\python\\python37.zip')
sys.path.append('D:\\python\\DLLs')
sys.path.append('D:\\python\\lib')
sys.path.append('D:\\python')
sys.path.append('C:\\Users\\Administrator\\.jenkins\\workspace\\reworld_appiumtest\\Reworld\\venv')
sys.path.append('C:\\Users\\Administrator\\.jenkins\\workspace\\reworld_appiumtest\\Reworld\\venv\\lib\\site-packages')
sys.path.append('C:\\Users\\Administrator\\.jenkins\\workspace\\reworld_appiumtest\\Reworld\\venv\\lib\\site-packages\\win32')
sys.path.append('C:\\Users\\Administrator\\.jenkins\\workspace\\reworld_appiumtest\\Reworld\\venv\\lib\\site-packages\\win32\\lib')
sys.path.append('C:\\Users\\Administrator\\.jenkins\\workspace\\reworld_appiumtest\\Reworld\\venv\\lib\\site-packages\\Pythonwin')
sys.path.append('D:\\pycharm\\PyCharm 2020.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend')
sys.path.append('C:\\Users\\Administrator\\.jenkins\\workspace\\reworld_appiumtest\\Reworld\\test_run')
import unittest
from config.globalfile import report_name, test_case_path
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test*.py')
report = report_name + '.html'
with open(report, 'wb') as f:
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            title='Reworld自动化测试报告', )
    runner.run(suite)
# 关闭测试报告
f.close()
