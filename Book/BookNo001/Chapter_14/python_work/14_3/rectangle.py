# -*- coding: utf-8 -*-
# @Time : 2022/04/07 17:46 下午
# @Author : HanChen
# @File : rectangle.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import pygame
from pygame.sprite import Sprite


class Rectangle(Sprite):
    """表示单个矩形的类"""

    def __init__(self, ai_settings, screen):
        """初始化矩形并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 在(0,0)处创建一个矩形
        self.rect = pygame.Rect(0, 0, ai_settings.rectangle_width,
                                ai_settings.rectangle_height)
        self.screen_rect = screen.get_rect()
        # 每个矩形最初都在屏幕右侧中央
        self.rect.x = self.screen_rect.right - self.rect.width
        self.rect.y = self.screen_rect.centery

        # 存储矩形的准确位置
        self.y = float(self.rect.y)

    def draw_rectangle(self):
        """在屏幕上绘制矩形"""
        pygame.draw.rect(self.screen, self.ai_settings.rectangle_color
                         , self.rect)

    def check_edges(self):
        """如果矩形位于屏幕边缘，就返回True"""
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= self.screen_rect.bottom:
            return True

    def update(self):
        """向上或向下移动矩形"""
        self.y += (self.ai_settings.rectangle_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.y = self.y

    def center_rectangles(self):
        """让飞船在屏幕上居中"""
        self.y = self.screen_rect.centery

        # 根据self.y更新rect对象
        self.rect.y = self.y
# ------------------ example01 ------------------
