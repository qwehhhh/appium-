# coding:utf-8
"""
配置全局参数
"""
import time,os
# 获取当前项目的存放路径
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# 测试用例代码存放路径
test_case_path = project_path + "\\src\\test_case"
# 测试报告的存放路径，并以当前时间作为报告的名称
report_path = project_path + "\\src\\report\\"
report_name = report_path + time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# img存放路径
img_path = project_path + "\\src\\img\\"
img_name = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 执行脚本路径
run_path = project_path + "\\test_run\\"

