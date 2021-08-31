# -*- coding: utf-8 -*-
# @Time : 2021/8/30 21:36 下午
# @Author : HanChen
# @File : 8_5.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
8-5 城市：编写一个名为 describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，如 Reykjavik is in Iceland。给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
"""
def describe_city(city, country='chile'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')
# ------------------ example01 ------------------