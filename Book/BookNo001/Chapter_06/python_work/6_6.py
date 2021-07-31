# -*- coding: utf-8 -*-
# @Time : 2021/7/31 17:44 下午
# @Author : HanChen
# @File : 6_6.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
6-6 调查：在6.3.1节编写的程序 favorite_languages.py 中执行以下操作。
    创建一个应该会接受调查的人员名单，其中这些人已包含在字典中，而其他人未包含在字典中。
    遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s faorite language is " +
        language.title() + ".")

print("-" * 20)

coders = ['jen', 'sarah', 'edward', 'phil', 'zhangsan', 'lisi', 'wangwu', 'zhaoliu']

for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll," + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")
# ------------------ example01 ------------------
