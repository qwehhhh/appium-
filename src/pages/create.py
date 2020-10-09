from src.common import Base_page
from appium.webdriver.common import mobileby


class create(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 创造按钮
    create_button = (by.ID, "com.codereview.reworldhaiwai:id/iv_m")
    # 私密按钮
    private_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]")
    # 返回按钮
    close_button = (by.ID, "com.codereview.reworldhaiwai:id/iv_back")

    # 点击创造按钮
    def click_create_button(self):
        self.find_element(*self.create_button).click()

    # 点击私密按钮
    def click_private_button(self):
        self.find_element(*self.private_button).click()

    # 点击返回按钮
    def click_close_button(self):
        self.find_element(*self.close_button).click()