# -*- coding: utf-8 -*-
# @Time : 2021/7/17 23:38 下午
# @Author : HanChen
# @File : 4_12.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
4-12 使用多个循环：在本节中，为节省篇幅，程序 foods.py的每个版本都没有使用for循环来打印列表。请选择一个版本的 foods.py，在其中编写两个for循环，将各个食品列表都打印出来。
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for my_food in my_foods:
    print("- " + my_food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print("- " + friend_food)
# ------------------ example01 ------------------
