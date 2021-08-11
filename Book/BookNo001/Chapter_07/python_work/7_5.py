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
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
# ------------------ example01 ------------------
