# -*- coding: utf-8 -*-
# @Time : 2022/03/29 01:48 上午
# @Author : HanChen
# @File : football.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import pygame
from pygame.sprite import Sprite


class Football(Sprite):
    """表示单个足球的类"""

    def __init__(self, ai_settings, screen):
        """初始化足球并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载足球图像，并设置其rect属性
        self.image = pygame.image.load('images/football.bmp')
        self.rect = self.image.get_rect()

        # 每个足球最初都在屏幕左上角附近
        self.rect.x = self.rect.centerx
        self.rect.y = self.rect.height

        # 存储足球的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制足球"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向下移动足球"""
        self.y += self.ai_settings.football_speed_factor
        self.rect.y = self.y
# ------------------ example01 ------------------
