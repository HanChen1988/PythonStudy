# -*- coding: utf-8 -*-
# @Time : 2021/7/4 3:47 下午
# @Author : HanChen
# @File : hello_world.py
# @Software: Sublime Text

# ------------------ example01 ------------------
# 使用变量打印"Hello Python world!"
message = "Hello Python world!"
print(message)
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
# 使用同一变量打印两条消息
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
# 使用变量打印"Hello Python Crash Course reader!"
message = "Hello Python Crash Course reader!"
print(mesage)
# ------------------ example03 ------------------

print("*" * 20)

# ------------------  error03  ------------------
# 报错信息:
# Traceback (most recent call last):
#   File "/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_02/python_work/hello_world.py", line 29, in <module>
#     print(mesage)
# NameError: name 'mesage' is not defined
# --snip--
# 解决方法:
# 1.正确拼写变量名
#     print(message)
# ------------------  error03  ------------------