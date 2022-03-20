# -*- coding: utf-8 -*-
# @Time : 2022/03/20 15:57 下午
# @Author : HanChen
# @File : alien_invasion.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
12-5 侧面射击：编写一个游戏，将一艘飞船放在屏幕左边，并允许玩家上下移动飞船。
    在玩家按空格键时，让飞船发射一颗在屏幕中向右穿行的子弹，并在子弹离开屏幕而消失后将其删除。
"""
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(screen, bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
# ------------------ example01 ------------------
