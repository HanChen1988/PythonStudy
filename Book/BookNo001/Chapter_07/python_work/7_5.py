# -*- coding: utf-8 -*-
# @Time : 2021/8/10 21:39 下午
# @Author : HanChen
# @File : 7_5.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
7-5 电影票：有家电影院根据观众的年龄收取不同的票价：不到 3 岁的观众免费；3~12 岁的观众为 10 美元；超过 12 岁的观众为 15 美元。
请编写一个循环，在其中询问用户的年龄，并指出其票价。
"""
while True:
    age = input("Please enter age: ")
    age = int(age)

    if age < 3:
        print("Free ticket.")
    elif age < 12:
        print("Tickets cost $10.")
    else:
        print("Tickets cost $15.")
# ------------------ example01 ------------------
