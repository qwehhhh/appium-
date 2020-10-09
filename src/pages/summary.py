from src.common import Base_page
from appium.webdriver.common import mobileby


class summ(Base_page.Base_page):
    by = mobileby.MobileBy()
    # summary按钮
    summ_button = (by.ID, "com.codereview.reworldhaiwai:id/rl_sign")
    # 个性签名框
    signature_button = (by.ID, "com.codereview.reworldhaiwai:id/edt_des")
    # 保存按钮
    save_button = (by.ID, "com.codereview.reworldhaiwai:id/save")

    # 点击summary按钮
    def click_summ_button(self):
        self.find_element(*self.summ_button).click()

    # 点击个性签名框
    def click_signature_button(self):
        self.find_element(*self.signature_button).click()

    # 输入内容
    def input_signature_button(self, info):
        self.send_keys(info, *self.signature_button)

    # 点击保存按钮
    def click_save_button(self):
        self.find_element(*self.save_button).click()