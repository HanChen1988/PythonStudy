# -*- coding: utf-8 -*-
# @Time : 2022/03/29 01:48 上午
# @Author : HanChen
# @File : game_functions.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import sys
import pygame
from time import sleep
from random import randint

from football import Football


def check_keydown_events(event, grass):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        grass.moving_right = True
    elif event.key == pygame.K_LEFT:
        grass.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, grass):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        grass.moving_right = False
    elif event.key == pygame.K_LEFT:
        grass.moving_left = False


def check_events(grass):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, grass)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, grass)


def update_screen(ai_settings, screen, grass, footballs):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    grass.blitme()
    footballs.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def create_football(ai_settings, screen, footballs):
    """创建一个足球并将其放在当前行"""
    football = Football(ai_settings, screen)
    football_width = football.rect.width
    football.x = randint(football_width, 
                         (ai_settings.screen_width - football_width))
    football.rect.x = football.x
    footballs.add(football)


def grass_hit(ai_settings, screen, grass, footballs):
    """响应被足球撞到的草地"""
    # 清空足球列表
    footballs.empty()

    # 创建一群新的足球，并将草地放到屏幕底端中央
    create_football(ai_settings, screen, footballs)
    grass.center_grass()


def check_footballs_bottom(ai_settings, stats, screen, grass, footballs):
    """检查是否有足球到达了屏幕底端"""
    screen_rect = screen.get_rect()
    if stats.grasses_left > 0:
        for football in footballs.sprites():
            if football.rect.bottom >= screen_rect.bottom:
                # 将grasses_left减1
                stats.grasses_left -= 1

                # 像草地被撞到一样进行处理
                grass_hit(ai_settings, screen, grass, footballs)

                # 暂停
                sleep(0.5)
                break
    else:
        stats.game_active = False


def update_footballs(ai_settings, stats, screen, grass, footballs):
    """
    更新整群足球的位置
    """
    footballs.update()

    # 检测足球和草地之间的碰撞
    if pygame.sprite.spritecollideany(grass, footballs):
        grass_hit(ai_settings, screen, grass, footballs)

    # 检查是否有足球到达屏幕底端
    check_footballs_bottom(ai_settings, stats, screen, grass, footballs)
# ------------------ example01 ------------------
