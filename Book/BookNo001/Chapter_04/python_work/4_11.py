# -*- coding: utf-8 -*-
# @Time : 2021/7/17 23:38 下午
# @Author : HanChen
# @File : 4_11.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
4-11 你的比萨和我的比萨：在你为完成练习 4-1 而编写的程序中，创建比萨列表的副本，并将其存储到变量 friend_pizzas 中，再完成如下任务。
    在原来的比萨列表中添加一种披萨。
    在列表 friend_pizzas 中添加另一种披萨。
    核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for循环来打印第一个列表；打印消息“My friend's favorite pizzas are:”，再使用一个for循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
"""
pizzas = ['beef', 'seafood', 'salmon', 'pepperoni']
friend_pizzas = pizzas[:]

pizzas.append("fruits")
friend_pizzas.append("ham")

print("My favorite pizzas are:")
for pizza in pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print("- " + friend_pizza)
# ------------------ example01 ------------------
