"""
把需要输入的数据封装成函数，使用时使用ddt模块调用
"""
import random, string


def get_log_data():
    return [
        ['2250297167@qq.com', 'qwe123']
    ]


def sousuo():
    # 指定随机数长度
    r_num = 10
    # # 生成数字 + 字母（字符串序列）
    # token = string.ascii_letters + string.digits
    # '''
    #     string.ascii_letters:生成大小写字母（type:字符串）
    #     string.digits:生成数字（type:字符串）
    # '''
    #
    # # 随机选择 指定长度 随机码（字符串列表）
    # token = random.sample(token, r_num)
    #
    # # 生成 数字 + 字母 随机数
    # token = ''.join(token)

    # 加强版（一行代码）
    token = ''.join(random.sample(string.digits + string.ascii_letters, r_num))
    a = list(token)
    print(a)
    return [
        [a]
    ]


def nick():
    r_num = 10
    token = ''.join(random.sample(string.digits + string.ascii_letters, r_num))
    a = list(token)
    print(a)
    return [
        [a]
    ]


def summ():
    r_num = 10
    token = ''.join(random.sample(string.digits + string.ascii_letters, r_num))
    a = list(token)
    print(a)
    return [
        [a]
    ]


def pinglun():
    r_num = 10
    token = ''.join(random.sample(string.digits + string.ascii_letters, r_num))
    a = list(token)
    print(a)
    return [
        [a]
    ]
