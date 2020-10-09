from src.common import Base_page
from appium.webdriver.common import mobileby


class my(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 我的按钮
    my_button = (by.ID, "com.codereview.reworldhaiwai:id/home2LottieMy")
    # 头像按钮
    Head_button = (by.ID, "com.codereview.reworldhaiwai:id/img_avtar")

    # 点击我的按钮
    def click_my_button(self):
        self.find_element(*self.my_button).click()

    # 点击头像按钮
    def click_Head_button(self):
        self.find_element(*self.Head_button).click()
