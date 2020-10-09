"""滑动页面"""
import time


class swipe():
    def __init__(self, driver):
        self.driver = driver

    def swipe_up(self, n):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        x1 = int(x * 0.5)  # x坐标
        y1 = int(y * 0.9)  # 起始y坐标
        y2 = int(y * 0.25)  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2)
            time.sleep(2)

    def swipe_down(self, n):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        x1 = int(x * 0.5)  # x坐标
        y1 = int(y * 0.25)  # 起始y坐标
        y2 = int(y * 0.9)  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2)
            time.sleep(5)
