# -*- coding: utf-8 -*-
# @Time : 2022/03/24 21:33 下午
# @Author : HanChen
# @File : game_functions.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import sys
import pygame

from star import Star


def check_keydown_events(event):
    """响应按键"""
    if event.key == pygame.K_q:
        sys.exit()


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)


def update_screen(ai_settings, screen, stars):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def get_number_stars_x(ai_settings, star_width):
    """计算每行可容纳多少个星星"""
    available_space_x = ai_settings.screen_width - (2 * star_width)
    number_stars_x = int(available_space_x / (2 * star_width))
    return number_stars_x


def get_number_rows(ai_settings, star_height):
    """计算屏幕可容纳多少行星星"""
    available_space_y = ai_settings.screen_height - (2 * star_height)
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows


def create_star(screen, stars, star_number, row_number):
    """创建一个星星并将其放在当前行"""
    star = Star(screen)
    star_width = star.rect.x
    star_height = star.rect.y
    star.x = star_width + 2 * star_width * star_number
    star.rect.x = star.x
    star.y = star_height + 2 * star_height * row_number
    star.rect.y = star.y
    stars.add(star)


def create_stars(ai_settings, screen, stars):
    """创建星群"""
    # 创建一个星星，并计算一行可容纳多少个星星
    # 星星间距为星星宽度
    star = Star(screen)
    star_width = star.rect.x
    star_height = star.rect.y
    number_stars_x = get_number_stars_x(ai_settings, star_width)
    number_rows = get_number_rows(ai_settings, star_height)

    # 创建星群
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            # 创建一个星星并将其加入当前行
            create_star(screen, stars, star_number, row_number)
# ------------------ example01 ------------------
