# -*- coding: utf-8 -*-
# @Time : 2021/12/23 15:59 下午
# @Author : HanChen
# @File : 10_5.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
10-5 关于编程的调查：编写一个 while 循环，询问用户为何喜欢编程。
    每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
"""
filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
# ------------------ example01 ------------------