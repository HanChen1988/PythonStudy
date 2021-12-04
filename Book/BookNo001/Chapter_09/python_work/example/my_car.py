# -*- coding: utf-8 -*-
# @Time : 2021/9/13 23:26 下午
# @Author : HanChen
# @File : my_car.py
# @Software: Sublime Text

# ------------------ example01 ------------------
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# ------------------ example01 ------------------