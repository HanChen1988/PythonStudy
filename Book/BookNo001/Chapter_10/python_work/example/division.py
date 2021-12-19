# -*- coding: utf-8 -*-
# @Time : 2021/12/18 10:05 上午
# @Author : HanChen
# @File : division.py
# @Software: Sublime Text

# ------------------ example01 ------------------
# print(5/0)
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
# ------------------ example04 ------------------
