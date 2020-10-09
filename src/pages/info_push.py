from src.common import Base_page
from appium.webdriver.common import mobileby


class info_push(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 铃铛按钮
    bell_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")
    # 版本更新按钮
    version_button = (by.ID, "com.codereview.reworldhaiwai:id/ll_version")
    # 返回按钮
    close_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.ImageButton")
    # 游戏审核按钮
    game_button = (by.ID, "com.codereview.reworldhaiwai:id/ll_game")
    # 站点通知按钮
    message_button = (by.ID, "com.codereview.reworldhaiwai:id/ll_msg")
    # 评论按钮
    comment_button = (by.ID, "com.codereview.reworldhaiwai:id/hint2")
    # 返回按钮
    return_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView")

    # 点击铃铛按钮
    def click_bell_button(self):
        self.find_element(*self.bell_button).click()

    # 点击版本更新按钮
    def click_version_button(self):
        self.find_element(*self.version_button).click()

    # 点击返回按钮
    def click_close_button(self):
        self.find_element(*self.close_button).click()

    # 点击游戏审核按钮
    def click_game_button(self):
        self.find_element(*self.game_button).click()

    # 点击站点通知按钮
    def click_message_button(self):
        self.find_element(*self.message_button).click()

    # 点击评论按钮
    def click_comment_button(self):
        self.find_element(*self.comment_button).click()

    # 点击返回按钮
    def click_return_button(self):
        self.find_element(*self.return_button).click()