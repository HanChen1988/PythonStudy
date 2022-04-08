# -*- coding: utf-8 -*-
# @Time : 2022/04/06 18:22 下午
# @Author : HanChen
# @File : alien_invasion.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
14-5 重构：找出执行了多项任务的函数和方法，对它们进行重构，以让代码高效而有序。
    例如，对于 check_bullet_alien_collisions()，
    将其中在外星人群被消灭干净时开始新等级的代码移到一个名为 start_new_level()的函数中；
    又比如，对于 Scoreboard 的方法`__init__()`，
    将其中调用四个不同方法的代码移到一个名为 prep_images()的方法中，以缩短方法`__init__()`。
    如果你重构了 check_play_button()，方法 prep_images()也可为 check_play_button()
    或 start_game() 提供帮助。

    注意：重构项目前，请阅读附录D，了解如果重构时引入了bug，如何将项目恢复到可正确运行的状态。
"""
import pygame
from pygame.sprite import Group
from scoreboard import Scoreboard
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
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens
                        , bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)


run_game()
# ------------------ example01 ------------------
