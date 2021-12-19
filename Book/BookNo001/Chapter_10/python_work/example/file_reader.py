# -*- coding: utf-8 -*-
# @Time : 2021/12/12 09:47 上午
# @Author : HanChen
# @File : file_reader.py
# @Software: Sublime Text

# ------------------ example01 ------------------
with open('/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
with open('/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
filename = 'pi_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    for line in file_object:
        print(line)
# ------------------ example03 ------------------

print("*" * 20)

# ------------------ example04 ------------------
filename = 'pi_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())
# ------------------ example04 ------------------

print("*" * 20)

# ------------------ example05 ------------------
filename = 'pi_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
# ------------------ example05 ------------------
