# -*- coding: utf-8 -*-
# @Time : 2022/03/17 3:49 上午
# @Author : HanChen
# @File : city_functions.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
11-2 人口数量：修改前面的函数，使其包含第三个必不可少的形参 population，
    并返回一个格式为 City, Country - population xxx 的字符串，如 Santiago, Chile - population 5000000。
    运行 test_cities.py, 确认测试 test_city_country() 未通过。

    修改上述函数，将形参 population 设置为可选的。
    再次运行 test_cities.py，确认测试 test_city_country() 又通过了。

    再编写一名为 test_city_country_population() 的测试，核实可以使用类似于
        'santiago'、'chile' 和 'population=5000000' 这样的值来调用这个函数。
    再次运行 test_cities.py，确认测试 test_city_country_population() 通过了。
"""
# """A collection of functions for working with cities."""
#
# def city_country(city, country, population):
#     """Return a string like 'Santiago, Chile - population 5000000'."""
#     output_string = city.title() + ", " + country.title()
#     output_string += ' - population ' + str(population)
#     return output_string
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
"""A collection of functions for working with cities."""

def city_country(city, country, population=0):
    """Return a string representing a city-country pair."""

    output_string = city.title() + ", " + country.title()
    if population:
        output_string += ' - population ' + str(population)
    return output_string
# ------------------ example02 ------------------
