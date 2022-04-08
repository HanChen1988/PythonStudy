# -*- coding: utf-8 -*-
# @Time : 2022/04/07 17:46 下午
# @Author : HanChen
# @File : difficult_fire_practice.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
14-3 有一定难度的射击练习：以你为完成练习 14-2 而做的工作为基础，
    让标靶的移动速度随游戏进行而加快，并在玩家单击 Play按钮时将其重置为初始值。

    14-2 射击练习：创建一个矩形，它在屏幕右边缘以固定的速度上下移动。
        然后，在屏幕左边缘创建一艘飞船，玩家可上下移动该飞船，并射击前述矩形目标。
        添加一个用于开始游戏的 Play 按钮，在玩家三次未击中目标时结束游戏，并重新显示 Play 按钮，
        让玩家能够通过单击该按钮来重新开始游戏。
"""
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Difficult Fire Practice")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船、一个子弹编组和一个矩形编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    rectangles = Group()

    # 创建矩形
    gf.create_rectangle(ai_settings, screen, rectangles)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, rectangles,
                        bullets)

        if stats.game_active:
            ship.update()
            gf.update_rectangles(ai_settings, rectangles)
            gf.update_bullets(ai_settings, screen, stats, rectangles, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, rectangles, bullets,
                         play_button)


run_game()
# ------------------ example01 ------------------
