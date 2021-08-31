# -*- coding: utf-8 -*-
# @Time : 2021/8/31 07:48 上午
# @Author : HanChen
# @File : printing_functions.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
8-15 打印模型：将示例 print_models.py 中的函数放在另一个名为 printing_functions.py 的文件中；在 print_models.py 的开头编写一条 import 语句，并修改这个文件以使用导入的函数。
"""

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
# ------------------ example01 ------------------