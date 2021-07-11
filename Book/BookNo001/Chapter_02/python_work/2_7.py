# -*- coding: utf-8 -*-
# @Time : 2021/7/5 00:2 下午
# @Author : HanChen
# @File : 2_7.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
2-7 剔除人名中的空白：存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"和"\n"各一次。
    打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip()、rstrip()、strip()对人名进行处理，并将结果打印出来。
"""
name = "\tAlbert Einstein\n"
print(name)
# 使用剔除函数lstrip()
print(name.lstrip())
# 使用剔除函数rstrip()
print(name.rstrip())
# 使用剔除函数strip()
print(name.strip())
# ------------------ example01 ------------------
