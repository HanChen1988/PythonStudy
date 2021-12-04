# -*- coding: utf-8 -*-
# @Time : 2021/12/04 11:01 上午
# @Author : HanChen
# @File : 9_3.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-3 用户：创建一个名为 User 的类，其中包含属性 first_name 和 last_name，还有用户简介通常会存储的其他几个属性。
    在类 User 中定义一个名为 describe_user() 的方法，它打印用户信息摘要；再定义一个名为 greet_user() 的方法，它向用户发出个性化的问候。
    创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
"""
class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()
# ------------------ example01 ------------------