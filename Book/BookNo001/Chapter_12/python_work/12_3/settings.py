# -*- coding: utf-8 -*-
# @Time : 2022/03/20 14:20 下午
# @Author : HanChen
# @File : settings.py
# @Software: Sublime Text

# ------------------ example01 ------------------
class Settings():
    """存储《火箭移动》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 火箭的设置
        self.rocket_speed_factor = 1.5
# ------------------ example01 ------------------
