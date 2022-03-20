# -*- coding: utf-8 -*-
# @Time : 2022/03/20 15:57 下午
# @Author : HanChen
# @File : ship.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载、旋转飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.angle = -90
        self.image_rotate = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image_rotate.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕左侧中央
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # 在飞船的属性centery中存储小数值
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的centery值，而不是rect
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image_rotate, self.rect)
# ------------------ example01 ------------------
