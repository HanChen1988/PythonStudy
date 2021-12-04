# -*- coding: utf-8 -*-
# @Time : 2021/12/04 16:51 下午
# @Author : HanChen
# @File : admin.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-12 多个模块：将 User 类存储在一个模块中，并将 Privileges 和 Admin 类存储在另一个模块中。
    再创建一个文件，在其中创建一个 Admin 实例，并对其调用方法 show_privileges()，以确认一切都依然能够正确地运行。
"""
"""A collection of classes for modeling an admin user account."""

from user import User


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges([])
    

class Privileges():
    """Stores privileges associated with an Admin account."""

    def __init__(self, privileges):
        """Initialize the privileges object."""
        self.privilege = privileges

    def show_privileges(self):
        """Display the privileges this administrator has."""
        for privilege in self.privileges:
            print("- " + privilege)
# ------------------ example01 ------------------