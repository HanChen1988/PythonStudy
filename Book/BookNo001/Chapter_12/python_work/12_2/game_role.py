# -*- coding: utf-8 -*-
# @Time : 2022/03/20 12:55 下午
# @Author : HanChen
# @File : game_role.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
12-2 游戏角色：找一副你喜欢的游戏角色位图图像或将一副图像转换为位图。
    创建一个类，将该角色绘制到屏幕中央，并将该图像的背景色设置为屏幕背景色，或将屏幕背景色设置为该图像的背景色。
"""
import pygame

from settings import Settings
from doraemon import Doraemon
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Game Role")

    # 创建一个哆啦A梦
    doraemon = Doraemon(screen)

    # 开始游戏的主循环
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, doraemon)


run_game()
# ------------------ example01 ------------------
