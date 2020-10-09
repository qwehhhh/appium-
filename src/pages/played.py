from src.common import Base_page
from appium.webdriver.common import mobileby


class play(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 玩过按钮
    play_button = (by.ID, "com.codereview.reworldhaiwai:id/tv_recent")
    # edit按钮
    edit_button = (by.ID, "com.codereview.reworldhaiwai:id/tv_right")
    # 选中按钮
    selected_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView")
    # 删除按钮
    delete_button = (by.ID, "com.codereview.reworldhaiwai:id/tv_all_delete")
    # comfirm按钮
    comfirm_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]")
    # 返回按钮
    close_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.ImageView")

    # 点击玩过按钮
    def click_play_button(self):
        self.find_element(*self.play_button).click()

    # 点击edit按钮
    def click_edit_button(self):
        self.find_element(*self.edit_button).click()

    # 点击选中按钮
    def click_selected_button(self):
        self.find_element(*self.selected_button).click()

    # 点击删除按钮
    def click_delete_button(self):
        self.find_element(*self.delete_button).click()

    # 点击commfirm按钮
    def click_comfirm_button(self):
        self.find_element(*self.comfirm_button).click()

    # 点击返回按钮
    def click_close_button(self):
        self.find_element(*self.close_button).click()