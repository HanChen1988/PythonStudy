# -*- coding: utf-8 -*-
# @Time : 2021/7/11 21:10 下午
# @Author : HanChen
# @File : 3_6.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
3-6 添加嘉宾：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
    以完成练习 3-4 或 练习 3-5 时编写的程序为基础，在程序末尾添加一条 print 语句，指出你找到了一个更大的餐桌。
    使用 insert() 将一位新嘉宾添加到名单开头。
    使用 insert() 将另一位新嘉宾添加到名单中间。
    使用 append() 将最后一位新嘉宾添加到名单末尾。
    打印一系列消息，向名单中的每位嘉宾发出邀请。
"""
guests = ['ZhangSan', 'LiSi', 'WangWu']
message = guests[0] + ", I'd like to invite you to dinner."
print(message)
message = guests[1] + ", I'd like to invite you to dinner."
print(message)
message = guests[2] + ", I'd like to invite you to dinner."
print(message)

message = "\nI found a bigger restaurant.\n"
print(message)

# 使用 insert() 将一位新嘉宾添加到名单开头。
guests.insert(0, "ZhaoLiu")
# 使用 insert() 将另一位新嘉宾添加到名单中间。
guests.insert(2, "SunQi")
# 使用 append() 将最后一位新嘉宾添加到名单末尾。
guests.append("ZhouBa")

message = guests[0] + ", I'd like to invite you to dinner."
print(message)
message = guests[1] + ", I'd like to invite you to dinner."
print(message)
message = guests[2] + ", I'd like to invite you to dinner."
print(message)
message = guests[3] + ", I'd like to invite you to dinner."
print(message)
message = guests[4] + ", I'd like to invite you to dinner."
print(message)
message = guests[5] + ", I'd like to invite you to dinner."
print(message)
# ------------------ example01 ------------------

