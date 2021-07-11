# -*- coding: utf-8 -*-
# @Time : 2021/7/11 22:42 下午
# @Author : HanChen
# @File : 3_11.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
3-11 有意引发错误：如果你还没有在程序中遇到过索引错误，就尝试引发一个这种错误。在你的一个程序中，修改其中的索引，以引发索引错误。关闭程序前，务必消除这个错误。
"""
guests = ['ZhangSan', 'LiSi', 'WangWu']
# print(guests[3])
print(guests[-1])
# ------------------ example01 ------------------

print("*" * 20)

# ------------------  error01  ------------------
# 报错信息:
# Traceback (most recent call last):
#   File "/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_03/python_work/3_11.py", line 12, in <module>
#     print(guests[3])
# IndexError: list index out of range
# --snip--
# 解决方法:
# 1.使用索引-1，访问最后一个列表元素
#     print(guests[-1])
# ------------------  error01  ------------------
