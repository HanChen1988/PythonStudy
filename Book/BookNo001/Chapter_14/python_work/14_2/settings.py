# -*- coding: utf-8 -*-
# @Time : 2022/04/06 17:16 下午
# @Author : HanChen
# @File : settings.py
# @Software: Sublime Text

# ------------------ example01 ------------------
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 矩形设置
        self.rectangle_width = 18
        self.rectangle_height = 90
        self.rectangle_color = (60, 60, 60)

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.rectangle_speed_factor = 1

        # fleet_direction为1表示向下；为-1表示向上
        self.fleet_direction = 1
# ------------------ example01 ------------------
