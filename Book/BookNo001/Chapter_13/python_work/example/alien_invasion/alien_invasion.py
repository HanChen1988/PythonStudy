# -*- coding: utf-8 -*-
# @Time : 2022/03/21 20:51 下午
# @Author : HanChen
# @File : alien_invasion.py
# @Software: Sublime Text

# ------------------ example01 ------------------
# import pygame
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# import game_functions as gf
#
#
# def run_game():
#     # 初始化pygame、设置和屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船
#     ship = Ship(ai_settings, screen)
#
#     # 创建一个用于存储子弹的编组
#     bullets = Group()
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         ship.update()
#         gf.update_bullets(bullets)
#         gf.update_screen(ai_settings, screen, ship, bullets)
#
#
# run_game()
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# import pygame
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# from alien import Alien
# import game_functions as gf
#
#
# def run_game():
#     # 初始化pygame、设置和屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船
#     ship = Ship(ai_settings, screen)
#
#     # 创建一个用于存储子弹的编组
#     bullets = Group()
#
#     # 创建一个外星人
#     alien = Alien(ai_settings, screen)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         ship.update()
#         gf.update_bullets(bullets)
#         gf.update_screen(ai_settings, screen, ship, alien, bullets)
#
#
# run_game()
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# import pygame
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# import game_functions as gf
#
#
# def run_game():
#     # 初始化pygame、设置和屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船、一个子弹编组和一个外星人编组
#     ship = Ship(ai_settings, screen)
#     bullets = Group()
#     aliens = Group()
#
#     # 创建外星人群
#     gf.create_fleet(ai_settings, screen, aliens)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         ship.update()
#         gf.update_bullets(bullets)
#         gf.update_screen(ai_settings, screen, ship, aliens, bullets)
#
#
# run_game()
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# import pygame
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# import game_functions as gf
#
#
# def run_game():
#     # 初始化pygame、设置和屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船、一个子弹编组和一个外星人编组
#     ship = Ship(ai_settings, screen)
#     bullets = Group()
#     aliens = Group()
#
#     # 创建外星人群
#     gf.create_fleet(ai_settings, screen, ship, aliens)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         ship.update()
#         gf.update_bullets(bullets)
#         gf.update_screen(ai_settings, screen, ship, aliens, bullets)
#
#
# run_game()
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# import pygame
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# import game_functions as gf
#
#
# def run_game():
#     # 初始化pygame、设置和屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船、一个子弹编组和一个外星人编组
#     ship = Ship(ai_settings, screen)
#     bullets = Group()
#     aliens = Group()
#
#     # 创建外星人群
#     gf.create_fleet(ai_settings, screen, ship, aliens)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         ship.update()
#         gf.update_bullets(bullets)
#         gf.update_aliens(aliens)
#         gf.update_screen(ai_settings, screen, ship, aliens, bullets)
#
#
# run_game()
# ------------------ example05 ------------------

# print("*" * 20)

# ------------------ example06 ------------------
# import pygame
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# import game_functions as gf
#
#
# def run_game():
#     # 初始化pygame、设置和屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船、一个子弹编组和一个外星人编组
#     ship = Ship(ai_settings, screen)
#     bullets = Group()
#     aliens = Group()
#
#     # 创建外星人群
#     gf.create_fleet(ai_settings, screen, ship, aliens)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         ship.update()
#         gf.update_bullets(bullets)
#         gf.update_aliens(ai_settings, aliens)
#         gf.update_screen(ai_settings, screen, ship, aliens, bullets)
#
#
# run_game()
# ------------------ example06 ------------------

# print("*" * 20)

# ------------------ example07 ------------------
# import pygame
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# import game_functions as gf
#
#
# def run_game():
#     # 初始化pygame、设置和屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船、一个子弹编组和一个外星人编组
#     ship = Ship(ai_settings, screen)
#     bullets = Group()
#     aliens = Group()
#
#     # 创建外星人群
#     gf.create_fleet(ai_settings, screen, ship, aliens)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         ship.update()
#         gf.update_bullets(aliens, bullets)
#         gf.update_aliens(ai_settings, aliens)
#         gf.update_screen(ai_settings, screen, ship, aliens, bullets)
#
#
# run_game()
# ------------------ example07 ------------------

# print("*" * 20)

# ------------------ example08 ------------------
# import pygame
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# import game_functions as gf
#
#
# def run_game():
#     # 初始化pygame、设置和屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船、一个子弹编组和一个外星人编组
#     ship = Ship(ai_settings, screen)
#     bullets = Group()
#     aliens = Group()
#
#     # 创建外星人群
#     gf.create_fleet(ai_settings, screen, ship, aliens)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         ship.update()
#         gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
#         gf.update_aliens(ai_settings, aliens)
#         gf.update_screen(ai_settings, screen, ship, aliens, bullets)
#
#
# run_game()
# ------------------ example08 ------------------

# print("*" * 20)

# ------------------ example09 ------------------
# import pygame
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# import game_functions as gf
#
#
# def run_game():
#     # 初始化pygame、设置和屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船、一个子弹编组和一个外星人编组
#     ship = Ship(ai_settings, screen)
#     bullets = Group()
#     aliens = Group()
#
#     # 创建外星人群
#     gf.create_fleet(ai_settings, screen, ship, aliens)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         ship.update()
#         gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
#         gf.update_aliens(ai_settings, ship, aliens)
#         gf.update_screen(ai_settings, screen, ship, aliens, bullets)
#
#
# run_game()
# ------------------ example09 ------------------

# print("*" * 20)

# ------------------ example10 ------------------
# import pygame
# from pygame.sprite import Group
# from settings import Settings
# from game_stats import GameStats
# from ship import Ship
# import game_functions as gf
#
#
# def run_game():
#     # 初始化pygame、设置和屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一个用于存储游戏统计信息的实例
#     stats = GameStats(ai_settings)
#
#     # 创建一艘飞船、一个子弹编组和一个外星人编组
#     ship = Ship(ai_settings, screen)
#     bullets = Group()
#     aliens = Group()
#
#     # 创建外星人群
#     gf.create_fleet(ai_settings, screen, ship, aliens)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ai_settings, screen, ship, bullets)
#         ship.update()
#         gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
#         gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
#         gf.update_screen(ai_settings, screen, ship, aliens, bullets)
#
#
# run_game()
# ------------------ example10 ------------------

# print("*" * 20)

# ------------------ example11 ------------------
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
# ------------------ example11 ------------------
