import pytest
import unittest
from src.data.data import *
from ddt import data, unpack, ddt
from src.pages import login, find, search, game_details, often_play, change, my, nickname, summary, sex, birthday, \
    favorite, recommended, create, played, feedback, settings, info_push
from src.common.first_driverYaml import driver_cap
import time
from src.common.swipe_screen import swipe
from config.globalfile import img_path, img_name


@ddt
class Test(unittest.TestCase):
    """兼容性测试用例"""

    @classmethod
    def setUpClass(self):
        # 调用设备参数
        # driver = driver_config.driver_info()
        self.driver = driver_cap()
        # self.driver = driver_cap(udid='876188d', port='4725')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # @data数据在get_log_data()函数中，加*号因为@data读取类型是元组，加*是为了将get_log_data()返回的数据列表变为元组
    @data(*get_log_data())
    # 表示用来解压元组中的多个元素，实现一条测试用例实现多个测试点
    @unpack
    # 当用例报错是重新执行测试用例，用例执行成功后继续执行下一条用例，rerus代表次数
    @pytest.mark.flaky(rerus=3)
    def test01_login(self, username, password):
        """登录"""
        # 调用登录方法
        self.login = login.Login_page(self.driver)
        # 点击我的按钮
        self.login.click_my_button()
        try:
            # 点击登录/注册按钮
            self.login.click_login_button()
            # 点击输入框
            self.login.click_user()
            # 输入手机号
            self.login.input_user(username)
            # 点击密码框
            self.login.input_password(password)
            # 点击登录按钮
            self.login.click_enter_button()
            time.sleep(5)
            self.login.driver.get_screenshot_as_file(img_path + img_name + '--01登录.png')
        except:
            # 调用首页的方法
            self.login = find.find_page(self.driver)
            # 点击首页
            self.login.click_find_button()

    @pytest.mark.flaky(rerus=3)
    def test02_find(self):
        """点击首页"""
        # 调用首页的方法
        self.find = find.find_page(self.driver)
        # 点击首页
        self.find.click_find_button()
        self.find.driver.get_screenshot_as_file(img_path + img_name + '--02首页.png')

    @pytest.mark.flaky(rerus=3)
    def test03_change(self):
        """换装页"""
        # 调用方法
        self.change = change.change(self.driver)
        # 点击换装按钮
        self.change.click_change_button()
        time.sleep(10)
        # 点击第一件黑白条纹衣服
        self.change.click_black_white_clothes_button()
        # 点击鞋子按钮
        self.change.click_shoes_button()
        # 点击鬼冢虎
        self.change.click_first_shoes_button()
        # 点击Extra按钮
        self.change.click_extra_button()
        # 点击第一个头发
        self.change.click_first_hair_button()
        # 点击蝴蝶结按钮
        self.change.click_Bow_button()
        # 点击十字项链
        self.change.click_ten_necklace_button()
        # 点击小鸟按钮
        self.change.click_bird_button()
        # 点击第一个裙子
        self.change.click_first_skirt_button()
        # 点击返回按钮
        self.change.click_close_button()

    @data(*sousuo())
    @unpack
    @pytest.mark.flaky(rerus=3)
    def test04_search(self, contest):
        """搜索"""
        # 调用方法
        self.search = search.search(self.driver)
        # 点击搜索按钮
        self.search.click_search_box_button()
        # 点击搜索框
        self.search.click_Input_search()
        # 输入内容
        self.search.input_Input_search(contest)
        # 点击搜索
        self.search.click_search_button()
        time.sleep(3)
        self.search.driver.get_screenshot_as_file(img_path + img_name + '--03搜索.png')
        # 点击返回按钮
        self.search.click_return_button()
        time.sleep(1)

    def test05_info(self):
        """消息推送"""
        # 调用方法
        self.info = info_push.info_push(self.driver)
        # 点击铃铛按钮
        self.info.click_bell_button()
        # 点击版本更新按钮
        self.info.click_version_button()
        # 点击返回按钮
        self.info.click_close_button()
        # 点击游戏审核按钮
        self.info.click_game_button()
        self.info.driver.get_screenshot_as_file(img_path + img_name + '--04游戏审核.png')
        # 点击返回按钮
        self.info.click_close_button()
        # 点击站长通知按钮
        self.info.click_message_button()
        # 点击返回按钮
        self.info.click_close_button()
        # 点击评论按钮
        self.info.click_comment_button()
        # 点击返回按钮
        self.info.click_return_button()

    @data(*pinglun())
    @unpack
    @pytest.mark.flaky(rerus=3)
    def test06_game(self, comm):
        """游戏详情页"""
        # 调用方法
        self.game = game_details.game(self.driver)
        # 点击游戏详情页
        self.game.click_game_button()
        # 下滑至底部，有的屏幕需要下滑才能显示出收藏评论等按钮
        self.game = swipe(self.driver)
        self.game.swipe_up(1)
        # 调用方法
        self.game = game_details.game(self.driver)
        # 点击收藏
        self.game.click_collect_button()
        # 点击评论
        self.game.click_comment_button()
        # 点击评论框
        self.game.click_comment_button_boc()
        # 输入评论
        self.game.send_comment_button_boc_box(comm)
        # 点击发送按钮
        self.game.click_send_button()
        time.sleep(1)
        self.game.driver.get_screenshot_as_file(img_path + img_name + '--05评论.png')
        time.sleep(1)
        # 点击返回
        self.game.click_return_button()
        # 点击分享
        self.game.click_Share_button()
        # 点击关闭
        self.game.click_close_button()
        # # 点击举报
        # self.game.click_Feedback_button()
        # # 选择原因
        # self.game.click_Feedback_why_button()
        # # 点击提交
        # self.game.click_report_button()
        # 上滑至顶部，有的屏幕需要下滑才能显示出收藏评论等按钮
        self.game = swipe(self.driver)
        self.game.swipe_down(1)
        # 调用方法
        self.game = game_details.game(self.driver)
        # 点击返回按钮
        self.game.click_back_button()

    @pytest.mark.flaky(rerus=3)
    def test07_often(self):
        """常玩页"""
        # 调用方法
        self.often = often_play.often_play(self.driver)
        # 点击常玩按钮
        self.often.click_often_buton()
        self.often.driver.get_screenshot_as_file(img_path + img_name + '--06常玩.png')
        # 点击游戏按钮
        self.often.click_game_button()
        # 点击返回按钮
        self.often.click_close_button()

    @pytest.mark.flaky(rerus=3)
    def test08_my(self):
        """我的页面"""
        # 调用方法
        self.my = my.my(self.driver)
        # 点击我的按钮
        self.my.click_my_button()
        # 点击头像按钮
        self.my.click_Head_button()
        # self.my.driver.get_screenshot_as_file(img_path + img_name + '--08个人资料.png')

    @data(*nick())
    @unpack
    @pytest.mark.flaky(rerus=3)
    def test09_nickname(self, content):
        """修改昵称"""
        # 调用方法
        self.nick = nickname.nick(self.driver)
        # 点击nickname按钮
        self.nick.click_nickname_button()
        # 点击输入框
        self.nick.click_input_button()
        # 输入内容
        self.nick.send_input(content)
        # 点击保存按钮
        self.nick.click_save_button()

    @data(*summ())
    @unpack
    @pytest.mark.flaky(rerus=3)
    def test10_summary(self, content):
        """修改个性签名"""
        # 调用方法
        self.summ = summary.summ(self.driver)
        # 点击summary按钮
        self.summ.click_summ_button()
        # 点击个性签名框
        self.summ.click_signature_button()
        # 输入内容
        self.summ.input_signature_button(content)
        # 点击保存按钮
        self.summ.click_save_button()

    @pytest.mark.flaky(rerus=3)
    def test11_sex(self):
        """选择性别"""
        # 调用方法
        self.sex = sex.sex(self.driver)
        # 点击女生按钮
        self.sex.click_girl_button()
        # 点击男生按钮
        self.sex.click_boy_button()

    @pytest.mark.flaky(rerus=3)
    def test12_birth(self):
        """生日"""
        # 调用方法
        self.birth = birthday.birth(self.driver)
        # 点击生日按钮
        self.birth.click_birth_button()
        # 点击comfirm按钮
        self.birth.click_cofirm_button()
        # 点击返回按钮
        self.birth.click_close_button()
        # self.birth.driver.get_screenshot_as_file(img_path + img_name + '--12修改后的我的页.png')

    @pytest.mark.flaky(rerus=3)
    def test13_fav(self):
        """喜欢页面"""
        # 调用方法
        self.fav = favorite.fav(self.driver)
        # 点击喜欢按钮
        self.fav.click_fav_button()
        time.sleep(5)
        # 刷新页面,调用方法
        self.fav = swipe(self.driver)
        self.fav.swipe_down(1)
        # 调用方法
        self.fav = favorite.fav(self.driver)
        # 点击返回按钮
        self.fav.click_close_button()
        # self.fav.driver.get_screenshot_as_file(img_path + img_name + '--13喜欢页面执行成功.png')

    @pytest.mark.flaky(rerus=3)
    def test14_recomm(self):
        """推荐页面"""
        # 调用方法
        self.recomm = recommended.recomm(self.driver)
        # 点击推荐按钮
        self.recomm.click_recomm_button()
        # 点击返回按钮
        self.recomm.click_close_button()
        # self.recomm.driver.get_screenshot_as_file(img_path + img_name + '--14推荐页面执行成功.png')

    @pytest.mark.flaky(rerus=3)
    def test15_create(self):
        """创造页"""
        # 调用方法
        self.create = create.create(self.driver)
        # 点击创造按钮
        self.create.click_create_button()
        # 点击私密按钮
        self.create.click_private_button()
        # 点击返回按钮
        self.create.click_close_button()
        # self.create.driver.get_screenshot_as_file(img_path + img_name + '--15创造页面执行成功.png')

    @pytest.mark.flaky(rerus=3)
    def test16_play(self):
        """玩过页面"""
        # 调用页面
        self.play = played.play(self.driver)
        # 点击玩过按钮
        self.play.click_play_button()
        try:
            # 判断是否有edit按钮，如果有就进行操作
            self.play.click_edit_button()
            # 点击选中按钮
            self.play.click_selected_button()
            # 点击删除按钮
            self.play.click_delete_button()
            try:
                # 判断是否有comfirm按钮，如果有就点击comfirm按钮
                self.play.click_comfirm_button()
                # 点击返回按钮
                self.play.click_close_button()
                # self.play.driver.get_screenshot_as_file(img_path + img_name + '--16玩过页面执行成功.png')
            except:
                # 如果没有就点击返回按钮
                self.play.click_close_button()
                # self.play.driver.get_screenshot_as_file(img_path + img_name + '--16玩过页面执行成功.png')
        except:
            # 如果没有edit按钮就点击返回按钮
            self.play.click_close_button()
            # self.play.driver.get_screenshot_as_file(img_path + img_name + '--16玩过页面执行成功.png')

    @pytest.mark.flaky(rerus=3)
    def test17_feed(self):
        """反馈与建议"""
        # 调用页面
        self.feed = feedback.feed(self.driver)
        # 点击反馈按钮
        self.feed.click_feed_button()
        # 点击返回按钮
        self.feed.click_close_button()
        # self.feed.driver.get_screenshot_as_file(img_path + img_name + '--17反馈建议页面执行成功.png')

    @pytest.mark.flaky(rerus=3)
    def test18_setting(self):
        """设置页面"""
        # 调用方法
        self.setting = settings.setting(self.driver)
        # 点击设置按钮
        self.setting.click_setting_button()
        # 点击login_out按钮
        self.setting.click_login_out_button()
        # 点击comfirm按钮
        self.setting.click_comfirm_button()
        time.sleep(4)
        # self.setting.driver.get_screenshot_as_file(img_path + img_name + '--18退出账号登录界面.png')


if __name__ == '__main__':
    unittest.main()
