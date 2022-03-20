# -*- coding: utf-8 -*-
# @Time : 2022/03/19 10:57 上午
# @Author : HanChen
# @File : game_functions.py
# @Software: Sublime Text

# ------------------ example01 ------------------
# import sys
#
# import pygame
#
# def check_events():
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# import sys
#
# import pygame
#
#
# def check_events():
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#
# def update_screen(ai_settings, screen, ship):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重绘屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# import sys
#
# import pygame
#
#
# def check_events(ship):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 # 向右移动飞船
#                 ship.rect.centerx += 1
#
#
# def update_screen(ai_settings, screen, ship):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重绘屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# import sys
#
# import pygame
#
#
# def check_events(ship):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = True
#
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = False
#
#
# def update_screen(ai_settings, screen, ship):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重绘屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# import sys
#
# import pygame
#
#
# def check_events(ship):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = True
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = True
#
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = False
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = False
#
#
# def update_screen(ai_settings, screen, ship):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重绘屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()
# ------------------ example05 ------------------

# print("*" * 20)

# ------------------ example06 ------------------
# import sys
#
# import pygame
#
#
# def check_keydown_events(event, ship):
#     """响应按键"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = True
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = True
#
#
# def check_keyup_events(event, ship):
#     """响应松开"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = False
#
#
# def check_events(ship):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             check_keydown_events(event, ship)
#         elif event.type == pygame.KEYUP:
#             check_keyup_events(event, ship)
#
#
# def update_screen(ai_settings, screen, ship):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重绘屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()
# ------------------ example06 ------------------

# print("*" * 20)

# ------------------ example07 ------------------
# import sys
#
# import pygame
#
# from bullet import Bullet
#
#
# def check_keydown_events(event, ai_settings, screen, ship, bullets):
#     """响应按键"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = True
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = True
#     elif event.key == pygame.K_SPACE:
#         # 创建一颗子弹，并将其加入到编组bullets中
#         new_bullet = Bullet(ai_settings, screen, ship)
#         bullets.add(new_bullet)
#
#
# def check_keyup_events(event, ship):
#     """响应松开"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = False
#
#
# def check_events(ai_settings, screen, ship, bullets):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             check_keydown_events(event, ai_settings, screen, ship, bullets)
#         elif event.type == pygame.KEYUP:
#             check_keyup_events(event, ship)
#
#
# def update_screen(ai_settings, screen, ship, bullets):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重绘屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 在飞船和外星人后面重绘所有子弹
#     for bullet in bullets.sprites():
#         bullet.draw_bullet()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()
# ------------------ example07 ------------------

# print("*" * 20)

# ------------------ example08 ------------------
# import sys
#
# import pygame
#
# from bullet import Bullet
#
#
# def check_keydown_events(event, ai_settings, screen, ship, bullets):
#     """响应按键"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = True
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = True
#     elif event.key == pygame.K_SPACE:
#         # 创建一颗子弹，并将其加入到编组bullets中
#         if len(bullets) < ai_settings.bullets_allowed:
#             new_bullet = Bullet(ai_settings, screen, ship)
#             bullets.add(new_bullet)
#
#
# def check_keyup_events(event, ship):
#     """响应松开"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = False
#
#
# def check_events(ai_settings, screen, ship, bullets):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             check_keydown_events(event, ai_settings, screen, ship, bullets)
#         elif event.type == pygame.KEYUP:
#             check_keyup_events(event, ship)
#
#
# def update_screen(ai_settings, screen, ship, bullets):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重绘屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 在飞船和外星人后面重绘所有子弹
#     for bullet in bullets.sprites():
#         bullet.draw_bullet()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()
# ------------------ example08 ------------------

# print("*" * 20)

# ------------------ example09 ------------------
# import sys
#
# import pygame
#
# from bullet import Bullet
#
#
# def check_keydown_events(event, ai_settings, screen, ship, bullets):
#     """响应按键"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = True
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = True
#     elif event.key == pygame.K_SPACE:
#         # 创建一颗子弹，并将其加入到编组bullets中
#         if len(bullets) < ai_settings.bullets_allowed:
#             new_bullet = Bullet(ai_settings, screen, ship)
#             bullets.add(new_bullet)
#
#
# def check_keyup_events(event, ship):
#     """响应松开"""
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         ship.moving_left = False
#
#
# def check_events(ai_settings, screen, ship, bullets):
#     """响应按键和鼠标事件"""
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             check_keydown_events(event, ai_settings, screen, ship, bullets)
#         elif event.type == pygame.KEYUP:
#             check_keyup_events(event, ship)
#
#
# def update_screen(ai_settings, screen, ship, bullets):
#     """更新屏幕上的图像，并切换到新屏幕"""
#     # 每次循环时都重绘屏幕
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
#
#     # 在飞船和外星人后面重绘所有子弹
#     for bullet in bullets.sprites():
#         bullet.draw_bullet()
#
#     # 让最近绘制的屏幕可见
#     pygame.display.flip()
#
#
# def update_bullets(bullets):
#     """更新子弹的位置，并删除已消失的子弹"""
#     # 更新子弹的位置
#     bullets.update()
#
#     # 删除已消失的子弹
#     for bullet in bullets.copy():
#         if bullet.rect.bottom <= 0:
#             bullets.remove(bullet)
# ------------------ example09 ------------------

# print("*" * 20)

# ------------------ example10 ------------------
import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
# ------------------ example10 ------------------
