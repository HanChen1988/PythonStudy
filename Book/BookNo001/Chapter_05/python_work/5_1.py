# -*- coding: utf-8 -*-
# @Time : 2021/7/27 22:24 下午
# @Author : HanChen
# @File : 5_1.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
5-1 条件测试：编写一系列条件测试；将每个测试以及你对其结果的预测和实际结果都打印出来。你编写的代码应类似于下面这样：
    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')

    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')

    详细研究实际结果，直到你明白了它为何为True 或 False。
    创建至少10个测试，其其中结果分别为 True 和 False 的测试都至少有5个。
"""
age = 16
print("Is age != 18? I predict True.")
print(age != 18)

print("\nIs age == 16? I predict True.")
print(age == 16)

print("\nIs age < 20? I predict True.")
print(age < 20)

print("\nIs age <= 16? I predict True.")
print(age <= 16)

print("\nIs age > 10? I predict True.")
print(age > 10)

print("\nIs age >= 20? I predict False.")
print(age >= 20)

print("-" * 20)

age_0 = 10
age_1 = 13
print("Is age_0 > 10 and age_1 > 10? I predict False.")
print(age_0 > 10 and age_1 > 10)

print("\nIs age_0 > 20 or age_1 > 20? I predict False.")
print(age_0 > 20 or age_1 > 20)

print("-" * 20)

cars = ['audi', 'subaru']
print("Is 'bmw' in cars? I predict False.")
print('bmw' in cars)

print("\nIs 'audi' not in cars? I predict False.")
print('audi' not in cars)
# ------------------ example01 ------------------

