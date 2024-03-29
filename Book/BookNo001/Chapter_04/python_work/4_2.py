# -*- coding: utf-8 -*-
# @Time : 2021/7/17 22:50 下午
# @Author : HanChen
# @File : 4_2.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
4-2 动物：想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for循环将每种动物的名称都打印出来。
    修改这个程序，使其针对每种动物都打印一个句子，如“A dog would make a great pet”。
    在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any of these animals would make a great pet!”这样的句子。
"""
animals = ['dog', 'cat', 'hamster', 'alpaca', 'pig']
for animal in animals:
    print(animal)
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
animals = ['dog', 'cat', 'hamster', 'alpaca', 'pig']
for animal in animals:
    print("A " + animal + " would make a great pet.")
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
animals = ['dog', 'cat', 'hamster', 'alpaca', 'pig']
for animal in animals:
    print("A " + animal + " would make a great pet.")

print("\nAny of these animals would make a great pet!")
# ------------------ example03 ------------------
