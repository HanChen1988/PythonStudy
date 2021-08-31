# -*- coding: utf-8 -*-
# @Time : 2021/8/30 21:36 下午
# @Author : HanChen
# @File : 8_4.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
8-4 大号T恤：修改函数 make_shirt()的函数，使其在默认情况下制作一件印有“I love Python” 的大号T恤。调用这个函数来制作如下T恤：一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）。
"""
def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')
# ------------------ example01 ------------------