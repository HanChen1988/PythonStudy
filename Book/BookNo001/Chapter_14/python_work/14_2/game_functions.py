# -*- coding: utf-8 -*-
# @Time : 2022/04/06 17:16 下午
# @Author : HanChen
# @File : game_functions.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import sys
import pygame

from bullet import Bullet
from rectangle import Rectangle


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, stats, play_button, ship, rectangles, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, play_button, ship, rectangles,
                              bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, stats, play_button, ship, rectangles,
                      bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    # 使用collidepoint()检查鼠标单击位置是否在Play按钮的rect内
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 清空子弹列表
        bullets.empty()

        # 让矩形、飞船居中
        for rectangle in rectangles.sprites():
            rectangle.center_rectangles()
        ship.center_ship()


def update_screen(ai_settings, screen, stats, ship, rectangles, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 在飞船后面重绘所有矩形
    for rectangle in rectangles.sprites():
        rectangle.draw_rectangle()

    # 在飞船和矩形后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 检测飞船数是否为0，如果为0游戏处于非活动状态。
    if stats.ships_left == 0:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(screen, stats, rectangles, bullets):
    """更新子弹的位置，检测子弹和矩形、屏幕右端的碰撞，并删除到达屏幕右端的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 检测子弹和矩形之间的碰撞
    if stats.ships_left > 0:
        collisions = pygame.sprite.groupcollide(bullets, rectangles, True, False)
        if not collisions:
            # 检查是否有子弹到达屏幕右端
            check_bullets_bottom(screen, stats, bullets)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_bullets_bottom(screen, stats, bullets):
    """检查是否有子弹到达了屏幕右端"""
    screen_rect = screen.get_rect()
    for bullet in bullets.sprites():
        if bullet.rect.right >= screen_rect.right:
            # 删除到达屏幕右端的子弹
            bullets.remove(bullet)

            # 将ships_left减1
            stats.ships_left -= 1

            break


def create_rectangle(ai_settings, screen, rectangles):
    """创建一个矩形并将其放在当前行"""
    rectangle = Rectangle(ai_settings, screen)
    rectangles.add(rectangle)


def check_fleet_edges(ai_settings, rectangles):
    """有矩形到达边缘时采取相应的措施"""
    for rectangle in rectangles.sprites():
        if rectangle.check_edges():
            change_fleet_direction(ai_settings)
            break


def change_fleet_direction(ai_settings):
    """将整群矩形改变它们的方向"""
    ai_settings.fleet_direction *= -1


def update_rectangles(ai_settings, rectangles):
    """
    检查是否有矩形位于屏幕边缘，并更新整群矩形的位置
    """
    check_fleet_edges(ai_settings, rectangles)
    rectangles.update()
# ------------------ example01 ------------------
