# -*- coding: utf-8 -*-
# @Time : 2021/8/10 21:39 下午
# @Author : HanChen
# @File : 7_2.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
7-2 餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
"""
users = input("How many people the user has to eat: ")
users = int(users)

if users > 8:
    print("\nThere is no empty table.")
else:
    print("\nFree table.")
# ------------------ example01 ------------------
