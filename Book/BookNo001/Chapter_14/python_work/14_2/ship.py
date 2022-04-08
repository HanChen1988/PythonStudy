# -*- coding: utf-8 -*-
# @Time : 2022/04/06 17:16 下午
# @Author : HanChen
# @File : ship.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载、旋转飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.angle = -90
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image_rotate.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕左侧中央
        self.rect.x = self.screen_rect.left
        self.rect.y = self.screen_rect.centery

        # 在飞船的属性y中存储小数值
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的y值，而不是rect
        if self.moving_up and self.rect.top > 0:
            self.y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed_factor

        # 根据self.y更新rect对象
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image_rotate, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.y = self.screen_rect.centery

        # 根据self.y更新rect对象
        self.rect.y = self.y
# ------------------ example01 ------------------
