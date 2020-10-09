from src.common import Base_page
from appium.webdriver.common import mobileby


class birth(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 生日按钮
    birth_button = (by.ID, "com.codereview.reworldhaiwai:id/iv_v4r")
    # comfirm按钮
    cofirm_button = (by.ID, "com.codereview.reworldhaiwai:id/tv_finish")
    # 返回按钮
    close_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton")

    # 点击生日按钮
    def click_birth_button(self):
        self.find_element(*self.birth_button).click()

    # 点击comfirmann
    def click_cofirm_button(self):
        self.find_element(*self.cofirm_button).click()

    # 点击返回按钮
    def click_close_button(self):
        self.find_element(*self.close_button).click()