# -*- coding: utf-8 -*-
# @Time : 2021/7/17 22:37 下午
# @Author : HanChen
# @File : 4_1.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
4-1 比萨：想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for循环将每种比萨的名称都打印出来。
    修改这个for循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种披萨，都显示一行输出，如“I like pepperoni pizza”。 
    在程序末尾添加一行代码，它不在for循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”。
"""
pizzas = ['beef', 'seafood', 'salmon', 'pepperoni']
for pizza in pizzas:
    print(pizza)
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
pizzas = ['beef', 'seafood', 'salmon', 'pepperoni']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
pizzas = ['beef', 'seafood', 'salmon', 'pepperoni']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print("\nI really love pizza!")
# ------------------ example03 ------------------
