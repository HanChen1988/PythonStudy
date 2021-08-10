# -*- coding: utf-8 -*-
# @Time : 2021/8/10 21:39 下午
# @Author : HanChen
# @File : 7_9.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
7-9 五香烟熏牛肉（pastrami）卖完了：使用为完成练习 7-8 而创建的列表 sandwich_orders，并确保 'pastrami' 在其中至少出现了三次。
    在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；
    再使用一个 while 循环将列表 sandwich_orders 中的 'pastrami' 都删除。
    确认最终的列表 finished_sandwiches 中不包含 'pastrmi'。

    7-8 熟食店：创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名字；再创建一个名为 finished_sandwiches 的空列表。
        遍历列表 sandwich_orders，对于其中的每种三明治，都打印一条消息，如 I made your tuna sandwich，并将其移到列表finished_sandwiches。
        所有三明治都制作好后，打印一条消息，将这些三明治列出来。
"""
print("Pastrami is sold out.\n")

sandwich_orders = ['sardine', 'pastrami', 'chocolate', 'chicken', 'pastrami', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = sandwich_orders

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())
# ------------------ example01 ------------------

