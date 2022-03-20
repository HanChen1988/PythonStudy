# -*- coding: utf-8 -*-
# @Time : 2022/03/20 12:34 下午
# @Author : HanChen
# @File : blue_sky.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
12-1 蓝色天空：创建一个背景为蓝色的 Pygame 窗口。
"""
import sys

import pygame


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")

    # 设置背景色
    bg_color = (0, 0, 255)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕
        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
# ------------------ example01 ------------------
