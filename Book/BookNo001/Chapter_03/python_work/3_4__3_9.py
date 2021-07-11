# -*- coding: utf-8 -*-
# @Time : 2021/7/11 20:41 下午
# @Author : HanChen
# @File : 3_4__3_9.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
3-4 嘉宾名单：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后，使用这个列表打印消息，邀请这些人来与你共进晚餐。
3-9 晚餐嘉宾：在完成练习 3-4~练习 3-7 时编写的程序之一中，使用len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
"""
guests = ['ZhangSan', 'LiSi', 'WangWu']
message = guests[0] + ", I'd like to invite you to dinner."
print(message)
message = guests[1] + ", I'd like to invite you to dinner."
print(message)
message = guests[2] + ", I'd like to invite you to dinner."
print(message)

# 使用len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
message = "\nI invited " + str(len(guests)) + " people to have dinner with me."
print(message)
# ------------------ example01 ------------------
