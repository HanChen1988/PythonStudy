# -*- coding: utf-8 -*-
# @Time : 2022/03/24 21:33 下午
# @Author : HanChen
# @File : star.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """表示单个星星的类"""

    def __init__(self, screen):
        """初始化星星并设置其起始位置"""
        super().__init__()
        self.screen = screen

        # 加载星星图像，并设置其rect属性
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # 每个星星最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储星星的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)
# ------------------ example01 ------------------
