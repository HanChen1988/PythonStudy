# -*- coding: utf-8 -*-
# @Time : 2021/7/28 07:05 上午
# @Author : HanChen
# @File : 5_4.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
5-4 外星人颜色#2：像练习 5-3 那样设置外星人的颜色，并编写一个 if-else 结构。
    如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了 5个点。
    如果外星人不是绿色的，就打印一条消息，指出玩家获得了 10个点。
    编写这个程序的两个版本，在一个版本中执行 if 代码块，而在另一个版本中执行 else 代码块。
"""
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

print("-" * 20)

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
# ------------------ example01 ------------------

