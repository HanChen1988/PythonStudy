# -*- coding: utf-8 -*-
# @Time : 2021/8/30 21:36 下午
# @Author : HanChen
# @File : 8_6.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
8-6 城市名：编写一个名为 city_country()的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串：
    "Santiago, Chile"
    至少使用三个城市-国家对调用这个函数，并打印它返回的值。
"""
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    msg = city.title() + ", " + country.title()
    return msg

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)

print("-" * 20)

def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)
# ------------------ example01 ------------------