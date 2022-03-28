# -*- coding: utf-8 -*-
# @Time : 2022/03/24 21:33 下午
# @Author : HanChen
# @File : game_functions.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import sys
import pygame

from raindrop import Raindrop


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


def update_screen(ai_settings, screen, raindrops):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    raindrops.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def get_number_raindrops_x(ai_settings, raindrop_width):
    """计算每行可容纳多少个雨滴"""
    available_space_x = ai_settings.screen_width - (2 * raindrop_width)
    number_raindrops_x = int(available_space_x / (2 * raindrop_width))
    return number_raindrops_x


def get_number_rows(ai_settings, raindrop_height):
    """计算屏幕可容纳多少行雨滴"""
    available_space_y = ai_settings.screen_height - (3 * raindrop_height)
    number_rows = int(available_space_y / (2 * raindrop_height))
    return number_rows


def create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number):
    """创建一个雨滴并将其放在当前行"""
    raindrop = Raindrop(ai_settings, screen)
    raindrop_width = raindrop.rect.x
    raindrop_height = raindrop.rect.y
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.y = raindrop_height + 2 * raindrop_height * row_number
    raindrop.rect.y = raindrop.y
    raindrops.add(raindrop)


def create_raindrops(ai_settings, screen, raindrops):
    """创建雨"""
    # 创建一个雨滴，并计算一行可容纳多少个雨滴
    # 雨滴间距为雨滴宽度
    raindrop = Raindrop(ai_settings, screen)
    raindrop_width = raindrop.rect.x
    raindrop_height = raindrop.rect.y
    number_raindrops_x = get_number_raindrops_x(ai_settings, raindrop_width)
    number_rows = get_number_rows(ai_settings, raindrop_height)

    # 创建雨
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            # 创建一个雨滴并将其加入当前行
            create_raindrop(ai_settings, screen, raindrops, raindrop_number,
                            row_number)


def update_raindrops(ai_settings, raindrops):
    """更新雨中所有雨滴的位置"""
    raindrops.update()

    # 删除已消失的雨滴
    for raindrop in raindrops.copy():
        if raindrop.rect.top >= ai_settings.screen_height:
            raindrops.remove(raindrop)
# ------------------ example01 ------------------
