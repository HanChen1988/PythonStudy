# -*- coding: utf-8 -*-
# @Time : 2022/03/15 23:11 下午
# @Author : HanChen
# @File : name_function.py
# @Software: Sublime Text

# ------------------ example01 ------------------
# def get_formatted_name(first, last):
#     """生成整洁的姓名"""
#     full_name = first + ' ' + last
#     return full_name.title()
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# def get_formatted_name(first, middle, last):
#     """生成整洁的姓名"""
#     full_name = first + ' ' + middle + ' ' + last
#     return full_name.title()
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
def get_formatted_name(first, last, middle=''):
    """生成整洁的姓名"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
# ------------------ example03 ------------------
