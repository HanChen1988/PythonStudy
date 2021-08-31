# -*- coding: utf-8 -*-
# @Time : 2021/8/30 21:36 下午
# @Author : HanChen
# @File : 8_3.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
8-3 T恤：编写一个名为 make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
"""
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')
# ------------------ example01 ------------------