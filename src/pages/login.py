"""封装登录页面的元素"""
from src.common import Base_page
from appium.webdriver.common import mobileby


class Login_page(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 我的按钮
    my_button = (by.ID, "com.codereview.reworldhaiwai:id/home2LottieMy")
    # 我的页面login/Registration按钮
    login_button = (by.ID, "com.codereview.reworldhaiwai:id/tx_tourish")
    # 手机输入框
    user = (by.ID, "com.codereview.reworldhaiwai:id/phone")
    # 密码输入框
    password = (by.ID, "com.codereview.reworldhaiwai:id/password")
    # 登录按钮
    enter_button = (by.ID, "com.codereview.reworldhaiwai:id/login")
    # 登录被踢按钮
    go_it_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")

    # 点击登录被踢按钮
    def click_go_it_button(self):
        self.find_element(*self.go_it_button).click()

    # 点击我的按钮
    def click_my_button(self):
        self.find_element(*self.my_button).click()

    # 点击login/Registration按钮
    def click_login_button(self):
        self.find_element(*self.login_button).click()

    # 点击输入框
    def click_user(self):
        self.find_element(*self.user).click()

    # 输入手机号
    def input_user(self, username):
        self.send_keys(username, *self.user)

    # 点击密码框
    def click_password(self):
        self.find_element(*self.password).click()

    # 输入密码
    def input_password(self, pwd):
        self.send_keys(pwd, *self.password)

    # 点击登录按钮
    def click_enter_button(self):
        self.find_element(*self.enter_button).click()