# -*- coding: utf-8 -*-
# @Time : 2021/7/17 23:38 下午
# @Author : HanChen
# @File : 4_10.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
4-10 切片：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
    打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
    打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
    打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
    4-2 动物：想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for循环将每种动物的名称都打印出来。
"""
animals = ['dog', 'cat', 'hamster', 'alpaca', 'pig']
for animal in animals:
    print(animal)
# 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
print("\nThe first three items in the list are:")
print(animals[:3])
# 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
print("\nThree items from the middle of the list are:")
print(animals[1:4])
# 打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
print("\nThe last three items in the list are:")
print(animals[-3:])
# ------------------ example01 ------------------
