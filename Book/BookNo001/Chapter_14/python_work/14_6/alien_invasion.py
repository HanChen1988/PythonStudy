# -*- coding: utf-8 -*-
# @Time : 2022/04/08 11:59 上午
# @Author : HanChen
# @File : alien_invasion.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
14-6 扩展游戏《外星人入侵》：想想如何扩展游戏《外星人入侵》。
    例如，可让外星人也能够向飞船射击，或者添加盾牌，让飞船躲到它后面，使得只有从两边射来的子弹才能摧毁飞船。
    另外，还可以使用像 pygame.mixer 这样的模块来添加音效，如爆炸声和射击声。
"""
import pygame
from pygame.sprite import Group
from pygame.mixer import Sound

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

    # 创建一个子弹音、一个爆炸音
    bullet_audio = Sound(ai_settings.bullet_audio_file_path)
    boom_audio = Sound(ai_settings.boom_audio_file_path)

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens
                        , bullets, bullet_audio)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets, boom_audio)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets, boom_audio)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)


run_game()
# ------------------ example01 ------------------
