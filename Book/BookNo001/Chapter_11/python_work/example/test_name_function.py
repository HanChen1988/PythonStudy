# -*- coding: utf-8 -*-
# @Time : 2022/03/16 00:58 上午
# @Author : HanChen
# @File : test_name_function.py
# @Software: Sublime Text

# ------------------ example01 ------------------
# import unittest
# from name_function import get_formatted_name
#
#
# class NamesTestCase(unittest.TestCase):
#     """测试name_function.py"""
#
#     def test_first_last_name(self):
#         """能够正确地处理像Janis Joplin这样的姓名吗？"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')
#
#
# unittest.main()
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
# ------------------ example02 ------------------
