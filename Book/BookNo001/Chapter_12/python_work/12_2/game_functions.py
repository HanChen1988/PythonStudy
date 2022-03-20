# -*- coding: utf-8 -*-
# @Time : 2022/03/20 12:55 下午
# @Author : HanChen
# @File : game_functions.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import sys

import pygame


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, doraemon):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    doraemon.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
# ------------------ example01 ------------------
