# -*- coding: utf-8 -*-
# @Time : 2022/04/07 16:27 下午
# @Author : HanChen
# @File : history_high_score.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
14-4 历史最高分：每当玩家关闭并重新开始游戏《外星人入侵》时，最高分都将被重重。
    请修复这个问题，调用 sys.exit()前将最高分写入文件，并当在 GameStats 中初始化最高分时从文件中读取它。
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
