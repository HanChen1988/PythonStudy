# -*- coding: utf-8 -*-
# @Time : 2021/7/28 07:42 上午
# @Author : HanChen
# @File : 5_8.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
5-8 以特殊方式跟管理员打招呼：创建一个至少包含 5个用户名的列表，且其中一个用户名为'admin'。想象你要编写代码，在每位用户登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。
    如果用户名为'admin'，就打印一条特殊的问候消息，如“Hello admin,would you like to see a status report?”
    否则，打印一条普通的问候消息，如“Hello Eric,thank you for logging in again”。
"""
usernames = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'admin']

for username in usernames:
    if username == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello " + username + ",thank you for logging in again.")
# ------------------ example01 ------------------

