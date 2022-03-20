# -*- coding: utf-8 -*-
# @Time : 2022/03/20 12:55 下午
# @Author : HanChen
# @File : doraemon.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import pygame


class Doraemon():

    def __init__(self, screen):
        """初始化哆啦A梦并设置其初始位置"""
        self.screen = screen

        # 加载哆啦A梦图像并获取其外接矩形
        self.image = pygame.image.load('images/doraemon.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个新哆啦A梦放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """在指定位置绘制哆啦A梦"""
        self.screen.blit(self.image, self.rect)
# ------------------ example01 ------------------
