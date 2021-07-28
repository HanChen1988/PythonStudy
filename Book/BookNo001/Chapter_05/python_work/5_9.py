# -*- coding: utf-8 -*-
# @Time : 2021/7/28 07:43 上午
# @Author : HanChen
# @File : 5_9.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
5-9 处理没有用户的情形：在为完成练习 5-8 编写的程序中，添加一条 if 语句，检查用户名列表是否为空。
    如果为空，就打印消息“We need to find some users!”
    删除列表中的所有用户名，确定将打印正确的消息。
"""
usernames = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'admin']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello " + username + ",thank you for logging in again.")
else:
    print("We need to find some users!")

print("-" * 20)

usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello " + username + ",thank you for logging in again.")
else:
    print("We need to find some users!")
# ------------------ example01 ------------------

