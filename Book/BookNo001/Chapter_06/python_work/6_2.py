# -*- coding: utf-8 -*-
# @Time : 2021/7/31 17:44 下午
# @Author : HanChen
# @File : 6_2.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
6-2 喜欢的数字：使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的。
"""
favorite_numbers = {
    'ZhangSan': 3,
    'LiSi': 4,
    'WangWu': 5,
    'ZhaoLiu': 6,
    'TianQi': 7,
}

for name,favorite_number in favorite_numbers.items():
    print(name + "'s favorite number is " + str(favorite_number) + ".")
# ------------------ example01 ------------------
