# -*- coding: utf-8 -*-
# @Time : 2021/8/10 21:39 下午
# @Author : HanChen
# @File : 7_10.py
# @Software: Sublime Text

# ------------------ example01 ------------------
"""
7-10 梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。
    使用类似于“If you could visit one place in the world,where would you go?”的提示，并编写一个打印调查结果的代码块。
"""
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")
# ------------------ example01 ------------------
