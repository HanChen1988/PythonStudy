# -*- coding: utf-8 -*-
# @Time : 2022/03/14 15:56 下午
# @Author : HanChen
# @File : 10_9.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
10-9 沉默的猫和狗：修改你在练习 10-8 中编写的 except 代码块，让程序在文件不存在时一言不发。

    10-8 猫和狗：创建两个文件 cats.txt 和 dogs.txt，
            在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
        编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
        将这些代码放在一个 try-except 代码块中，以便在文件不存在时捕获 FileNotFound 错误，
            并打印一条友好的消息。
        将其中一个文件移到另一个地方，并确认 except 代码块中的代码将正确地执行。
"""
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:

    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print("\nReading file: " + filename)
        print(contents)
# ------------------ example01 ------------------