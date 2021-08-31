# -*- coding: utf-8 -*-
# @Time : 2021/8/31 07:48 上午
# @Author : HanChen
# @File : user_profile.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
8-16 导入：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。在主程序文件中，使用下述各种方法导入这个函数，再调用它：
    import module_name
    from module_name import function_name
    from module_name import function_name as fn
    import module_name as mn
    from module_name import *

    8-13 用户简介：复制前面的程序 user_profile.py，在其中调用 build_profile()来创建有关你的简介；调用这个函数三次，每次都提供不同数量的实参。
"""
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
# ------------------ example01 ------------------