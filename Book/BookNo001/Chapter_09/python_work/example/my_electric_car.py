# -*- coding: utf-8 -*-
# @Time : 2021/9/14 21:24 下午
# @Author : HanChen
# @File : my_electric_car.py
# @Software: Sublime Text

# ------------------ example01 ------------------
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# ------------------ example01 ------------------