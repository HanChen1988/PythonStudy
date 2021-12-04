# -*- coding: utf-8 -*-
# @Time : 2021/12/04 10:29 上午
# @Author : HanChen
# @File : 9_1.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-1 餐馆：创建一个名为 Restaurant 的类，其方法__init__()设置两个属性：restaurant_name 和 cuisine_type。
    创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条信息，指出餐馆正在营业。
    根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
"""
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.restaurant_name + " is open. Come on in!"
        print("\n" + msg)

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
# ------------------ example01 ------------------