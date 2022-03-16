# -*- coding: utf-8 -*-
# @Time : 2022/03/17 4:19 上午
# @Author : HanChen
# @File : employee.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
11-3 雇员：编写一个名为 Employee 的类，其方法__init__()接受名、姓和年薪，并将它们都存储在属性中。
    编写一个名为 give_raise() 的方法，它默认将年薪增加 5000 美元，但也能够接受其他的年薪增加量。

    为 Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_raise() 和 test_give_custom_raise()。
    使用方法 setUp()，以免在每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了。
"""
class Employee():
    """A class to represent an employee."""

    def __init__(self, f_name, l_name, salary):
        """Initialize the employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount
# ------------------ example01 ------------------
