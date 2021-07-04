# -*- coding: utf-8 -*-
# @Time : 2021/7/4 10:49 下午
# @Author : HanChen
# @File : apostrophe.py
# @Software: Sublime Text

# ------------------ example01 ------------------
# 使用双引号
message = "One of Python's strengths is its diverse community."
print(message)
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
# 使用单引号
message = 'One of Python's strengths is its diverse community.'
print(message)
# ------------------ example02 ------------------

print("*" * 20)

# ------------------  error02  ------------------
# 报错信息:
# Traceback (most recent call last):
# File "/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_02/python_work/apostrophe.py", line 17
#   message = 'One of Python's strengths is its diverse community.'
#                           ^
# SyntaxError: invalid syntax
# --snip--
# 解决方法:
# 1.改用双引号
#     message = "One of Python's strengths is its diverse community."
# ------------------  error02  ------------------
