# -*- coding: utf-8 -*-
# @Time : 2022/03/24 21:33 下午
# @Author : HanChen
# @File : raindrop.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """表示单个雨滴的类"""

    def __init__(self, ai_settings, screen):
        """初始化雨滴并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载雨滴图像，并设置其rect属性
        self.image = pygame.image.load('images/raindrop.bmp').convert()
        # 修改加载雨滴图像的尺寸
        self.image = pygame.transform.scale(self.image, (45, 64))
        self.rect = self.image.get_rect()

        # 每个雨滴最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储雨滴的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制雨滴"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向下移动雨滴"""
        self.y += self.ai_settings.raindrop_speed_factor
        self.rect.y = self.y
# ------------------ example01 ------------------
