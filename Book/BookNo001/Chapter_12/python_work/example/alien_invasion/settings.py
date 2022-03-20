# -*- coding: utf-8 -*-
# @Time : 2022/03/19 00:53 上午
# @Author : HanChen
# @File : settings.py
# @Software: Sublime Text

# ------------------ example01 ------------------
# class Settings():
#     """存储《外星人入侵》的所有设置的类"""
#
#     def __init__(self):
#         """初始化游戏的设置"""
#         # 屏幕设置
#         self.screen_width = 1200
#         self.screen_height = 800
#         self.bg_color = (230, 230, 230)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# class Settings():
#     """存储《外星人入侵》的所有设置的类"""
#
#     def __init__(self):
#         """初始化游戏的设置"""
#         # 屏幕设置
#         self.screen_width = 1200
#         self.screen_height = 800
#         self.bg_color = (230, 230, 230)
#
#         # 飞船的设置
#         self.ship_speed_factor = 1.5
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# class Settings():
#     """存储《外星人入侵》的所有设置的类"""
#
#     def __init__(self):
#         """初始化游戏的设置"""
#         # 屏幕设置
#         self.screen_width = 1200
#         self.screen_height = 800
#         self.bg_color = (230, 230, 230)
#
#         # 飞船的设置
#         self.ship_speed_factor = 1.5
#
#         # 子弹设置
#         self.bullet_speed_factor = 1
#         self.bullet_width = 3
#         self.bullet_height = 15
#         self.bullet_color = (60, 60, 60)
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
# ------------------ example04 ------------------
