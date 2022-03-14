# -*- coding: utf-8 -*-
# @Time : 2022/03/14 15:07 下午
# @Author : HanChen
# @File : 10_6.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
10-6 加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。
    在这种情况下，当你尝试将输入转换为整数时，将引发 ValueError 异常。
    编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。
    在用户输入的任何一个值不是数字时都捕获 ValueError 异常，并打印一条友好的错误消息。
    对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
"""
try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)

except ValueError:
    print("Sorry, I really needed a number.")

else:
    sum = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
# ------------------ example01 ------------------