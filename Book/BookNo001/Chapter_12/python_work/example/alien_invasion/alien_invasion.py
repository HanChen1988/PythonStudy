# -*- coding: utf-8 -*-
# @Time : 2022/03/19 00:47 上午
# @Author : HanChen
# @File : alien_invasion.py
# @Software: Sublime Text

# ------------------ example01 ------------------
# import sys
#
# import pygame
#
#
# def run_game():
#     # 初始化游戏并创建一个屏幕对象
#     pygame.init()
#     screen = pygame.display.set_mode((1200, 800))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 开始游戏的主循环
#     while True:
#
#         # 监视键盘和鼠标事件
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         # 让最近绘制的屏幕可见
#         pygame.display.flip()
#
#
# run_game()
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# import sys
#
# import pygame
#
#
# def run_game():
#     # 初始化游戏并创建一个屏幕对象
#     pygame.init()
#     screen = pygame.display.set_mode((1200, 800))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 设置背景色
#     bg_color = (230, 230, 230)
#
#     # 开始游戏的主循环
#     while True:
#
#         # 监视键盘和鼠标事件
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         # 每次循环时都重绘屏幕
#         screen.fill(bg_color)
#
#         # 让最近绘制的屏幕可见
#         pygame.display.flip()
#
#
# run_game()
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# import sys
#
# import pygame
#
# from settings import Settings
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
#     # 开始游戏的主循环
#     while True:
#
#         # 监视键盘和鼠标事件
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         # 每次循环时都重绘屏幕
#         screen.fill(ai_settings.bg_color)
#
#         # 让最近绘制的屏幕可见
#         pygame.display.flip()
#
#
# run_game()
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# import sys
#
# import pygame
#
# from settings import Settings
# from ship import Ship
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
#     ship = Ship(screen)
#
#     # 开始游戏的主循环
#     while True:
#
#         # 监视键盘和鼠标事件
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#
#         # 每次循环时都重绘屏幕
#         screen.fill(ai_settings.bg_color)
#         ship.blitme()
#
#         # 让最近绘制的屏幕可见
#         pygame.display.flip()
#
#
# run_game()
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# import pygame
#
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
#     ship = Ship(screen)
#
#     # 开始游戏的主循环
#     while True:
#
#         # 监视键盘和鼠标事件
#         gf.check_events()
#
#         # 每次循环时都重绘屏幕
#         screen.fill(ai_settings.bg_color)
#         ship.blitme()
#
#         # 让最近绘制的屏幕可见
#         pygame.display.flip()
#
#
# run_game()
# ------------------ example05 ------------------

# print("*" * 20)

# ------------------ example06 ------------------
# import pygame
#
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
#     ship = Ship(screen)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events()
#         gf.update_screen(ai_settings, screen, ship)
#
#
# run_game()
# ------------------ example06 ------------------

# print("*" * 20)

# ------------------ example07 ------------------
# import pygame
#
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
#     ship = Ship(screen)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ship)
#         gf.update_screen(ai_settings, screen, ship)
#
#
# run_game()
# ------------------ example07 ------------------

# print("*" * 20)

# ------------------ example08 ------------------
# import pygame
#
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
#     ship = Ship(screen)
#
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ship)
#         ship.update()
#         gf.update_screen(ai_settings, screen, ship)
#
#
# run_game()
# ------------------ example08 ------------------

# print("*" * 20)

# ------------------ example09 ------------------
# import pygame
#
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
#     # 开始游戏的主循环
#     while True:
#         gf.check_events(ship)
#         ship.update()
#         gf.update_screen(ai_settings, screen, ship)
#
#
# run_game()
# ------------------ example09 ------------------

# print("*" * 20)

# ------------------ example10 ------------------
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
#         bullets.update()
#         gf.update_screen(ai_settings, screen, ship, bullets)
#
#
# run_game()
# ------------------ example10 ------------------

# print("*" * 20)

# ------------------ example11 ------------------
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
#         bullets.update()
#
#         # 删除已消失的子弹
#         for bullet in bullets.copy():
#             if bullet.rect.bottom <= 0:
#                 bullets.remove(bullet)
#         print(len(bullets))
#
#         gf.update_screen(ai_settings, screen, ship, bullets)
#
#
# run_game()
# ------------------ example11 ------------------

# print("*" * 20)

# ------------------ example12 ------------------
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
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
# ------------------ example12 ------------------
