# -*- coding: utf-8 -*-
# @Time : 2021/7/17 23:38 下午
# @Author : HanChen
# @File : 4_13.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
4-13 自助餐：有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
    使用一个for循环将该餐馆提供的五种食品都打印出来。
    尝试修改其中的一个元素，核实Python确实会拒绝你这样做。
    餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：给元组变量赋值，并使用一个for循环将新元组的每个元素都打印出来。
"""
foods = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')
print("Original foods:")
for food in foods:
    print("- " + food)
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
# foods[0] = 'noodles'
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
foods = ('noodles', 'sausage', 'carrot cake', 'cannoli', 'ice cream')
print("Modified foods:")
for food in foods:
    print("- " + food)
# ------------------ example03 ------------------

print("*" * 20)

# ------------------  error02  ------------------
# 报错信息:
# Traceback (most recent call last):
#   File "/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_04/python_work/4_13.py", line 22, in <module>
#     foods[0] = 'noodles'
# TypeError: 'tuple' object does not support item assignment
# --snip--
# 解决方法:
# 1.将一个新元组存储到变量foods中
#    foods = ('noodles', 'falafel', 'carrot cake', 'cannoli', 'ice cream')
# ------------------  error02  ------------------

