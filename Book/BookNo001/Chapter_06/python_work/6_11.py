# -*- coding: utf-8 -*-
# @Time : 2021/7/31 18:44 下午
# @Author : HanChen
# @File : 6_11.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
6-11 城市：创建一个名为 cities 的字典，其中将三个城市名用作键；对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。在表示每座城市的字典中，应包含 country、population 和 fact 等键。将每座城市的名字以及有关它们的信息都打印出来。
"""
cities = {
    'beijing':{
        'country': 'china',
        'population': '21.89 million people',
        'fact': 'political center',
    },
    'shanghai':{
        'country': 'china',
        'population': '24.18 million people',
        'fact': 'Political center',
    },
    'shenzhen':{
        'country': 'china',
        'population': '17.56 million people',
        'fact': 'Economic demonstration zone',
    },
}

for city,city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact'].title()

    print("\ncity: " + city.title())
    print("\tcountry: " + country)
    print("\tpopulation: " + population)
    print("\tfact: " + fact)
# ------------------ example01 ------------------
