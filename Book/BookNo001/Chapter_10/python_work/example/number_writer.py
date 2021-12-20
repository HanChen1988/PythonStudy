# -*- coding: utf-8 -*-
# @Time : 2021/12/19 11:25 上午
# @Author : HanChen
# @File : number_writer.py
# @Software: Sublime Text

# ------------------ example01 ------------------
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
# ------------------ example01 ------------------
