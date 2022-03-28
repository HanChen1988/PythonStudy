# -*- coding: utf-8 -*-
# @Time : 2022/03/24 21:33 下午
# @Author : HanChen
# @File : stars.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
13-1 星星：找一副星星图像，并在屏幕上显示一系列整齐排列的星星。
"""
import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Star")

    # 创建一个星星编组
    stars = Group()

    # 创建星群
    gf.create_stars(ai_settings, screen, stars)

    # 开始游戏的主循环
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, stars)


run_game()
# ------------------ example01 ------------------
