# -*- coding: utf-8 -*-
# @Time : 2022/03/14 16:32 下午
# @Author : HanChen
# @File : 10_11.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
10-11 喜欢的数字：编写一个程序，提示用户输入他喜欢的数字，并使用 json.dump() 将这个数字存储到文件中。
    在编写一个程序，从文件中读取这个值，并打印消息 “I know your favorite number! It's ___.”
"""
# favorite_number_write.py
import json

number = input("What's your favorite number? ")

filename = 'favorite_number.json'

with open(filename, 'w') as f:
    json.dump(number, f)

print("-" * 20)

# favorite_number_read.py
import json

filename = 'favorite_number.json'

with open(filename) as f:
    number = json.load(f)

print("I know your favorite number! It's " + str(number) + ".")
# ------------------ example01 ------------------