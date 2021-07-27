# -*- coding: utf-8 -*-
# @Time : 2021/7/27 22:24 下午
# @Author : HanChen
# @File : 5_2.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
5-2 更多的条件测试：你并非只能创建10个测试。如果你想尝试做更多的比较，可再编写一些测试，并将它们加入到 conditional_tests.py 中。对于下面列出的各种测试，至少编写一个结果为 True 和 False 的测试。
    检查两个字符串相等和不等。
    使用函数 lower() 的测试。
    检查两个数字相等、不等、大于、小于、大于等于和小于等于。
    使用关键字 and 和 or 的测试。
    测试特定的值是否包含在列表中。
    测试特定的值是否未包含在列表中。
"""
# 检查两个字符串相等和不等
name = 'ZhangSan'
print("Is name == 'ZhangSan'? I predict True.")
print(name == 'ZhangSan')

print("\nIs name != 'ZhangSan'? I predict False.")
print(name != 'ZhangSan')

# 使用函数 lower() 的测试
name = 'ZhangSan'
print("\nIs name.lower() == 'ZhangSan'? I predict False.")
print(name.lower() == 'ZhangSan')

# 检查两个数字相等、不等、大于、小于、大于等于和小于等于
answer = 10
print("\nIs answer == 10? I predict True.")
print(answer == 10)

print("\nIs answer != 10? I predict False.")
print(answer != 10)

print("\nIs answer > 10? I predict False.")
print(answer > 10)

print("\nIs answer < 10? I predict False.")
print(answer < 10)

print("\nIs answer >= 10? I predict True.")
print(answer >= 10)

print("\nIs answer <= 10? I predict True.")
print(answer >= 10)

# 使用关键字 and 和 or 的测试
age_0 = 12
age_1 = 18
print("\nIs age_0 > 11 and age_1 > 18? I predict False.")
print(age_0 > 11 and age_1 > 18)

print("\nIs age_0 > 11 or age_1 > 18? I predict True.")
print(age_0 > 11 or age_1 > 18)

# 测试特定的值是否包含在列表中
cars = ['audi', 'subaru', 'toyota']
print("\nIs 'bmw' in cars? I predict False.")
print('bmw' in cars)

# 测试特定的值是否未包含在列表中
print("\nIs 'bmw' not in cars? I predict True.")
print('bmw' not in cars)
# ------------------ example01 ------------------

