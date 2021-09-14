# -*- coding: utf-8 -*-
# @Time : 2021/9/14 21:24 下午
# @Author : HanChen
# @File : my_cars.py
# @Software: Sublime Text

# ------------------ example01 ------------------
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
# ------------------ example01 ------------------

print("*" * 20)

# ------------------ example02 ------------------
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
# ------------------ example02 ------------------

print("*" * 20)

# ------------------ example03 ------------------
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
# ------------------ example03 ------------------
