# -*- coding: utf-8 -*-
# @Time : 2021/7/28 07:05 上午
# @Author : HanChen
# @File : 5_6.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
5-6 人生的不同阶段：设置变量 age 的值，再编写一个 if-elif-else 结构，根据 age 的值判断处于人生的哪个阶段。
    如果一个人的年龄小于 2 岁，就打印一条消息，指出他是婴儿。
    如果一个人的年龄为 2（含）~4 岁，就打印一条消息，指出他正蹒跚学步。
    如果一个人的年龄为 4（含）~13 岁，就打印一条消息，指出他是儿童。
    如果一个人的年龄为 13（含）~20 岁，就打印一条消息，指出他是青少年。
    如果一个人的年龄为 20（含）~65 岁，就打印一条消息，指出他是成年人。
    如果一个人的年龄超过 65（含）岁，就打印一条消息，指出他是老年人。
"""
age = 10

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")
# ------------------ example01 ------------------

