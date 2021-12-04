# -*- coding: utf-8 -*-
# @Time : 2021/12/04 16:46 下午
# @Author : HanChen
# @File : 9_11.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-11 导入 Admin 类：以为完成练习 9-8 而做的工作为基础，将 User 、 Privileges 和 Admin 类存储在一个模块中，再创建一个文件，在其中创建一个 Admin 实例并对其调用方法 show_privileges()，以确认一切都能正确地运行。
"""
from user import Admin

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges

print("\nThe admin " + eric.username + " has these privileges: ")
eric.privileges.show_privileges()
# ------------------ example01 ------------------