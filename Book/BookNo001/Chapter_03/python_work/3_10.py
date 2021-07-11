# -*- coding: utf-8 -*-
# @Time : 2021/7/11 10:03 下午
# @Author : HanChen
# @File : 3_10.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
3-10 尝试使用各个函数：想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。
"""
languages = ['chinese', 'english', 'french', 'german']
# 打印列表
print(languages)
# 访问第一个列表元素
print(languages[0])
# 访问第二个列表元素
print(languages[1].title())
print("*" * 20)
# 修改第一个列表元素
languages[0] = 'russian'
print(languages)
# 在列表末尾添加元素
languages.append('chinese')
print(languages)
# 在列表开头插入元素
languages.insert(0, 'spanish')
print(languages)
print("*" * 20)
# 使用del语句删除元素
del languages[0]
print(languages)
print("*" * 20)
# 使用方法pop()删除元素
languages.pop()
print(languages)
# 弹出列表中任何位置处的元素
languages.pop(0)
print(languages)
print("*" * 20)
# 在列表末尾添加元素
languages.append('french')
print(languages)
# 使用方法remove()根据值删除元素,只删除第一个指定的值.
languages.remove('french')
print(languages)
print("*" * 20)
# 使用方法sort()对列表进行永久性排序
languages.sort()
print(languages)
# 使用方法sort(),按与字母顺序相反的顺序排列列表元素
languages.sort(reverse=True)
print(languages)
print("*" * 20)
# 使用函数sorted()对列表进行临时排序
languages = ['russian', 'english', 'french', 'german']
print(sorted(languages))
print(languages)
# 使用函数sorted(),按与字母顺序相反的顺序排列列表元素
print(sorted(languages, reverse=True))
print(languages)
print("*" * 20)
# 使用方法reverse()倒着打印列表
languages.reverse()
print(languages)
print("*" * 20)
# 确定列表的长度
print(len(languages))
# ------------------ example01 ------------------

