# -*- coding: utf-8 -*-
# @Time : 2022/05/07 7:18 上午
# @Author : HanChen
# @File : mpl_squares.py
# @Software: PyCharm

# ------------------ example01 ------------------
# import matplotlib.pyplot as plt
#
# squares = [1, 4, 9, 16, 25]
# # 将这个列表传递给函数plot(),这个函数尝试根据这些数字绘制出有意义的图形。
# plt.plot(squares)
# # plt.show()打开matplotlib查看器,并显示绘制的图形。
# plt.show()
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# import matplotlib.pyplot as plt
#
# squares = [1, 4, 9, 16, 25]
# plt.plot(squares, linewidth=5)
#
# # 设置图表标题,并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', labelsize=14)
#
# plt.show()
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题,并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
# ------------------ example03 ------------------
