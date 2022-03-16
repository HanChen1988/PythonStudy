# -*- coding: utf-8 -*-
# @Time : 2022/03/15 23:13 下午
# @Author : HanChen
# @File : names.py
# @Software: Sublime Text

# ------------------ example01 ------------------
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".") 
# ------------------ example01 ------------------
