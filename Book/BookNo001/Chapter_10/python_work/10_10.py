# -*- coding: utf-8 -*-
# @Time : 2022/03/14 15:56 下午
# @Author : HanChen
# @File : 10_10.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
10-10 常见单词：访问项目 Gutenberg（http://gutenberg.org/），并找一些你想分析的图书。
        下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
    你可以使用方法 count() 来确定特定的单词或短语在字符串中出现了多少次。
    例如，下面的代码计算 'row' 在一个字符串中出现了多少次：
        >>> line = "Row, row, row your boat"
        >>> print(line.count('row'))
        2
        >>> print(line.lower().count('row'))
        3
    请注意，通过使用 lower() 将字符串转换为小写，可捕获要查找的单词出现的所有次数，而不管其大小写格式如何。
    编写一个程序，它读取你在项目 Gutenberg 中获取的文件，并计算单词 'the' 在每个文件中分别出现了多少次。
"""
def count_words(filename,file_path):
    """计算一个文件中单词 'the' 出现的次数"""
    file_path += filename
    try:
        with open(file_path) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算一个文件中单词 'the' 出现的次数
        num_words = contents.lower().count('the')
        print("The file " + filename + " has about " + str(num_words) + " 'the' words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
file_path='text_files/'
for filename in filenames:
    count_words(filename,file_path)
# ------------------ example01 ------------------