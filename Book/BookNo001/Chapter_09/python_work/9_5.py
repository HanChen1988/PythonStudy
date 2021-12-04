# -*- coding: utf-8 -*-
# @Time : 2021/12/04 11:40 上午
# @Author : HanChen
# @File : 9_5.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-5 尝试登录次数：在为完成练习 9-3 而编写的 User 类中，添加一个名为 login_attempts 的属性。
    编写一个名为 increment_login_attempts()的方法，它将属性 login_attempts 的值加 1。
    再编写一个名为 reset_login_attempts()的方法，它将属性login_attempts的值重置为0。
    根据 User 类创建一个实例，再调用方法 increment_login_attempts()多次。打印属性 login_attempts 的值，确认它被正确地递增；
    然后调用方法 reset_login_attempts()，并再次打印属性 login_attempts 的值，确认它被重置为0。
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

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))

print("Resetting login attempts...")
eric.reset_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))
# ------------------ example01 ------------------