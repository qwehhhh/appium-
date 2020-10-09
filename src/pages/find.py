from src.common import Base_page
from appium.webdriver.common import mobileby


class find_page(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 发现页按钮
    find_button = (by.ID, "com.codereview.reworldhaiwai:id/home2LottieHome")

    # 点击发现页按钮
    def click_find_button(self):
        self.find_element(*self.find_button).click()
