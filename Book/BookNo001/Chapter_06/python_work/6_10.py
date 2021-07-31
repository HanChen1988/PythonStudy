# -*- coding: utf-8 -*-
# @Time : 2021/7/31 18:44 下午
# @Author : HanChen
# @File : 6_10.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
6-10 喜欢的数字：修改为完成练习 6-2 而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来。
"""
favorite_numbers = {
    'ZhangSan': [3, 6],
    'LiSi': [4],
    'WangWu': [1, 5],
    'ZhaoLiu': [2, 6],
    'TianQi': [7, 8, 9],
}

for name,numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))
# ------------------ example01 ------------------
