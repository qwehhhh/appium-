from src.common import Base_page
from appium.webdriver.common import mobileby


class feed(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 反馈按钮
    feed_button = (by.ID, "com.codereview.reworldhaiwai:id/tv_feedback")
    # 返回按钮
    close_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton")

    # 点击反馈按钮
    def click_feed_button(self):
        self.find_element(*self.feed_button).click()

    # 点击返回
    def click_close_button(self):
        self.find_element(*self.close_button).click()