from src.common import Base_page
from appium.webdriver.common import mobileby
import time
from appium.webdriver.common.touch_action import TouchAction

class change(Base_page.Base_page):
    by = mobileby.MobileBy()
    # 换装按钮
    change_button = (by.ID, "com.codereview.reworldhaiwai:id/home2Image1")
    # 第一件衣服按钮——黑白条纹衣服
    black_white_clothes_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView")
    # 第三件蓝色警服按钮
    blue_police_clothes_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView")
    # 黑白骷髅衣服按钮
    Black_white_skeleton_button = (by.ID, "com.codereview.reworldhaiwai:id/home2Rl1")
    # 蓝黑背带裤衣服按钮
    blue_black_overalls_button = (by.ID, "com.codereview.reworldhaiwai:id/home2Rl3")
    # 鞋子按钮
    shoes_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ImageView")
    # 第一个鞋鬼冢虎按钮
    first_shoes_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView")
    # 第三个绿鞋按钮
    green_shoes_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView")
    # 第六双鞋按钮
    six_shoes_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.ImageView")
    # 第八双鞋子
    eight_shoes_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.FrameLayout/android.widget.ImageView")
    # Extra按钮
    extra_button = (by.ID, "com.codereview.reworldhaiwai:id/action_bar_root")
    # 第一个头发
    first_hair_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView")
    # 第三个头发
    third_hair_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView")
    # 第六个头发
    six_hair_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.ImageView")
    # 第八个头发
    eight_hair_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.FrameLayout/android.widget.ImageView")
    # 蝴蝶结按钮
    Bow_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ImageView")
    # 十字项链按钮
    ten_necklace_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView")
    # 小鸟按钮
    bird_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.ImageView")
    # 第一个裙子
    first_skirt_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout")
    # 第三个刀按钮
    third_knife_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout")\
    # 第六个两撇按钮
    six_skim_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.ImageView")
    # 第八个不带心的裙子
    eight_skirt_button = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.FrameLayout/android.widget.ImageView")
    # 返回按钮
    close_button = (by.XPATH,
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                    "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android"
                    ".widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget"
                    ".FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                    ".LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget"
                    ".HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout["
                    "1]/android.widget.ImageView")

    # 点击换装按钮
    def click_change_button(self):
        self.find_element(*self.change_button).click()

    # 点击第一件衣服按钮——黑白条纹衣服
    def click_black_white_clothes_button(self):
        self.find_element(*self.black_white_clothes_button).click()

    # 点击第三件蓝色警服按钮
    def click_blue_police_clothes_button(self):
        self.find_element(*self.blue_police_clothes_button).click()

    # 点击黑白骷髅衣服，需根据屏幕适配决定是否向下滑动页面
    def click_Black_white_skeleton_button(self):
        self.find_element(*self.Black_white_skeleton_button).click()

    # 点击蓝黑背带裤衣服按钮，需根据屏幕适配决定是否向下滑动页面
    def click_blue_black_overalls_button(self):
        self.find_element(*self.blue_black_overalls_button).click()

    # 点击鞋子按钮
    def click_shoes_button(self):
        self.find_element(*self.shoes_button).click()

    # 点击鬼冢虎鞋子
    def click_first_shoes_button(self):
        self.find_element(*self.first_shoes_button).click()

    # 点击第三双绿鞋
    def click_green_shoes_button(self):
        self.find_element(*self.green_shoes_button).click()

    # 点击第六双鞋
    def click_six_shoes_button(self):
        self.find_element(*self.six_shoes_button).click()

    # 点击第八双鞋子
    def click_eight_shoes_button(self):
        self.find_element(*self.eight_shoes_button).click()

    # 点击Extra按钮
    def click_extra_button(self):
        self.find_element(*self.extra_button).click()

    # 点击第一个头发
    def click_first_hair_button(self):
        self.find_element(*self.first_hair_button).click()

    # 点击第三个头发
    def click_third_hair_button(self):
        self.find_element(*self.third_hair_button).click()

    # 点击第六个头发
    def click_six_hair_button(self):
        self.find_element(*self.six_hair_button).click()

    # 点击第八个头发
    def click_eight_hair_button(self):
        self.find_element(*self.eight_hair_button).click()

    # 点击蝴蝶结按钮
    def click_Bow_button(self):
        self.find_element(*self.Bow_button).click()

    # 点击十字项链按钮
    def click_ten_necklace_button(self):
        self.find_element(*self.ten_necklace_button).click()

    # 点击小鸟按钮
    def click_bird_button(self):
        self.find_element(*self.bird_button).click()

    # 点击第一个裙子
    def click_first_skirt_button(self):
        self.find_element(*self.first_skirt_button).click()

    # 点击第三个刀按钮
    def click_third_knife_button(self):
        self.find_element(*self.third_knife_button).click()

    # 点击第六个两撇按钮
    def click_six_skim_button(self):
        self.find_element(*self.six_skim_button).click()

    # 点击第八个不带心的裙子
    def click_eight_skirt_button(self):
        self.find_element(*self.eight_skirt_button).click()

    # 华为pro30红衣服坐标
    def tap_huawei30red_clothes(self):
        time.sleep(10)
        # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
        # 188.8当前控件的X轴坐标位置，1069是屏幕手机最右下角X轴坐标位置
        # 红衣服的坐标
        rel_a1 = 728 / 1151
        # 941.5当前控件的Y轴坐标位置，1916是屏幕手机最右下角Y轴坐标位置
        rel_b1 = 1919 / 2398
        # 获取当前手机屏幕大小x,y
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print(x, y)
        # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
        self.driver.tap([(rel_a1 * x, rel_b1 * y)])

    # 华为pro30白衣服坐标
    def tap_huawei30white_clothes(self):
        time.sleep(10)
        # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
        # 188.8当前控件的X轴坐标位置，1069是屏幕手机最右下角X轴坐标位置
        # 红衣服的坐标
        rel_a1 = 1009 / 1151
        # 941.5当前控件的Y轴坐标位置，1916是屏幕手机最右下角Y轴坐标位置
        rel_b1 = 1927 / 2398
        # 获取当前手机屏幕大小x,y
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print(x, y)
        # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
        self.driver.tap([(rel_a1 * x, rel_b1 * y)])

    # 点击返回按钮
    def click_close_button(self):
        self.find_element(*self.close_button).click()


