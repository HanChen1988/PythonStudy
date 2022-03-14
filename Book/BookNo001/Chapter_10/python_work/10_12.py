# -*- coding: utf-8 -*-
# @Time : 2022/03/14 16:48 下午
# @Author : HanChen
# @File : 10_12.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
10-12 记住喜欢的数字：将练习 10-11 中的两个程序合二为一。
    如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
    运行这个程序两次，看看它是否像预期的那样工作。

    10-11 喜欢的数字：编写一个程序，提示用户输入他喜欢的数字，并使用 json.dump() 将这个数字存储到文件中。
        在编写一个程序，从文件中读取这个值，并打印消息 “I know your favorite number! It's ___.”
"""
import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print("I know your favorite number! It's " + str(number) + ".")
# ------------------ example01 ------------------