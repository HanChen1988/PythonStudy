# 第8章：函数

>   ​		在本章中，你将学习编写函数。函数是带名字的代码块，用于完成具体的工作。
>
>   ​		要执行函数定义的特定任务，可调用该函数。需要在程序中多次执行同一项任务时，你无需反复编写完成该任务的代码，而只需调用执行该任务的函数，让Python运行其中的代码。你将发现，通过使用函数，程序的编写、阅读、测试和修复都将更容易。
>
>   ​		在本章中，你还会学习向函数传递信息的方式。你将学习如何编写主要任务是显示信息的函数，还有用于处理数据并返回一个或一组值的函数。最后，你将学习如何将函数在被称为模块的独立文件中，让主程序文件的组织更为有序。

## 8.1 定义函数

>   示例：
>
>   ```python
>   # greeter.py
>   # 使用关键字def来告诉Python你要定义一个函数。这是函数定义，向Python指出了函数名，还可能在括号内指出函数为完成其任务需要什么样的信息。即便括号是空的，括号也必不可少。最后，定义以冒号结尾。
>   def greet_user():
>        # 文本是被称为文档字符串（docstring）的注释，描述了函数是做什么的。文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档。
>        """显示简单的问候语"""
>        print("Hello!")
>   
>   # 要使用这个函数，可调用它。函数调用让Python执行函数的代码。要调用函数，可依次指定函数名以及用括号括起的必要信息。
>   greet_user()
>   ```
>
>   输出语句：
>
>   ```python
>   Hello!
>   ```

### 8.1.1 向函数传递信息

>   示例：
>
>   ```python
>   def greet_user(username):
>        """显示简单的问候语"""
>        print("Hello, " + username.title() + "!")
>       
>   greet_user('jesse')
>   ```
>
>   输出语句：
>
>   ```python
>   Hello, Jesse!
>   ```

### 8.1.2 实参和形参

>   ​		形参：函数完成其工作所需的一项信息。
>
>   ​		实参：调用函数时传递给函数的信息。我们调用函数时，将要让函数使用的信息放在括号内。
>
>   ​		注意：大家有时候会形参、实参不分，因此如果你看到有人将函数定义中的变量称为实参或将函数调用中的变量称为形参，不要大惊小怪。

## 8.2 传递实参

>   ​		鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同；也可使用关键字实参，其中每个实参都由变量名和值组成；还可使用列表和字典。

### 8.2.1 位置实参

>   ​		调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。
>
>   
>
>   示例：
>
>   ```python
>   # pets.py
>   def describe_pet(animal_type, pet_name):
>        """显示宠物的信息"""
>        print("\nI have a " + animal_type + ".")
>        print("My " + animal_type + "'s name is '" + pet_name.title() + ".")
>       
>   describe_pet('hamster', 'harry')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   I have a hamster.
>   My hamster's name is 'Harry.
>   ```

#### 1.调用函数多次

>   ​		你可以根据需要调用函数任意次。
>
>   ​		调用函数多次是一种效率极高的工作方式。
>
>   ​		在函数中，可根据需要使用任意数量的位置实参，Python将按顺序将函数调用中的实参关联到函数定义中相应的形参。
>
>   
>
>   示例：
>
>   ```python
>   def describe_pet(animal_type, pet_name):
>        """显示宠物的信息"""
>        print("\nI have a " + animal_type + ".")
>        print("My " + animal_type + "'s name is " + pet_name.title() + ".")
>       
>   describe_pet('hamster', 'harry')
>   describe_pet('dog', 'willie')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   I have a hamster.
>   My hamster's name is Harry.
>   
>   I have a dog.
>   My dog's name is Willie.
>   ```

#### 2.位置实参的顺序很重要

>   ​		使用位置实参来调用函数时，如果实参的顺序不正确，结果可能出乎意料。
>
>   
>
>   示例：
>
>   ```python
>   def describe_pet(animal_type, pet_name):
>        """显示宠物的信息"""
>        print("\nI have a " + animal_type + ".")
>        print("My " + animal_type + "'s name is " + pet_name.title() + ".")
>       
>   describe_pet('harry', 'hamster')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   I have a harry.
>   My harry's name is Hamster.
>   ```

### 8.2.2 关键字实参

>   ​		关键字实参是传递给函数的名称-值对。
>
>   ​		关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
>
>   ​		注意：使用关键字实参时，务必准确地指定函数定义中的形参名。
>
>   
>
>   示例：
>
>   ```python
>   def describe_pet(animal_type, pet_name):
>        """显示宠物的信息"""
>        print("\nI have a " + animal_type + ".")
>        print("My " + animal_type + "'s name is " + pet_name.title() + ".")
>       
>   describe_pet(animal_type='hamster', pet_name='harry')
>   ```
>
>   输出语句：
>
>   ```python
>   I have a hamster.
>   My hamster's name is Harry.
>   ```

### 8.2.3 默认值

>   ​		编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。
>
>   ​		注意：使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。这让Python依然能够正确地解读位置实参。
>
>   
>
>   示例：
>
>   ```python
>   def describe_pet(pet_name, animal_type='dog'):
>        """显示宠物的信息"""
>        print("\nI have a " + animal_type + ".")
>        print("My " + animal_type + "'s name is " + pet_name.title() + ".")
>       
>   describe_pet(pet_name='willie')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   I have a dog.
>   My dog's name is Willie.
>   ```

### 8.2.4 等效的函数调用

>   ​		鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。
>
>   ​		注意：使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行。使用对你来说最容易理解的调用方式即可。
>
>   
>
>   示例：
>
>   ```python
>   def describe_pet(pet_name, animal_type='dog'):
>        """显示宠物的信息"""
>        print("\nI have a " + animal_type + ".")
>        print("My " + animal_type + "'s name is " + pet_name.title() + ".")
>       
>   # 一条名为Willie的小狗
>   describe_pet('willie')
>   describe_pet(pet_name='willie')
>   
>   # 一只名为Harry的仓鼠
>   describe_pet('harry', 'hamster')
>   describe_pet(pet_name='harry', animal_type='hamster')
>   describe_pet(animal_type='hamster', pet_name='harry')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   I have a dog.
>   My dog's name is Willie.
>   
>   I have a dog.
>   My dog's name is Willie.
>   
>   I have a hamster.
>   My hamster's name is Harry.
>   
>   I have a hamster.
>   My hamster's name is Harry.
>   
>   I have a hamster.
>   My hamster's name is Harry.
>   ```

### 8.2.5 避免实参错误

>   ​		等你开始使用函数后，如果遇到实参不匹配错误，不要大惊小怪。你提供的实参多于或小于函数完成其工作所需的信息时，将出现实参不匹配错误。
>
>   ​		如果你给变量和函数指定描述性名称，那么无论对于你，还是可能使用你编写的代码的其他任何人来说，Python提供的错误信息都将更有帮助。
>
>   
>
>   示例：
>
>   ```python
>   def describe_pet(animal_type, pet_name):
>        """显示宠物的信息"""
>        print("\nI have a " + animal_type + ".")
>        print("My " + animal_type + "'s name is " + pet_name.title() + ".")
>       
>   describe_pet()
>   ```
>
>   输出语句：
>
>   ```python
>   Traceback (most recent call last):
>     # trackback指出了问题出在什么地方，让我们能够回过头去找出函数调用中的错误。
>     File "/Users/hanchen/Desktop/pythontest.py", line 6, in <module>
>       # 指出了导致问题的函数调用。
>       describe_pet()
>   # traceback指出该函数调用少两个实参，并指出了相应形参的名称。如果这个函数存储在一个独立的文件中，我们也许无需打开这个文件并查看函数的代码，就能重新正确地编写函数调用。
>   TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
>   ```

## 8.3 返回值

>   ​		函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值被称为返回值。
>
>   ​		在函数中，可使用return语句将值返回到调用函数的代码行。
>
>   ​		返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

### 8.3.1 返回简单值

>   示例：
>
>   ```python
>   # formatted_name.py
>   # 函数get_formatted_name()的定义通过形参接受名和姓。
>   def get_formatted_name(first_name, last_name):
>       """返回整洁的姓名"""
>       # 它将姓和名合二为一，在它们之间加上一个空格，并将结果存储在变量full_name中。
>       full_name = first_name + ' ' + last_name
>       # 然后，将full_name的值转换为首字母大写格式，并将结果返回到函数调用行。
>       return full_name.title()
>   
>   # 调用返回值的函数时，需要提供一个变量，用于存储返回的值。
>   musician = get_formatted_name('jimi', 'hendrix')
>   print(musician)
>   ```
>
>   输出语句：
>
>   ```python
>   Jimi Hendrix
>   ```

### 8.3.2 让实参变成可选的

>   ​		有时候，需要让实参变成可选的，这样使用函数的人就只需在必要时才提供额外的信息。可使用默认值来让实参变成可选的。
>
>   ​		可选值让函数能够处理各种不同情形的同时，确保函数调用尽可能简单。
>
>   
>
>   示例：
>
>   ```python
>   def get_formatted_name(first_name, last_name, middle_name=''):
>       """返回整洁的姓名"""
>       if middle_name:
>           full_name = first_name + ' ' + middle_name + ' ' + last_name
>       else:
>           full_name = first_name + ' ' + last_name
>       return full_name.title()
>       
>   musician = get_formatted_name('jimi', 'hendrix')
>   print(musician)
>   
>   musician = get_formatted_name('john', 'hooker', 'lee')
>   print(musician)
>   ```
>
>   输出语句：
>
>   ```python
>   Jimi Hendrix
>   John Lee Hooker
>   ```

### 8.3.3 返回字典

>   ​		函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。
>
>   
>
>   示例1：
>
>   ```python
>   # person.py
>   def build_person(first_name, last_name):
>       """返回一个字典，其中包含有关一个人的信息"""
>       person = {'first': first_name, 'last': last_name}
>       return person
>   
>   musician = build_person('jimi', 'hendrix')
>   print(musician)
>   ```
>
>   输出语句：
>
>   ```python
>   {'first': 'jimi', 'last': 'hendrix'}
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   def build_person(first_name, last_name, age=''):
>       """返回一个字典，其中包含有关一个人的信息"""
>       person = {'first': first_name, 'last': last_name} 
>       if age:
>           person['age'] = age
>       return person
>   
>   musician = build_person('jimi', 'hendrix', age=27)
>   print(musician)
>   ```
>
>   输出语句：
>
>   ```python
>   {'first': 'jimi', 'last': 'hendrix', 'age': 27}
>   ```

### 8.3.4 结合使用函数和 while 循环

>   示例：
>
>   ```python
>   # greeter.py
>   def get_formatted_name(first_name, last_name):
>       """返回整洁的姓名"""
>       full_name = first_name + ' ' + last_name
>       return full_name.title()
>   
>   # 这是一个无限循环！
>   while True:
>       print("\nPlease tell me your name:")
>       print("(enter 'q' at any time to quit)")
>       
>       f_name = input("First name: ")
>       if f_name == 'q':
>           break
>       
>       l_name = input("Last name: ")
>       if l_name == 'q':
>           break
>           
>       formatted_name = get_formatted_name(f_name, l_name)
>       print("\nHello, " + formatted_name + "!")
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Please tell me your name:
>   (enter 'q' at any time to quit)
>   First name: eric
>   Last name: matthes
>   
>   Hello, Eric Matthes!
>   
>   Please tell me your name:
>   (enter 'q' at any time to quit)
>   First name: q
>   ```

## 8.4 传递列表

>   ​		你经常会发现，向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（如字典）。将列表传递给函数后，函数就能直接访问其内容。
>
>   
>
>   示例：
>
>   ```python
>   # greet_users.py
>   def greet_users(names):
>       """向列表中的每位用户都发出简单的问候"""
>       for name in names:
>           msg = "Hello, " + name.title() + "!"
>           print(msg)
>       
>   usernames = ['hannah', 'ty', 'margot']
>   greet_users(usernames)
>   ```
>
>   输出语句：
>
>   ```python
>   Hello, Hannah!
>   Hello, Ty!
>   Hello, Margot!
>   ```

### 8.4.1 在函数中修改列表

>   ​		将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效地处理大量的数据。
>
>   ​		每个函数都应只负责一项具体的工作。
>
>   
>
>   示例1：
>
>   ```python
>   # printing_models.py
>   # 首先创建一个列表，其中包含一些要打印的设计
>   unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
>   completed_models = []
>   
>   # 模拟打印每个设计，直到没有未打印的设计为止
>   # 打印每个设计后，都将其移到列表completed_models中
>   while unprinted_designs:
>       current_design = unprinted_designs.pop()
>       
>       #模拟根据设计制作3D打印模型的过程
>       print("Printing model: " + current_design)
>       completed_models.append(current_design)
>       
>   # 显示打印好的所有模型
>   print("\nThe following models have been printed:")
>   for completed_model in completed_models:
>       print(completed_model)
>   ```
>
>   输出语句：
>
>   ```python
>   Printing model: dodecahedron
>   Printing model: robot pendant
>   Printing model: iphone case
>   
>   The following models have been printed:
>   dodecahedron
>   robot pendant
>   iphone case
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   def print_models(unprinted_designs, completed_models):
>       """
>       模拟打印每个设计，直到没有未打印的设计为止
>       打印每个设计后，都将其移到列表completed_models中
>       """
>       while unprinted_designs:
>           current_design = unprinted_designs.pop()
>           
>           # 模拟根据设计制作3D打印模型的过程
>           print("Printing model: " + current_design)
>           completed_models.append(current_design)
>           
>   def show_completed_models(completed_models):
>       """显示打印好的所有模型"""
>       print("\nThe following models have been printed:")
>       for completed_model in completed_models:
>           print(completed_model)
>           
>   unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
>   completed_models = []
>   
>   print_models(unprinted_designs, completed_models)
>   show_completed_models(completed_models)
>   ```
>
>   输出语句：
>
>   ```python
>   Printing model: dodecahedron
>   Printing model: robot pendant
>   Printing model: iphone case
>   
>   The following models have been printed:
>   dodecahedron
>   robot pendant
>   iphone case
>   ```

### 8.4.2 禁止函数修改列表

>   ​		有时候，需要禁止函数修改列表。
>
>   ​		为解决这个问题，可向函数传递列表的副本而不是原件；这样函数所做的任何修改都只影响副本，而丝毫不影响原件。
>
>   ​		切片表示法[:]创建列表的副本。
>
>   ​		虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，否则还是应该将原始列表传递给函数，因为让函数使用现成列表可避免花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此。
