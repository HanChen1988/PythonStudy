# -*- coding: utf-8 -*-
# @Time : 2021/8/10 21:39 下午
# @Author : HanChen
# @File : 7_6.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
7-6 三个出口：以另一种方式完成练习 7-4 或练习 7-5，在程序中采取如下所有做法。
    在 while 循环中使用条件测试来结束循环。
    使用变量 active 来控制循环结束的时机。
    使用 break 语句在用户输入'quit'时退出循环。

    7-5 电影票：有家电影院根据观众的年龄收取不同的票价：不到 3 岁的观众免费；3~12 岁的观众为 10 美元；超过 12 岁的观众为 15 美元。
    请编写一个循环，在其中询问用户的年龄，并指出其票价。
"""
prompt = "\nPlease enter age:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    message = int(message)

    if message < 3:
        print("Free ticket.")
    elif message < 12:
        print("Tickets cost $10.")
    else:
        print("Tickets cost $15.")
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
prompt = "\nPlease enter age:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False

    message = int(message)

    if message < 3:
        print("Free ticket.")
    elif message < 12:
        print("Tickets cost $10.")
    else:
        print("Tickets cost $15.")
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
prompt = "\nPlease enter age:"
prompt += "\nEnter 'quit' to end the program. "

while True:
    message = input(prompt)

    if message == 'quit':
        break

    message = int(message)

    if message < 3:
        print("Free ticket.")
    elif message < 12:
        print("Tickets cost $10.")
    else:
        print("Tickets cost $15.")
# ------------------ example03 ------------------
