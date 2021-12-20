# -*- coding: utf-8 -*-
# @Time : 2021/12/19 11:27 上午
# @Author : HanChen
# @File : number_reader.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
# ------------------ example01 ------------------
