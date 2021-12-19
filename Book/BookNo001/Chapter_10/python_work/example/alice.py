# -*- coding: utf-8 -*-
# @Time : 2021/12/18 11:02 上午
# @Author : HanChen
# @File : alice.py
# @Software: Sublime Text

# ------------------ example01 ------------------
# filename = 'alice.txt'

# with open(filename) as f_obj:
#     contents = f_obj.read()
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
title = "Alice in Wonderland"
print(title.split())
# ------------------ example03 ------------------

print("*" * 20)

# ------------------ example04 ------------------
filename = 'alice.txt'
filepath = "/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/" + filename

try:
    with open(filepath) as f_obj:
        contents = f_obj.read()
except:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
# ------------------ example04 ------------------
