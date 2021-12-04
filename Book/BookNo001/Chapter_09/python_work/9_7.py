# -*- coding: utf-8 -*-
# @Time : 2021/12/04 15:47 下午
# @Author : HanChen
# @File : 9_7.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-7 管理员：管理员是一种特殊的用户。
    编写一个名为 Admin 的类，让它继承你为完成练习 9-3 或练习 9-5 而编写的 User 类。
    添加一个名为 privileges 的属性，用于存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
    编写一个名为 show_privileges()的方法，它显示管理员的权限。创建一个 Admin实例，并调用这个方法。

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


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

eric.show_privileges()
# ------------------ example01 ------------------