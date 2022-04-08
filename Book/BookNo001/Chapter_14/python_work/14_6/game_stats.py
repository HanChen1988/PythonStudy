# -*- coding: utf-8 -*-
# @Time : 2022/04/08 11:59 上午
# @Author : HanChen
# @File : game_stats.py
# @Software: Sublime Text

# ------------------ example01 ------------------
class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 让游戏一开始处于非活动状态
        self.game_active = False

        # 在任何情况下都不应重置最高得分
        self.high_score = 0
        try:
            with open(self.ai_settings.text_file_path, 'r') as f_obj:
                self.high_score = int(f_obj.read())
        except FileNotFoundError:
            return None

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
# ------------------ example01 ------------------
