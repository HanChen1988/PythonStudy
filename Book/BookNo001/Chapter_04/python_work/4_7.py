# -*- coding: utf-8 -*-
# @Time : 2021/7/17 23:05 下午
# @Author : HanChen
# @File : 4_7.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
4-7 3的倍数：创建一个列表，其中包含 3~30内能被 3整除的数字；再使用一个for循环将这个列表中的数字都打印出来。
"""
multiples = [value for value in range(3, 31) if value % 3 == 0]
for multiple in multiples:
    print(multiple)
# ------------------ example01 ------------------
