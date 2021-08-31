# -*- coding: utf-8 -*-
# @Time : 2021/8/31 07:48 上午
# @Author : HanChen
# @File : 8_16.py
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
import user_profile

user_profile1 = user_profile.build_profile('san', 'zhang')
print(user_profile1)
user_profile2 = user_profile.build_profile('san', 'zhang', location='beijing')
print(user_profile2)
user_profile3 = user_profile.build_profile('san', 'zhang', location='beijing', field='programming')
print(user_profile3)

print("-" * 20)

from user_profile import build_profile

user_profile1 = build_profile('san', 'zhang')
print(user_profile1)
user_profile2 = build_profile('san', 'zhang', location='beijing')
print(user_profile2)
user_profile3 = build_profile('san', 'zhang', location='beijing', field='programming')
print(user_profile3)

print("-" * 20)

from user_profile import build_profile as bp

user_profile1 = bp('san', 'zhang')
print(user_profile1)
user_profile2 = bp('san', 'zhang', location='beijing')
print(user_profile2)
user_profile3 = bp('san', 'zhang', location='beijing', field='programming')
print(user_profile3)

print("-" * 20)

import user_profile as up

user_profile1 = up.build_profile('san', 'zhang')
print(user_profile1)
user_profile2 = up.build_profile('san', 'zhang', location='beijing')
print(user_profile2)
user_profile3 = up.build_profile('san', 'zhang', location='beijing', field='programming')
print(user_profile3)

print("-" * 20)

from user_profile import *

user_profile1 = build_profile('san', 'zhang')
print(user_profile1)
user_profile2 = build_profile('san', 'zhang', location='beijing')
print(user_profile2)
user_profile3 = build_profile('san', 'zhang', location='beijing', field='programming')
print(user_profile3)
# ------------------ example01 ------------------