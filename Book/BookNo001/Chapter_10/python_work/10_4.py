# -*- coding: utf-8 -*-
# @Time : 2021/12/23 15:59 下午
# @Author : HanChen
# @File : 10_4.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
10-4 访客名单：编写一个 while 循环，提示用户输入其名字。
    用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。
    确保这个文件中的每条记录都独占一行。
"""
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + "\n")
        print("Hi " + name + ", you've been added to the guest book.")
# ------------------ example01 ------------------