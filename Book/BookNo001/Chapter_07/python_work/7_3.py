# -*- coding: utf-8 -*-
# @Time : 2021/8/10 21:39 下午
# @Author : HanChen
# @File : 7_3.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
7-3 10 的整数倍：让用户输入一个数字，并指出这个数字是否是 10的整数倍。
"""
number = input("Give me a number, please: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")
# ------------------ example01 ------------------