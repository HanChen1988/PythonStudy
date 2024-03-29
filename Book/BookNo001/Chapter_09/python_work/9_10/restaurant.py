# -*- coding: utf-8 -*-
# @Time : 2021/12/04 16:39 下午
# @Author : HanChen
# @File : Restaurant.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-10 导入 Restaurant 类：将最新的 Restaurant 类存储在一个模块中。
    在另一个文件中，导入 Restaurant 类，创建一个 Restaurant 实例，并调用 Restaurant 的一个方法，以确认 import 语句正确无误。
"""
"""A class representing a restaurant."""

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served
# ------------------ example01 ------------------