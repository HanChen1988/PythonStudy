# -*- coding: utf-8 -*-
# @Time : 2021/12/04 17:02 下午
# @Author : HanChen
# @File : 9_14.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
9-14 骰子：模块 random 包含以各种方式生成随机数的函数，其中的 randint() 返回一个位于指定范围内的整数，例如，下面的代码返回一个 1~6 内的整数：
    ----------------------------------------------------------------------------------------------------
    from random import randint
    x = randint(1, 6)
    ----------------------------------------------------------------------------------------------------
    请创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。编写一个名的 roll_die()的方法，它打印位于 1 和骰子面数之间的随机数。创建一个 6 面的骰子，再掷 10次。
    创建一个 10面的骰子和一个 20面的骰子，并将它们都掷 10次。
"""
from random import randint

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)
# ------------------ example01 ------------------