# -*- coding: utf-8 -*-
# @Time : 2021/12/23 15:47 下午
# @Author : HanChen
# @File : 10_3.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
10-3 访客：编写一个程序，提示用户输入其名字；用户做出响应后，将其名字写入到文件 guest.txt 中。
"""
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)
# ------------------ example01 ------------------