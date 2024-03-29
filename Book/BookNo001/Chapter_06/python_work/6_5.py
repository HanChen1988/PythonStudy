# -*- coding: utf-8 -*-
# @Time : 2021/7/31 17:44 下午
# @Author : HanChen
# @File : 6_5.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
6-5 河流：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键-值对可能是'nile': 'egypt'。
    使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
    使用循环将该字典中每条河流的名字都打印出来。
    使用循环将该字典包含的每个国家的名字都打印出来。
"""
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())
# ------------------ example01 ------------------
