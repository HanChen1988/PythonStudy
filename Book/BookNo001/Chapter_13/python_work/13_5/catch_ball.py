# -*- coding: utf-8 -*-
# @Time : 2022/03/29 01:48 上午
# @Author : HanChen
# @File : catch_ball.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
13-5 抓球：创建一个游戏，在屏幕底端放置一个玩家可左右移动的角色。
    让一个球出现在屏幕顶端，且水平位置是随机的，并让这个球以固定的速度往下落。
    如果角色与球发生碰撞（表示将球抓住了），就让球消失。
    每当角色抓住球或球因抵达屏幕底端而消失后，都创建一个新球。
"""
import pygame
from pygame.sprite import Group
from settings import Settings
from grass import Grass
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch Ball")

    # 创建一片草地、一个足球编组
    grass = Grass(ai_settings, screen)
    footballs = Group()

    # 创建一个足球
    gf.create_football(ai_settings, screen, footballs)

    # 开始游戏的主循环
    while True:
        gf.check_events(grass)
        grass.update()
        gf.update_footballs(ai_settings, screen, grass, footballs)
        gf.update_screen(ai_settings, screen, grass, footballs)


run_game()
# ------------------ example01 ------------------
