# -*- coding: utf-8 -*-
# @Time : 2021/7/31 18:44 下午
# @Author : HanChen
# @File : 6_7.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
6-7 人：在为完成练习 6-1 而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为 people 的列表中。遍历这个列表，将其中每个人的所有信息都打印出来。
"""
people = []

person = {
    'first_name': 'San', 
    'last_name': 'Zhang', 
    'age': 18, 
    'city': 'BeiJing',
    }

people.append(person)

person = {
    'first_name': 'Si', 
    'last_name': 'Li', 
    'age': 20, 
    'city': 'BeiJing',
    }

people.append(person)

person = {
    'first_name': 'Wu', 
    'last_name': 'Wang', 
    'age': 17, 
    'city': 'BeiJing',
    }
    
people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + ", of " + city + ", is " + age + " years old.")
# ------------------ example01 ------------------
