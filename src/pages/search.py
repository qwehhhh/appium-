from src.common import Base_page
from appium.webdriver.common import mobileby


class search(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 搜索框按钮
    search_box_button = (by.ID, "com.codereview.reworldhaiwai:id/searchLL")
    # 搜索输入框
    Input_search = (by.ID, "com.codereview.reworldhaiwai:id/searchEdit")
    # 搜索按钮
    search_button = (by.ID, "com.codereview.reworldhaiwai:id/searchTv")
    # 返回按钮
    return_button = (by.CLASS_NAME, "android.widget.ImageView")

    # 点击搜索框按钮
    def click_search_box_button(self):
        self.find_element(*self.search_box_button).click()

    # 点击搜索框
    def click_Input_search(self):
        self.find_element(*self.Input_search).click()

    # 输入内容
    def input_Input_search(self, content):
        self.send_keys(content, *self.Input_search)

    # 点击搜索按钮
    def click_search_button(self):
        self.find_element(*self.search_button).click()

    # 点击返回按钮
    def click_return_button(self):
        self.find_element(*self.return_button).click()


