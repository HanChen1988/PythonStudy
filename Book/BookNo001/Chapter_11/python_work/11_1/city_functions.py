# -*- coding: utf-8 -*-
# @Time : 2022/03/17 3:19 上午
# @Author : HanChen
# @File : city_functions.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
11-1 城市和国家：编写一个函数，它接受两个形参：一个城市名和一个国家名。
    这个函数返回一个格式为 City, Country 的字符串，如 Santiago, Chile。
    将这个函数存储在一个名为 city_functions.py 的模块中。

    创建一个名为 test_cities.py 的程序，对刚编写的函数进行测试（别忘了，你需要导入模块 unittest 以及要测试的函数）。
    编写一个名为 test_city_country() 的方法，核实使用类似于 'santiago' 和 'chile' 这样的值来调用前述函数时，得到的字符串是正确的。
    运行 test_cities.py，确认测试 test_city_country() 通过了。
"""
"""A collection of functions for working with cities."""

def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())
# ------------------ example01 ------------------
