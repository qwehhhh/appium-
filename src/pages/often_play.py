from src.common import Base_page
from appium.webdriver.common import mobileby


class often_play(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 常玩按钮
    often_buton = (by.ID, "com.codereview.reworldhaiwai:id/tv_tav_title_dmg")
    # 游戏按钮
    game_button = (by.ID, "com.codereview.reworldhaiwai:id/historyRecommentBg")
    # 返回按钮
    close_button = (by.ID, "com.codereview.reworldhaiwai:id/img_close")

    # 点击常玩按钮
    def click_often_buton(self):
        self.find_element(*self.often_buton).click()

    # 点击游戏按钮
    def click_game_button(self):
        self.find_element(*self.game_button).click()

    # 点击返回按钮
    def click_close_button(self):
        self.find_element(*self.close_button).click()