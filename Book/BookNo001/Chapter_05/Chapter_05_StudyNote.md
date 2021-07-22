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
>       # 检查当前的汽车名是否是'bmw'。如果是，就以全大写的方式打印它；否则就以首字母大写的方式打印。
>       if car == 'bmw':
>           print(car.upper())
>       else:
>           print(car.title())
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
>    print("Hold the anchovies!")
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
>       print("That is not the correct answer. Please try again!")
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

#### 2. 使用or检查多个条件


