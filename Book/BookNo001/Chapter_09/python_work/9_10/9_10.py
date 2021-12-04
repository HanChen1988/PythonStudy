# -*- coding: utf-8 -*-
# @Time : 2021/12/04 16:39 下午
# @Author : HanChen
# @File : 9_10.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-10 导入 Restaurant 类：将最新的 Restaurant 类存储在一个模块中。
    在另一个文件中，导入 Restaurant 类，创建一个 Restaurant 实例，并调用 Restaurant 的一个方法，以确认 import 语句正确无误。
"""
from restaurant import Restaurant

channel_club = Restaurant('the channel club', 'steak and seafood')
channel_club.describe_restaurant()
channel_club.open_restaurant()
# ------------------ example01 ------------------