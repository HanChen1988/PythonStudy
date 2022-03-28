# -*- coding: utf-8 -*-
# @Time : 2022/03/29 01:48 上午
# @Author : HanChen
# @File : settings.py
# @Software: Sublime Text

# ------------------ example01 ------------------
class Settings():
    """存储《抓球》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # 草地设置
        self.grass_speed_factor = 4.5
        self.grass_limit = 3

        # 足球设置
        self.football_speed_factor = 1.5
# ------------------ example01 ------------------
