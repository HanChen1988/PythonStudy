# -*- coding: utf-8 -*-
# @Time : 2021/7/28 07:48 上午
# @Author : HanChen
# @File : 5_11.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
在一个列表中存储数字 1~9。
    遍历这个列表。
    在循环中使用一个 if-elif-else 结构，以打印每个数字对应的序数。输出内容应为 1st、2nd、3rd、4th、5th、6th、7th、8th 和 9th，但每个序数都独立一行。
"""
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")
# ------------------ example01 ------------------

