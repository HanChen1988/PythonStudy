# -*- coding: utf-8 -*-
# @Time : 2022/03/17 4:19 上午
# @Author : HanChen
# @File : test_employee.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
11-3 雇员：编写一个名为 Employee 的类，其方法__init__()接受名、姓和年薪，并将它们都存储在属性中。
    编写一个名为 give_raise() 的方法，它默认将年薪增加 5000 美元，但也能够接受其他的年薪增加量。

    为 Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_raise() 和 test_give_custom_raise()。
    使用方法 setUp()，以免在每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了。
"""
import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the module employee."""

    def setUp(self):
        """Make an employee to use in tests."""
        self.eric = Employee('eric', 'matthes', 65000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)

unittest.main()
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ correct01 ------------------
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
# ------------------ correct01 ------------------
