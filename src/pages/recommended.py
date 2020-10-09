from src.common import Base_page
from appium.webdriver.common import mobileby


class recomm(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 推荐按钮
    recomm_button = (by.ID, "com.codereview.reworldhaiwai:id/iv_r")
    # 返回按钮
    close_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.ImageButton")

    # 点击推荐按钮
    def click_recomm_button(self):
        self.find_element(*self.recomm_button).click()

    # 点击返回按钮
    def click_close_button(self):
        self.find_element(*self.close_button).click()
