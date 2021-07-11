# -*- coding: utf-8 -*-
# @Time : 2021/7/11 21:01 下午
# @Author : HanChen
# @File : 3_5.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
3-5 修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
    以完成练习 3-4 时编写的程序为基础，在程序末尾添加一条 print 语句，指出哪位嘉宾无法赴约。
    修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
    再次打印一系列消息，向名单中的每位嘉宾发出邀请。
"""
guests = ['ZhangSan', 'LiSi', 'WangWu']
message = guests[0] + ", I'd like to invite you to dinner."
print(message)
message = guests[1] + ", I'd like to invite you to dinner."
print(message)
message = guests[2] + ", I'd like to invite you to dinner."
print(message)

message = "\n" + guests[2] + " can't make an appointment at night.\n"
print(message)

guests[2] = "ZhaoLiu"

message = guests[0] + ", I'd like to invite you to dinner."
print(message)
message = guests[1] + ", I'd like to invite you to dinner."
print(message)
message = guests[2] + ", I'd like to invite you to dinner."
print(message)
# ------------------ example01 ------------------
