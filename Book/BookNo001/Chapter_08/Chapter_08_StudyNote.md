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
>        """返回整洁的姓名"""
>        # 它将姓和名合二为一，在它们之间加上一个空格，并将结果存储在变量full_name中。
>        full_name = first_name + ' ' + last_name
>        # 然后，将full_name的值转换为首字母大写格式，并将结果返回到函数调用行。
>        return full_name.title()
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
>        """返回整洁的姓名"""
>        if middle_name:
>            full_name = first_name + ' ' + middle_name + ' ' + last_name
>        else:
>            full_name = first_name + ' ' + last_name
>        return full_name.title()
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
>        """返回一个字典，其中包含有关一个人的信息"""
>        person = {'first': first_name, 'last': last_name}
>        return person
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
>        """返回一个字典，其中包含有关一个人的信息"""
>        person = {'first': first_name, 'last': last_name} 
>        if age:
>            person['age'] = age
>        return person
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
>        """返回整洁的姓名"""
>        full_name = first_name + ' ' + last_name
>        return full_name.title()
>   
>   while True:
>       print("\nPlease tell me your name:")
>        print("(enter 'q' at any time to quit)")
>    
>           f_name = input("First name: ")
>        if f_name == 'q':
>            break
>    
>           l_name = input("Last name: ")
>        if l_name == 'q':
>            break
>    
>               formatted_name = get_formatted_name(f_name, l_name)
>        print("\nHello, " + formatted_name + "!")
>    ```
>   
>输出语句：
>   
>```python
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
>        """向列表中的每位用户都发出简单的问候"""
>        for name in names:
>            msg = "Hello, " + name.title() + "!"
>            print(msg)
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
>        current_design = unprinted_designs.pop()
>       
>        #模拟根据设计制作3D打印模型的过程
>        print("Printing model: " + current_design)
>        completed_models.append(current_design)
>       
>   # 显示打印好的所有模型
>   print("\nThe following models have been printed:")
>   for completed_model in completed_models:
>        print(completed_model)
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
>        """
>        模拟打印每个设计，直到没有未打印的设计为止
>        打印每个设计后，都将其移到列表completed_models中
>        """
>        while unprinted_designs:
>            current_design = unprinted_designs.pop()
>           
>            # 模拟根据设计制作3D打印模型的过程
>            print("Printing model: " + current_design)
>            completed_models.append(current_design)
>           
>   def show_completed_models(completed_models):
>        """显示打印好的所有模型"""
>        print("\nThe following models have been printed:")
>        for completed_model in completed_models:
>            print(completed_model)
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

## 8.5 传递任意数量的实参

>   ​		有时候，你预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任意数量的实参。
>
>   
>
>   示例1：
>
>   ```python
>   # pizza.py
>   def make_pizza(*toppings):
>       """打印顾客点的所有配料"""
>       print(toppings)
>       
>   make_pizza('pepperoni')
>   make_pizza('mushrooms', 'green peppers', 'extra cheese')
>   ```
>
>   输出语句：
>
>   ```python
>   ('pepperoni',)
>   ('mushrooms', 'green peppers', 'extra cheese')
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   def make_pizza(*toppings):
>       """概述要制作的比萨"""
>       print("\nMaking a pizza with the following toppings:")
>       for topping in toppings:
>           print("- " + topping)
>           
>   make_pizza('pepperoni')
>   make_pizza('mushrooms', 'green peppers', 'extra cheese')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Making a pizza with the following toppings:
>   - pepperoni
>   
>   Making a pizza with the following toppings:
>   - mushrooms
>   - green peppers
>   - extra cheese
>   ```

### 8.5.1 结合使用位置实参和任意数量实参

>   ​		如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
>
>   ​		Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
>
>   
>
>   示例：
>
>   ```python
>   def make_pizza(size, *toppings):
>       """概述要制作的比萨"""
>       print("\nMaking a " + str(size) +
>            "-inch pizza with the following toppings:")
>       for topping in toppings:
>           print("- " + topping)
>           
>   make_pizza(16, 'pepperoni')
>   make_pizza(12, 'mushrooms', 'green perrers', 'extra cheese')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Making a 16-inch pizza with the following toppings:
>   - pepperoni
>   
>   Making a 12-inch pizza with the following toppings:
>   - mushrooms
>   - green perrers
>   - extra cheese
>   ```

### 8.5.2 使用任意数量的关键字实参

>   ​		有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数量的键-值对—调用语句提供了多少就接受多少。
>
>   
>
>   示例：
>
>   ```python
>   # user_profile.py
>   def build_profile(first, last, **user_info):
>       """创建一个字典，其中包含我们知道的有关用户的一切"""
>       profile = {}
>       profile['first_name'] = first
>       profile['last_name'] = last
>       for key, value in user_info.items():
>           profile[key] = value
>       return profile
>   
>   user_profile = build_profile('albert', 'einstein',
>                               location='princeton',
>                               field='physics')
>   print(user_profile)
>   ```
>
>   输出语句：
>
>   ```python
>   {'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
>   ```

## 8.6 将函数存储在模块中

>   ​		函数的优点之一是，使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。你开可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。import语句允许在当前运行的程序文件中使用模块中的代码。
>
>   ​		通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。这还能让你在众多不同的程序中重用函数。将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。

### 8.6.1 导入整个模块

>   ​		要让函数是可导入的，得先创建模块。模块是扩展名为.py的文件，包含要导入到程序中的代码。
>
>   ​		这就是一种导入方法：只需编写一条import语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。如果你使用这种import语句导入了名为module_name.py的整个模块，就可使用下面的语法来使用其中任何一个函数：module_name.function_name()
>
>   
>
>   示例：
>
>   ```python
>   # pizza.py
>   def make_pizza(size, *toppings):
>       """概述要制作的比萨"""
>       print("\nMaking a " + str(size) +
>            "-inch pizza with the following toppings:")
>       for topping in toppings:
>           print("- " + topping)
>           
>   # making_pizzas.py
>   import pizza
>   
>   pizza.make_pizza(16, 'pepperoni')
>   pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Making a 16-inch pizza with the following toppings:
>   - pepperoni
>   
>   Making a 12-inch pizza with the following toppings:
>   - mushrooms
>   - green peppers
>   - extra cheese
>   ```

### 8.6.2 导入特定的函数

>   ​		导入模块中的特定函数，这种导入方法的语法如下：
>
>   ​				from module_name import function_name
>
>   ​		通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
>
>   ​				from module_name import function_0, function_1, function_2
>
>   ​		若使用这种语法，调用函数时就无需使用句点。
>
>   
>
>   示例：
>
>   ```python
>   # pizza.py
>   def make_pizza(size, *toppings):
>       """概述要制作的比萨"""
>       print("\nMaking a " + str(size) +
>            "-inch pizza with the following toppings:")
>       for topping in toppings:
>           print("- " + topping)
>           
>   # making_pizzas.py
>   from pizza import make_pizza
>   
>   make_pizza(16, 'pepperoni')
>   make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Making a 16-inch pizza with the following toppings:
>   - pepperoni
>   
>   Making a 12-inch pizza with the following toppings:
>   - mushrooms
>   - green peppers
>   - extra cheese
>   ```

### 8.6.3 使用 as 给函数指定别名

>   ​		如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名—函数的另一个名称，类似于外号。要给函数指定这种特殊外号，需要在导入它时这样做。
>
>   ​		指定别名的通用语法如下：
>
>   ​				from module_name import function_name as fn
>
>
>   示例：
>
>   ```python
>   # pizza.py
>   def make_pizza(size, *toppings):
>       """概述要制作的比萨"""
>       print("\nMaking a " + str(size) +
>            "-inch pizza with the following toppings:")
>       for topping in toppings:
>           print("- " + topping)
>           
>   # making_pizzas.py
>   from pizza import make_pizza as mp
>   
>   mp(16, 'pepperoni')
>   mp(12, 'mushrooms', 'green peppers', 'extra cheese')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Making a 16-inch pizza with the following toppings:
>   - pepperoni
>   
>   Making a 12-inch pizza with the following toppings:
>   - mushrooms
>   - green peppers
>   - extra cheese
>   ```

### 8.6.4 使用 as 给模块指定别名

>   ​		给模块指定别名的通用语法如下：
>
>   ​				import module_name as mn
>
>   
>
>   示例：
>
>   ```python
>   # pizza.py
>   def make_pizza(size, *toppings):
>       """概述要制作的比萨"""
>       print("\nMaking a " + str(size) +
>            "-inch pizza with the following toppings:")
>       for topping in toppings:
>           print("- " + topping)
>           
>   # making_pizzas.py
>   import pizza as p
>   
>   p.make_pizza(16, 'pepperoni')
>   p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Making a 16-inch pizza with the following toppings:
>   - pepperoni
>   
>   Making a 12-inch pizza with the following toppings:
>   - mushrooms
>   - green peppers
>   - extra cheese
>   ```

### 8.6.5 导入模块中的所有函数

>   ​		import语句中的星号让Python将模块中的每个函数都复制到这个程序文件中。由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法：如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。
>
>   ​		最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。
>
>   ​		导入模块中所有函数的通用语法如下：
>
>   ​				from module_name import *
>
>   
>
>   示例：
>
>   ```python
>   # pizza.py
>   def make_pizza(size, *toppings):
>       """概述要制作的比萨"""
>       print("\nMaking a " + str(size) +
>            "-inch pizza with the following toppings:")
>       for topping in toppings:
>           print("- " + topping)
>           
>   # making_pizzas.py
>   from pizza import *
>   
>   make_pizza(16, 'pepperoni')
>   make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Making a 16-inch pizza with the following toppings:
>   - pepperoni
>   
>   Making a 12-inch pizza with the following toppings:
>   - mushrooms
>   - green peppers
>   - extra cheese
>   ```

## 8.7 函数编写指南

>   ​		编写函数时，需要牢记几个细节。
>
>   ​		应给函数指定描述性名称，且只在其中使用小写字母和下划线。描述性名称可帮助你和别人明白代码想要做什么。给模块命名时也应遵循上述约定。
>
>   ​		每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。文档良好的函数让其他程序员只需阅读文档字符串中的描述就能够使用它：他们完全可以相信代码如描述的那样运行；只要知道函数的名称、需要的实参以及返回值的类型，就能在自己的程序中使用它。
>
>   ​		给形参指定默认值时，等号两边不要有空格：
>
>   ​				def function_name(parameter_0, parameter_1='default value')
>
>   ​		对于函数调用中的关键字实参，也应遵循这种约定：
>
>   ​				function_name(value_0, parameter_1='value')
>
>   ​		[PEP8](https://www.python.org/dev/peps/pep-0008/)建议代码行的长度不要超过79字符，这样只要编辑器窗口适中，就能看到整行代码。如果形参很多，导致函数定义的长度超过了79字符，可在函数定义中输入左括号后按回车键，并在下一行按两次Tab键，从而将形参列表和只缩进一层的函数体区分开来。
>
>   ​		大多数编辑器都会自动对齐后续参数列表行，使其缩进程度与你给第一个参数列表行指定的缩进程度相同。
>
>   ​				def function_name(
>
>   ​						parameter_0, parameter_1, parameter_2,
>
>   ​						parameter_3, parameter_4, parameter_5):
>
>   ​					function body...
>
>   ​		如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开，这样将更容易知道前一个函数在什么地方结束，下一个函数从什么地方开始。
>
>   ​		所有的import语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序。

## 8.8 小结

>   ​		在本章中，你学习了：如何编写函数，以及如何传递实参，让函数能够访问完成其工作所需的信息；如何使用位置实参和关键字实参，以及如何接受任意数量的实参；显示输出的函数和返回值的函数；如何将函数同列表、字典、if语句和while循环结合起来使用。你还知道了如何将函数存储在被称为模块的独立文件中，让程序文件更简单、更易于理解。最后，你学习了函数编写指南，遵循这些指南可让程序始终结构良好，并对你和其他人来说易于阅读。
>
>   ​		程序员的目标之一是，编写简单的代码来完成任务，而函数有助于你实现这样的目标。它们让你编写好代码块并确定其能够正确运行后，就可置之不理。确定函数能够正确地完成其工作后，你就可以接着投身于下一个编码任务。
>
>   ​		函数让你编写代码一次后，想重用它们多少次就重用多少次。需要运行函数中的代码时，只需编写一行函数调用代码，就可让函数完成其工作。需要修改函数的行为时，只需修改一个代码块，而所做的修改将影响调用这个函数的每个地方。
>
>   ​		使用函数让程序更容易阅读，而良好的函数名概述了程序各个部分的作用。相对于阅读一系列的代码块，阅读一系列函数调用让你能够更快地明白程序的作用。
>
>   ​		函数还让代码更容易测试和调试。如果程序使用一系列的函数来完成其任务，而其中的每个函数都完成一项具体的工作，测试和维护起来将容易得多：你可编写分别调用每个函数的程序，并测试每个函数是否在它可能遇到的各种情况下都能正确地运行。经过这样的测试后你就能信心满满，深信你每次调用这些函数时，它们都将正确地运行。

