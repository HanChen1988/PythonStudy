# -*- coding: utf-8 -*-
# @Time : 2021/7/17 22:57 下午
# @Author : HanChen
# @File : 4_5.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
4-5 计算 1~1000000的总和：创建一个列表，其中包含数字 1~1000000，再使用min() 和 max()核实该列表确实是从1开始，到1000000结束的。另外，对这个列表调用函数 sum()，看看Python将一百万个数字相加需要多长时间。
"""
numbers = list(range(1,1000001))
# 取最小值
min_number = min(numbers)
print("min_number: " + str(min_number))
# 取最大值
max_number = max(numbers)
print("max_number: " + str(max_number))
# 求和
sum_number = sum(numbers)
print("sum_number: " + str(sum_number))
# ------------------ example01 ------------------
