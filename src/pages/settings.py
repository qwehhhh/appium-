from src.common import Base_page
from appium.webdriver.common import mobileby


class setting(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 设置按钮
    setting_button = (by.ID, "com.codereview.reworldhaiwai:id/tv_setting")
    # login_out按钮
    login_out_button = (by.ID, "com.codereview.reworldhaiwai:id/btn_loginout")
    # comfirm按钮
    comfirm_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]")

    # 点击设置按钮
    def click_setting_button(self):
        self.find_element(*self.setting_button).click()

    # 点击login_out按钮
    def click_login_out_button(self):
        self.find_element(*self.login_out_button).click()

    # 点击comfirm按钮
    def click_comfirm_button(self):
        self.find_element(*self.comfirm_button).click()