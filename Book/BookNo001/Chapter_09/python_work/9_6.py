# -*- coding: utf-8 -*-
# @Time : 2021/12/04 12:07 下午
# @Author : HanChen
# @File : 9_6.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。
    编写一个名为 IceCreamStand 的类，让它继承你为完成练习 9-1 或者练习 9-4 而编写的 Restaurant 类。这两个版本的 Restaurant 类都可以，挑选你更喜欢的那个即可。
    添加一个名为 flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并调用这个方法。

    9-4 就餐人数：在为完成练习 9-1 而编写的程序中，添加一个名为 number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为 restaurant 的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
        添加一个名为 set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
        添加一个名为 increment_number_served()的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
"""
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.restaurant_name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()
# ------------------ example01 ------------------