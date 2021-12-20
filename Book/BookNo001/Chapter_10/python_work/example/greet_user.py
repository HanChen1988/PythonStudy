# -*- coding: utf-8 -*-
# @Time : 2021/12/20 21:30 下午
# @Author : HanChen
# @File : greet_user.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
# ------------------ example01 ------------------
