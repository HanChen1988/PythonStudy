# -*- coding: utf-8 -*-
# @Time : 2022/07/10 15:19 下午
# @Author : HanChen
# @File : scatter_squares.py
# @Software: PyCharm

# ------------------ example01 ------------------
# import matplotlib.pyplot as plt
#
# plt.scatter(2, 4)
# plt.show()
# ------------------ example01 ------------------

# print("*" * 20)

# ------------------ example02 ------------------
# import matplotlib.pyplot as plt
#
# # 实参s设置点的尺寸
# plt.scatter(2, 4, s=200)
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()
# ------------------ example02 ------------------

# print("*" * 20)

# ------------------ example03 ------------------
# import matplotlib.pyplot as plt
#
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
#
# plt.scatter(x_values, y_values, s=100)
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()
# ------------------ example03 ------------------

# print("*" * 20)

# ------------------ example04 ------------------
# import matplotlib.pyplot as plt
#
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
#
# plt.scatter(x_values, y_values, s=40)
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# # 设置每个坐标轴的取值范围
# plt.axis([0, 1100, 0, 1100000])
#
# plt.show()
# ------------------ example04 ------------------

# print("*" * 20)

# ------------------ example05 ------------------
# import matplotlib.pyplot as plt
#
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
#
# plt.scatter(x_values, y_values, edgecolor='none', s=40)
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# # 设置每个坐标轴的取值范围
# plt.axis([0, 1100, 0, 1100000])
#
# plt.show()
# ------------------ example05 ------------------

# print("*" * 20)

# ------------------ example06 ------------------
# import matplotlib.pyplot as plt
#
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
#
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# # 设置每个坐标轴的取值范围
# plt.axis([0, 1100, 0, 1100000])
#
# plt.show()
# ------------------ example06 ------------------

# print("*" * 20)

# ------------------ example07 ------------------
# import matplotlib.pyplot as plt
#
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
#
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# # 设置每个坐标轴的取值范围
# plt.axis([0, 1100, 0, 1100000])
#
# plt.show()
# ------------------ example07 ------------------

# print("*" * 20)

# ------------------ example08 ------------------
# import matplotlib.pyplot as plt
#
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
#
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
#             edgecolor='none', s=40)
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# # 设置每个坐标轴的取值范围
# plt.axis([0, 1100, 0, 1100000])
#
# plt.show()
# ------------------ example08 ------------------

# print("*" * 20)

# ------------------ example09 ------------------
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.savefig(r'./images/squares_plot.png', bbox_inches='tight')
# ------------------ example09 ------------------
