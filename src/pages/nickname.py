from src.common import Base_page
from appium.webdriver.common import mobileby


class nick(Base_page.Base_page):
    by = mobileby.MobileBy()
    # nickname按钮
    nickname_button = (by.ID, "com.codereview.reworldhaiwai:id/iv_borrow_record")
    # 输入框按钮
    input_button = (by.ID, "com.codereview.reworldhaiwai:id/ucenter_edittext")
    # 保存按钮
    save_button = (by.ID, "com.codereview.reworldhaiwai:id/save")

    # 点击nickname按钮
    def click_nickname_button(self):
        self.find_element(*self.nickname_button).click()

    # 点击输入框按钮
    def click_input_button(self):
        self.find_element(*self.input_button).click()

    # 输入框输入内容
    def send_input(self, info):
        self.send_keys(info, *self.input_button)

    # 点击保存按钮
    def click_save_button(self):
        self.find_element(*self.save_button).click()