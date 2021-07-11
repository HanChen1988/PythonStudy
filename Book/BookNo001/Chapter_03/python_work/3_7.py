# -*- coding: utf-8 -*-
# @Time : 2021/7/11 21:24 下午
# @Author : HanChen
# @File : 3_7.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
3-7 缩减名单：你刚得知新购买的餐桌无法即使送达，因此只能邀请两位嘉宾。
    以完成练习 3-6 时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
    使用 pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
    对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
    使用 del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
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

message = "\nJust learned that the newly purchased table cannot be delivered, so we can only invite two guests.\n"
print(message)

popped_guest = guests.pop()
message = popped_guest + ", I'm sorry I can't invite you to dinner."
print(message)
popped_guest = guests.pop(-1)
message = popped_guest + ", I'm sorry I can't invite you to dinner."
print(message)
popped_guest = guests.pop(2)
message = popped_guest + ", I'm sorry I can't invite you to dinner."
print(message)
popped_guest = guests.pop(0)
message = popped_guest + ", I'm sorry I can't invite you to dinner."
print(message)
message = guests[0] + ", I'd like to invite you to dinner."
print(message)
message = guests[1] + ", I'd like to invite you to dinner.\n"
print(message)

del guests[0]
del guests[0]

print(guests)
# ------------------ example01 ------------------

