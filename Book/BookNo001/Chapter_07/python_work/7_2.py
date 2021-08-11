# -*- coding: utf-8 -*-
# @Time : 2021/8/10 21:39 下午
# @Author : HanChen
# @File : 7_2.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
7-2 餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
"""
party_size = input("How many people are in your dinner party tonight? ")
party_size = int(party_size)

if party_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")
# ------------------ example01 ------------------