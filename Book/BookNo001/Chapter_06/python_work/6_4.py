# -*- coding: utf-8 -*-
# @Time : 2021/7/31 17:44 下午
# @Author : HanChen
# @File : 6_4.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
6-4 词汇表 2：既然你知道了如何遍历字典，现在请整理你为完成练习 6-3 而编写的代码，将其中的一系列 print 语句替换为一个遍历字典中的键和值的循环。确定该循环正确无误后，再在词汇表中添加 5 个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
"""
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

for word, definition in glossary.items():
    print(word.title() + "\n" +
        "\t" + definition)

print("-" * 20)

glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'



for word, definition in glossary.items():
    print(word.title() + "\n" +
        "\t" + definition)
# ------------------ example01 ------------------
