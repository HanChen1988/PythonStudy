# -*- coding: utf-8 -*-
# @Time : 2022/03/24 21:33 下午
# @Author : HanChen
# @File : settings.py
# @Software: Sublime Text

# ------------------ example01 ------------------
class Settings():
    """存储《雨滴》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # 雨滴设置
        self.raindrop_speed_factor = 1
# ------------------ example01 ------------------
