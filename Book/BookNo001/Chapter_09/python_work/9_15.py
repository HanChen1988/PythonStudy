# -*- coding: utf-8 -*-
# @Time : 2021/12/04 17:27 下午
# @Author : HanChen
# @File : 9_15.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-15 Python Module of the Week：要了解 Python标准库，一个很不错的资源是网站 Python Module of the Week。
    请访问 http://pymotw.com/ 并查看其中的目录，在其中找一个你感兴趣的模块进行探索，或阅读模块 collections 和 random 的文档。
"""
import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA   :', data)

data_string = json.dumps(data)
print('ENCODED:', data_string)

decoded = json.loads(data_string)
print('DECODED:', decoded)

print('ORIGINAL:', type(data[0]['b']))
print('DECODED :', type(decoded[0]['b']))
# ------------------ example01 ------------------