from src.common import Base_page
from appium.webdriver.common import mobileby


class game(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 游戏详情页按钮
    game_button = (by.ID, "com.codereview.reworldhaiwai:id/findBannerIcon")
    # 收藏按钮
    collect_button = (by.ID, "com.codereview.reworldhaiwai:id/imgCollect")
    # 评论按钮
    comment_button = (by.ID, "com.codereview.reworldhaiwai:id/imgComment")
    # 评论框按钮
    comment_button_boc = (by.ID, "com.codereview.reworldhaiwai:id/tv_content_t")
    # 输入评论框按钮
    comment_button_boc_box = (by.ID, "com.codereview.reworldhaiwai:id/et_content")
    # 发送按钮
    send_button = (by.ID, "com.codereview.reworldhaiwai:id/send")
    # 评论返回按钮
    return_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                               ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                               ".LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                               ".RelativeLayout/android.view.ViewGroup[1]/android.widget.ImageButton")
    # 分享按钮
    Share_button = (by.ID, "com.codereview.reworldhaiwai:id/fraShareTo")
    # 关闭按钮
    close_button = (by.ID, "com.codereview.reworldhaiwai:id/tv_cancel")
    # 举报按钮
    Feedback_button = (by.ID, "com.codereview.reworldhaiwai:id/fraFeedback")
    # 举报原因按钮
    Feedback_why_button = (by.ID, "com.codereview.reworldhaiwai:id/iv_one")
    # 提交按钮
    report_button = (by.ID, "com.codereview.reworldhaiwai:id/tv_report")
    # 页面返回按钮
    back_button = (by.ID, "com.codereview.reworldhaiwai:id/img_close")

    # 点击游戏详情页按钮
    def click_game_button(self):
        self.find_element(*self.game_button).click()

    # 点击收藏按钮
    def click_collect_button(self):
        self.find_element(*self.collect_button).click()

    # 点击评论按钮
    def click_comment_button(self):
        self.find_element(*self.comment_button).click()

    # 点击评论框
    def click_comment_button_boc(self):
        self.find_element(*self.comment_button_boc).click()

    # 输入评论框
    def send_comment_button_boc_box(self, info):
        self.send_keys(info, *self.comment_button_boc_box)

    # 点击发送按钮
    def click_send_button(self):
        self.find_element(*self.send_button).click()

    # 点击返回按钮
    def click_return_button(self):
        self.find_element(*self.return_button).click()

    # 点击分享按钮
    def click_Share_button(self):
        self.find_element(*self.Share_button).click()

    # 点击关闭按钮
    def click_close_button(self):
        self.find_element(*self.close_button).click()

    # 点击举报按钮
    def click_Feedback_button(self):
        self.find_element(*self.Feedback_button).click()

    # 点击举报原因按钮
    def click_Feedback_why_button(self):
        self.find_element(*self.Feedback_why_button).click()

    # 点击提交按钮
    def click_report_button(self):
        self.find_element(*self.report_button).click()

    # 点击返回按钮
    def click_back_button(self):
        self.find_element(*self.back_button).click()