# -*- coding: utf-8 -*-
# @Time : 2021/12/04 11:00 上午
# @Author : HanChen
# @File : 9_2.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-2 三家餐馆：根据你为完成练习 9-1 而编写的类创建三个实例，并对每个实例调用方法 describe_restaurant()。

    9-1 餐馆：创建一个名为 Restaurant 的类，其方法__init__()设置两个属性：restaurant_name 和 cuisine_type。
        创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条信息，指出餐馆正在营业。
        根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
"""
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()
# ------------------ example01 ------------------