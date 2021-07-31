# -*- coding: utf-8 -*-
# @Time : 2021/7/31 17:44 下午
# @Author : HanChen
# @File : 6_1__6_12.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
6-1 人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键 first_name、last_name、age和city。将存储在该字典中的每项信息都打印出来。
    6-12 扩展：本章的示例足够复杂，可以以很多方式进行扩展了。请对本章的一个示例进行扩展：添加键和值、调整程序要解决的问题或改进输出的格式。
"""
person = {
    'first_name': 'San', 
    'last_name': 'Zhang', 
    'age': 18, 
    'city': 'BeiJing',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

print("-" * 20)

person['country'] = 'china'
print(person['country'])
# ------------------ example01 ------------------
