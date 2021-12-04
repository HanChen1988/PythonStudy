# -*- coding: utf-8 -*-
# @Time : 2021/12/04 16:56 下午
# @Author : HanChen
# @File : 9_13.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-13 使用 OrderedDict：在练习 6-4 中，你使用了一个标准字典来表示词汇表。请使用 OrderedDict 类来重写这个程序，并确认输出的顺序与你在字典中添加键-值对的顺序一直。
"""
from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)
# ------------------ example01 ------------------