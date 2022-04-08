# -*- coding: utf-8 -*-
# @Time : 2022/04/08 11:59 上午
# @Author : HanChen
# @File : scoreboard.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备包含当前得分、最高得分、玩家等级、绘制飞船的图像
        self.prep_images(self.stats.score, 'score', 'number', '1')
        self.prep_images(self.stats.high_score, 'high_score', 'number', '1')
        self.prep_images(self.stats.level, 'level', 'number', '0')
        self.prep_images(self.stats.ships_left, 'ship', 'image')

    def prep_images(self, obj, obj_name, obj_type, is_format='0'):
        """将得分、最高得分、等级、余下飞船数转换为一幅渲染的图像"""
        if obj_type == 'number' and is_format == '1':
            # 将obj转换为一幅渲染的图像
            rounded_obj = int(round(obj, -1))
            obj_str = "{:,}".format(rounded_obj)
            self.obj_image = self.font.render(obj_str, True, self.text_color,
                                              self.ai_settings.bg_color)

        if obj_type == 'number' and is_format == '0':
            # 将obj转换为一幅渲染的图像
            self.obj_image = self.font.render(str(obj), True,
                                              self.text_color,
                                              self.ai_settings.bg_color)

        if obj_type == 'image' and obj_name == 'ship':
            # 显示还余下多少艘飞船
            self.ships = Group()
            for ship_number in range(obj):
                ship = Ship(self.ai_settings, self.screen)
                ship.rect.x = 10 + ship_number * ship.rect.width
                ship.rect.y = 10
                self.ships.add(ship)

        if obj_name == 'score':
            # 将得分放在屏幕右上角
            self.score_image = self.obj_image
            self.score_rect = self.score_image.get_rect()
            self.score_rect.right = self.screen_rect.right - 20
            self.score_rect.top = 20

        if obj_name == 'high_score':
            # 将最高得分放在屏幕顶部中央
            self.high_score_image = self.obj_image
            self.high_score_rect = self.high_score_image.get_rect()
            self.high_score_rect.centerx = self.screen_rect.centerx
            self.high_score_rect.top = self.score_rect.top

        if obj_name == 'level':
            # 将等级放在得分下方
            self.level_image = self.obj_image
            self.level_rect = self.level_image.get_rect()
            self.level_rect.right = self.score_rect.right
            self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """在屏幕上显示得分、玩家等级、绘制飞船"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)
# ------------------ example01 ------------------
