# -*- coding: utf-8 -*-
# @Time : 2021/12/14 07:40 上午
# @Author : HanChen
# @File : pi_string.py
# @Software: Sublime Text

# ------------------ example01 ------------------
filename = 'pi_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
filename = 'pi_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
filename = 'pi_million_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
# ------------------ example03 ------------------

print("*" * 20)

# ------------------ example04 ------------------
filename = 'pi_million_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
# ------------------ example04 ------------------
