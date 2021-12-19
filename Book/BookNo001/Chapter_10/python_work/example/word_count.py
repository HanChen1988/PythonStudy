# -*- coding: utf-8 -*-
# @Time : 2021/12/18 11:02 上午
# @Author : HanChen
# @File : word_count.py
# @Software: Sublime Text

# ------------------ example01 ------------------
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename
    
    try:
        with open(filepath) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
        
filename = 'alice.txt'
count_words(filename)
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename
    
    try:
        with open(filepath) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
        
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename
    
    try:
        with open(filepath) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
        
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
# ------------------ example03 ------------------
