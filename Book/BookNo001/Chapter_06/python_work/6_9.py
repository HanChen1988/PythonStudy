# -*- coding: utf-8 -*-
# @Time : 2021/7/31 18:44 下午
# @Author : HanChen
# @File : 6_9.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
6-9 喜欢的地方：创建一个名为 favorite_places 的字典。在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的 1~3 个地方。为让这个练习更有趣些，可让一些朋友指出他们喜欢的几个地方。遍历整个字典，并将其中每个人的名字及其喜欢的地方打印出来。
"""
favorite_places = {
    'zhangsan': ['beijing'],
    'lisi': ['hangzhou', 'suzhou'],
    'wangwu': ['guilin', 'guangzhou', 'haikou'],
}

for name,places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place)
# ------------------ example01 ------------------
