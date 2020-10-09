from src.common import Base_page
from appium.webdriver.common import mobileby


class sex(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 女生按钮
    girl_button = (by.ID, "com.codereview.reworldhaiwai:id/rb_female")
    # 男生按钮
    boy_button = (by.ID, "com.codereview.reworldhaiwai:id/rb_male")

    # 点击女生按钮
    def click_girl_button(self):
        self.find_element(*self.girl_button).click()

    # 点击男生按钮
    def click_boy_button(self):
        self.find_element(*self.boy_button).click()
