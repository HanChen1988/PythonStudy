# -*- coding: utf-8 -*-
# @Time : 2021/12/14 07:13 上午
# @Author : HanChen
# @File : write_message.py
# @Software: Sublime Text

# ------------------ example01 ------------------
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
# ------------------ example03 ------------------

print("*" * 20)

# ------------------ example04 ------------------
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
# ------------------ example04 ------------------
