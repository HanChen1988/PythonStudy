# -*- coding: utf-8 -*-
# @Time : 2021/12/20 21:28 下午
# @Author : HanChen
# @File : remember_me.py
# @Software: Sublime Text

# ------------------ example01 ------------------
# import json
#
# username = input("What is your name? ")
#
# filename = 'username.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("We'll remember you when you come back, " + username + "!")
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# import json

# # 如果以前存储了用户名，就加载它
# # 否则，就提示用户输入用户名并存储它
# filename = 'username.json'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print("We'll remember you when you come back, " + username + "!")
# else:
#     print("Welcome back, " + username + "!")
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# import json
#
# def greet_user():
#     """问候用户，并指出其名字"""
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print("We'll remember you when you come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")
#
# greet_user()
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# import json
#
# def get_stored_username():
#     """如果存储了用户名，就获取它"""
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
# def greet_user():
#     """问候用户，并指出其名字"""
#     username = get_stored_username()
#     if username:
#         print("Welcome back, " + username + "!")
#     else:
#         username = input("What is your name? ")
#         filename = 'username.json'
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print("We'll remember you wehn you come back, " + username + "!")
#
# greet_user()
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
# ------------------ example05 ------------------
