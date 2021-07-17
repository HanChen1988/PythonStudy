# -*- coding: utf-8 -*-
# @Time : 2021/7/17 23:05 下午
# @Author : HanChen
# @File : 4_8.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
4-8 立方：将同一个数字乘三次称为立方。例如，在 Python 中，2的立方用 2**3 表示。请创建一个列表，其中包含前10个整数（即 1~10）的立方，再使用一个for循环将这些立方数都打印出来。
"""
# 写法1
cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)

print("-" * 20)

# 写法2
cubes = []

for number in range(1,11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)
# ------------------ example01 ------------------
