# -*- coding: utf-8 -*-
# @Time : 2021/8/31 07:48 上午
# @Author : HanChen
# @File : 8_9.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
8-9 魔术师：创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()的函数，这个函数打印列表中每个魔术师的名字。
"""
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())

magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)
# ------------------ example01 ------------------