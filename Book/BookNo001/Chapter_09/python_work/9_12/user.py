# -*- coding: utf-8 -*-
# @Time : 2021/12/04 16:51 下午
# @Author : HanChen
# @File : user.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-12 多个模块：将 User 类存储在一个模块中，并将 Privileges 和 Admin 类存储在另一个模块中。
    再创建一个文件，在其中创建一个 Admin 实例，并对其调用方法 show_privileges()，以确认一切都依然能够正确地运行。
"""
"""A class for modeling users."""

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0
# ------------------ example01 ------------------