# -*- coding: utf-8 -*-
# @Time : 2022/03/24 21:33 下午
# @Author : HanChen
# @File : continuous_drizzle.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
13-4 连绵细雨：修改为完成练习 13-3 而编写的代码，使得一行雨滴消失在屏幕底端后，屏幕顶端又出现一行新雨滴，并开始往下落。

    13-3 雨滴：寻找一副雨滴图像，并创建一系列整齐排列的雨滴。让这些雨滴往下落，直到到达屏幕底端后消失。
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
    pygame.display.set_caption("Continuous Drizzle")

    # 创建一个雨滴编组
    raindrops = Group()

    # 创建整群雨滴
    gf.create_raindrops(ai_settings, screen, raindrops)

    # 开始游戏的主循环
    while True:
        gf.check_events()
        gf.update_raindrops(ai_settings, raindrops)
        gf.update_screen(ai_settings, screen, raindrops)


run_game()
# ------------------ example01 ------------------
