# -*- coding: utf-8 -*-
# @Time : 2021/7/28 07:05 上午
# @Author : HanChen
# @File : 5_5.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
5-5 外星人颜色#3：将练习 5-4 中的 if-else 结构改为 if-elif-else 结构。
    如果外星人是绿色的，就打印一条消息，指出玩家获得了 5个点。
    如果外星人是黄色的，就打印一条消息，指出玩家获得了 10个点。
    如果外星人是红色的，就打印一条消息，指出玩家获得了 15个点。
    编写这个程序的三个版本，它们分别在外星人的绿色、黄色和红色时打印一条消息。
"""
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

print("-" * 20)

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

print("-" * 20)

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
# ------------------ example01 ------------------

