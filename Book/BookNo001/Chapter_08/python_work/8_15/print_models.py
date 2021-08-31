# -*- coding: utf-8 -*-
# @Time : 2021/8/31 07:48 上午
# @Author : HanChen
# @File : print_models.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
8-15 打印模型：将示例 print_models.py 中的函数放在另一个名为 printing_functions.py 的文件中；在 print_models.py 的开头编写一条 import 语句，并修改这个文件以使用导入的函数。
"""
import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
# ------------------ example01 ------------------