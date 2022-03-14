# -*- coding: utf-8 -*-
# @Time : 2021/12/23 15:03 下午
# @Author : HanChen
# @File : 10_2.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
10-2 C 语言学习笔记：可使用方法 replace() 将字符串中的特定单词都替换为另一个单词。
    下面是一个简单的示例，演示了如何将句子中的'dog'替换为'cat':
        >>> message = "I really like dogs."
        >>> print(message.replace('dog', 'cat'))
        'I really like cats.'
    读取你刚创建的文件 learning_python.txt 中的每一行，将其中的 Python 都替换为另一门语言的名称，如 C。
    将修改后的各行都打印到屏幕上。
"""
filename = 'learning_python.txt'

with open(filename) as f:
    contents = f.read()
    print(contents.replace('Python', 'C'))

print("=" * 20)

filename = 'learning_python.txt'

with open(filename) as f:
    for line in f:
        print(line.rstrip().replace('Python', 'C'))

print("=" * 20)

filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip().replace('Python', 'C'))
# ------------------ example01 ------------------