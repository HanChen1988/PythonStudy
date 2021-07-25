# 第5章：if语句

>   ​		编程时经常需要检查一系列条件，并据此决定采取什么措施。在Python中，if语句让你能够检查程序的当前状态，并据此采取相应的措施。
>
>   ​		在本章中，你将学习条件测试，以检查感兴趣的任何条件。你将学习简单的if语句，以及创建一系列复杂的if语句来确定当前到底处于什么情形。接下来，你将把学到的知识应用于列表，以编写for循环，以一种方式处理列表中的大多数元素，并以另一种不同的方式处理包含特定值的元素。

## 5.1 一个简单示例

>   ​		遍历一个列表，并以首字母大写的方式打印其中的汽车名，但对于汽车名'bmw'，以全大写的方式打印。
>
>   
>
>   示例：
>
>   ```python
>   # car.py
>   cars = ['audi', 'bmw', 'subaru', 'toyota']
>   
>   for car in cars:
>        # 检查当前的汽车名是否是'bmw'。如果是，就以全大写的方式打印它；否则就以首字母大写的方式打印。
>    	if car == 'bmw':
>            print(car.upper())
>    	else:
>            print(car.title())
>   ```
>
>   输出语句：
>
>   ```python
>   Audi
>   BMW
>   Subaru
>   Toyota
>   ```

## 5.2 条件测试

>   ​		每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试。
>
>   ​		Python根据条件测试的值为True还是False来决定是否执行if语句中的代码。
>
>   ​		如果条件测试的值为True，Python就执行紧跟在if语句后面的代码；如果为False，Python就忽略这些代码。

### 5.2.1 检查是否相等

>   ​		大多数条件测试都将一个变量的当前值同特定值进行比较。
>
>   ​		一个等号是陈述；二个等号是发问。
>
>   
>
>   示例1：
>
>   ```python
>   # 使用一个等号将car的值设置为'bmw'
>   car = 'bmw'
>   # 使用两个等号（==）检查car的值是否为'bmw'。这个相等运算符在它两边的值相等时返回True，否则返回False。
>   print(car == 'bmw')
>   ```
>
>   输出语句：
>
>   ```python
>   True
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   car = 'audi'
>   print(car == 'bmw')
>   ```
>
>   输出语句：
>
>   ```python
>   False
>   ```

### 5.2.2 检查是否相等时不考虑大小写

>   ​		在Python中检查是否相等时区分大小写。
>
>   ​		如果大小写很重要，这种行为有其优点。但如果大小写无关紧要，而只想检查变量的值，可将变量的值转换为小写，再进行比较。
>
>   ​		函数lower()不会修改存储在变量中的值，因此进行这样的比较时不会影响原来的变量。
>
>   ​		网站采用类似的方式让用户输入的数据符合特定的格式。
>
>   
>
>   示例1：
>
>   ```python
>   car = 'Audi'
>   print(car == 'audi')
>   ```
>
>   输出语句：
>
>   ```python
>   False
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   car = 'Audi'
>   print(car.lower() == 'audi')
>   print(car)
>   ```
>
>   输出语句：
>
>   ```python
>   True
>   Audi
>   ```

### 5.2.3 检查是否不相等

>​		要判断两个值是否不等，可结合使用惊叹号和等号（!=），其中的惊叹号表示不，在很多编程语言中都如此。
>
>​		你编写的大多数条件表达式都检查两个值是否相等，但有时候检查两个值是否不等的效率更高。
>
>
>
>示例：
>
>```python
># toppings.py
>requested_topping = 'mushrooms'
>
>if requested_topping != 'anchovies':
>        print("Hold the anchovies!")
>```
>
>输出语句：
>
>```python
>Hold the anchovies!
>```

### 5.2.4 比较数字

>   ​		在if语句中可使用各种数学比较，这让你能够直接检查关心的条件。
>
>   
>
>   示例1：
>
>   ```python
>   # 检查两个数字是否相等
>   age = 18
>   print(age == 18)
>   ```
>
>   输出语句：
>
>   ```python
>   True
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # 检查两个数字是否不等
>   # magic_number.py
>   answer = 17
>   if answer != 42:
>    	print("That is not the correct answer. Please try again!")
>   ```
>
>   输出语句：
>
>   ```python
>   That is not the correct answer. Please try again!
>   ```
>
>   
>
>   示例3：
>
>   ```python
>   age = 19
>   # 小于
>   print("age < 21:")
>   print(age < 21)
>   # 小于等于
>   print("age <= 21:")
>   print(age <= 21)
>   # 大于
>   print("age > 21:")
>   print(age > 21)
>   # 大于等于
>   print("age >= 21")
>   print(age >= 21)
>   ```
>
>   输出语句：
>
>   ```python
>   age < 21:
>   True
>   age <= 21:
>   True
>   age > 21:
>   False
>   age >= 21
>   False
>   ```

### 5.2.5 检查多个条件

>   ​		你可能想同时检查多个条件，关键字and和or可助你一臂之力。

#### 1. 使用and检查多个条件

>   ​		要检查是否两个条件都为True，可使用关键字and将两个条件测试合二为一；如果每个测试都通过了，整个表达式就为True；如果至少有一个测试没有通过，整个表达式就为False。
>
>   ​		为改善可读性，可将每个测试都分别放在一对括号内，但并非必须这样做。
>
>   
>
>   示例：
>
>   ```python
>   # 定义了两个用于存储年龄的变量:age_0和age_1
>   age_0 = 22
>   age_1 = 18
>   print("(age_0 >= 21) and (age_1 >= 21):")
>   # 检查这两个变量是否都大于或等于21
>   print((age_0 >= 21) and (age_1 >= 21))
>   
>   age_1 = 22
>   print("(age_0 >= 21) and (age_1 >= 21):")
>   print((age_0 >= 21) and (age_1 >= 21))
>   ```
>
>   输出语句：
>
>   ```python
>   (age_0 >= 21) and (age_1 >= 21):
>   False
>   (age_0 >= 21) and (age_1 >= 21):
>   True
>   ```

#### 2. 使用or检查多个条件

>   ​		关键字or也能够让你检查多个条件，但只要至少有一个条件满足，就能通过整个测试。仅当两个测试都没有通过时，使用or的表达式才为False。
>
>   
>
>   示例：
>
>   ```python
>   age_0 = 22
>   age_1 = 18
>   print("(age_0 >= 21) or (age_1 >= 21):")
>   print((age_0 >= 21) or (age_1 >= 21))
>   
>   age_0 = 18
>   print("(age_0 >= 21) or (age_1 >= 21):")
>   print((age_0 >= 21) or (age_1 >= 21))
>   ```
>
>   输出语句：
>
>   ```python
>   (age_0 >= 21) or (age_1 >= 21):
>   True
>   (age_0 >= 21) or (age_1 >= 21):
>   False
>   ```

### 5.2.6 检查特定值是否包含在列表中

>   ​		有时候，执行操作前必须检查列表是否包含特定的值。
>
>   ​		要判断特定的值是否已包含在列表中，可使用关键字in。
>
>   
>
>   示例：
>
>   ```python
>   requested_toppings = ['mushroom', 'onions', 'pineapple']
>   print("'mushroom' in requested_toppings")
>   print('mushroom' in requested_toppings)
>   
>   print("'pepperoni' in requested_toppings")
>   print('pepperoni' in requested_toppings)
>   ```
>
>   输出语句：
>
>   ```python
>   'mushroom' in requested_toppings
>   True
>   'pepperoni' in requested_toppings
>   False
>   ```

### 5.2.7 检查特定值是否不包含在列表中

>   ​		还有些时候，确定特定的值未包含在列表中很重要；在这种情况下，可使用关键字not in。
>
>   
>
>   示例：
>
>   ```python
>   # banned_users.py
>   banned_users = ['andrew', 'carolina', 'david']
>   user = 'marie'
>   # 如果user的值未包含在列表banned_users中,Python将返回True,进而执行缩进的代码行
>   if user not in banned_users:
>        print(user.title() + ", you can post a response if you wish.")
>   ```
>
>   输出语句：
>
>   ```python
>   Marie, you can post a response if you wish.
>   ```

### 5.2.8 布尔表达式

>   ​		布尔表达式的结果要么为True，要么为False。
>
>   ​		布尔值通常用于记录条件。
>
>   ​		在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。
>
>   
>
>   示例：
>
>   ```python
>   game_active = True
>   print("game_active:")
>   print(game_active)
>   can_edit = False
>   print("can_edit:")
>   print(can_edit)
>   ```
>
>   输出语句：
>
>   ```python
>   game_active:
>   True
>   can_edit:
>   False
>   ```

## 5.3 if语句

>   ​		if语句有很多种，选择使用哪种取决于要测试的条件数。
>
>   ​		如果你只想执行一个代码块，就使用if-elif-else结构；如果要运行多个代码块，就使用一系列独立的if语句。

### 5.3.1 简单的 if 语句

>   ​		最简单的if语句只有一个测试和一个操作。
>
>   ​		在if语句中可包含任何条件测试，而在紧跟在测试后面的缩进代码块中，可执行任何操作。如果条件测试的结果为True,Python就会执行紧跟在if语句后面的代码；否则Python将忽略这些代码。
>
>   ​		在紧跟在if语句后面的代码块中，可根据需要包含任意数量的代码行。
>
>   
>
>   示例1：
>
>   ```python
>   # voting.py
>   age = 19
>   if age >= 18:
>        print("You are old enough to vote!")
>   ```
>
>   输出语句：
>
>   ```python
>   You are old enough to vote!
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   age = 19
>   if age >= 18:
>        print("You are old enough to vote!")
>        print("Have you registered to vote yet?")
>   ```
>
>   输出语句：
>
>   ```python
>   You are old enough to vote!
>   Have you registered to vote yet?
>   ```

### 5.3.2 if-else 语句

>   ​		经常需要在条件测试通过了执行一个操作，并在没有通过时执行另一个操作；在这种情况下，可使用Python提供的if-else语句。
>
>   
>
>   示例：
>
>   ```python
>   age = 17
>   if age >= 18:
>       print("You are old enough to vote!")
>       print("Have you registered to vote yet?")
>   else:
>       print("Sorry, you are too young to vote.")
>       print("Please register to vote as soon as you turn 18!")
>   ```
>
>   输出语句：
>
>   ```python
>   Sorry, you are too young to vote.
>   Please register to vote as soon as you turn 18!
>   ```

### 5.3.3 if-elif-else 结构

>   ​		经常需要检查超过两个的情形，为此可使用Python的if-elif-else结构。
>
>   ​		Python只执行if-elif-else结构中的一个代码块，它依次检查每个条件测试，直到遇到通过了的条件测试。测试通过后，Python将执行紧跟在它后面的代码，并跳过余下的测试。
>
>   
>
>   示例1：
>
>   ```python
>   """
>   看一个根据年龄段收费的游乐场:
>   4岁以下免费;
>   4~18岁收费5美元;
>   18岁（含）以上收费10美元。
>   """
>   # amusement_park.py
>   age = 12
>   
>   if age < 4:
>       print("Your admission cost is $0.")
>   elif age < 18:
>       print("Your admission cost is $5.")
>   else:
>       print("Your admission cost is $10.")
>   ```
>
>   输出语句：
>
>   ```python
>   Your admission cost is $5.
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   """
>   看一个根据年龄段收费的游乐场:
>   4岁以下免费;
>   4~18岁收费5美元;
>   18岁（含）以上收费10美元。
>   """
>   # amusement_park.py
>   age = 12
>   if age < 4:
>       price = 0
>   elif age < 18:
>       price = 5
>   else:
>       price = 10
>   
>   print("Your admission cost is $" + str(price) + ".")
>   ```
>
>   输出语句:
>
>   ```python
>   Your admission cost is $5.
>   ```

### 5.3.4 使用多个elif代码块

>   ​		可根据需要使用任意数量的elif代码块。
>
>   
>
>   示例：
>
>   ```python
>   """
>   看一个根据年龄段收费的游乐场:
>   4岁以下免费;
>   4~18岁收费5美元;
>   18岁（含）以上收费10美元；
>   65岁（含）以上可以半价（5美元）。
>   """
>   # amusement_park.py
>   age = 12
>   
>   if age < 4:
>       price = 0
>   elif age < 18:
>       price = 5
>   elif age < 65:
>       price = 10
>   else:
>       price = 5
>   
>   print("Your admission cost is $" + str(price) + ".")
>   ```
>
>   输出语句：
>
>   ```python
>   Your admission cost is $5.
>   ```

### 5.3.5 省略 else 代码块

>   ​		Python并不要求if-elif结构后面必须有else代码块。在有些情况下，else代码块很有用；而其他一些情况下，使用一条elif语句来处理特定的情形更清晰。
>
>   ​		else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行，这可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个elif代码块来代替else代码块。这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。
>
>   
>
>   示例：
>
>   ```python
>   age = 12
>   
>   if age < 4:
>       price = 0
>   elif age < 18:
>       price = 5
>   elif age < 65:
>       price = 10
>   elif age >= 65:
>       price = 5
>   
>   print("Your admission cost is $" + str(price) + ".")
>   ```
>
>   输出语句：
>
>   ```python
>   Your admission cost is $5.
>   ```

### 5.3.6 测试多个条件

>   ​		有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含elif和else代码块的简单if语句。在可能有多个条件为True，且你需要在每个条件为True时都采取相应措施时，适合使用这种方法。
>
>   
>
>   示例：
>
>   ```python
>   # toppings.py
>   requested_toppings = ['mushrooms', 'extra cheese']
>   
>   if 'mushrooms' in requested_toppings:
>       print("Adding mushrooms.")
>   if 'pepperoni' in requested_toppings:
>       print("Adding pepperoni.")
>   if 'extra cheese' in requested_toppings:
>       print("Adding extra cheese.")
>       
>   print("\nFinished making your pizza!")
>   ```
>
>   输出语句：
>
>   ```python
>   Adding mushrooms.
>   Adding extra cheese.
>   
>   Finished making your pizza!
>   ```

## 5.4 使用 if 语句处理列表

>   ​		通过结合使用if语句和列表，可完成一些有趣的任务：对列表中特定的值做特殊处理；高效地管理不断变化的情形；证明代码在各种情况下都将按预期那样运行。

### 5.4.1 检查特殊元素

