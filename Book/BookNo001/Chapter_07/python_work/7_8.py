# -*- coding: utf-8 -*-
# @Time : 2021/8/10 21:39 下午
# @Author : HanChen
# @File : 7_8.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
7-8 熟食店：创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名字；再创建一个名为 finished_sandwiches 的空列表。
    遍历列表 sandwich_orders，对于其中的每种三明治，都打印一条消息，如 I made your tuna sandwich，并将其移到列表finished_sandwiches。
    所有三明治都制作好后，打印一条消息，将这些三明治列出来。
"""
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")
# ------------------ example01 ------------------
