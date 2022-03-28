# -*- coding: utf-8 -*-
# @Time : 2022/03/25 23:04 下午
# @Author : HanChen
# @File : stars.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
13-2 更逼真的星星：为让星星的分布更逼真，可随机地放置星星。本书前面说过，可像下面这样来生成随机数：
    from random import randint
    random_number = randint(-10,10)
    上述代码返回一个 -10 和 10 之间的随机整数。在为完成练习 13-1 而编写的程序中，随机地调整每颗星星的位置。
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
