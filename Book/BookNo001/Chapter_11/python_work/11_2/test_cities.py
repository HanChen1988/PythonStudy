# -*- coding: utf-8 -*-
# @Time : 2022/03/17 3:49 上午
# @Author : HanChen
# @File : test_cities.py
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
# import unittest
#
# from city_functions import city_country
#
# class CitiesTestCase(unittest.TestCase):
#     """Tests for 'city_functions.py'."""
#
#     def test_city_country(self):
#         """Does a simple city and country pair work?"""
#         santiago_chile = city_country('santiago', 'chile')
#         self.assertEqual(santiago_chile, 'Santiago, Chile')
#
# unittest.main()
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_city_country_population(self):
        """Can I include a population argument?"""
        santiago_chile = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')

unittest.main()
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------  error01  ------------------
# E
# ======================================================================
# ERROR: test_city_country (__main__.CitiesTestCase)
# Does a simple city and country pair work?
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_11/python_work/11_2/test_cities.py", line 29, in test_city_country
#     santiago_chile = city_country('santiago', 'chile')
# TypeError: city_country() missing 1 required positional argument: 'population'
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
#
# FAILED (errors=1)
# ------------------  error01  ------------------

# print("*" * 20)

# ------------------ correct01 ------------------
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
# ------------------ correct01 ------------------

# print("*" * 20)

# ------------------ correct02 ------------------
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
# ------------------ correct02 ------------------
