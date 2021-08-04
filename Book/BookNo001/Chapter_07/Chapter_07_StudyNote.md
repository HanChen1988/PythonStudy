# 第7章：用户输入和 while 循环

>   ​		大多数程序都旨在解决最终用户的问题，为此通常需要从用户那里获取一些信息。
>
>   ​		在本章中，你将学习如何接受用户输入，让程序能够对其进行处理。在程序需要一个名字时，你需要提示用户输入该名字；程序需要一个名单时，你需要提示用户输入一系列名字。为此，你需要使用函数input()。
>
>   ​		你还将学习如何让程序不断地运行，让用户能够根据需要输入信息，并在程序中使用这些信息。为此，你需要使用while循环让程序不断地运行，直到指定的条件不满足为止。
>
>   ​		通过获取用户输入并学会控制程序的运行时间，可编写出交互式程序。

## 7.1 函数 input()的工作原理

>   ​		函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。
>
>   ​		函数input()接受一个参数：即要向用户显示的提示或说明，让用户知道该如何做。程序等待用户输入，并在用户按回车键后继续运行。
>
>   ​		注意：Sublime Text不能运行提示用户输入的程序。
>
>   
>
>   示例：
>
>   ```python
>   # parrot.py
>   message = input("Tell me something, and I will repeat it back to you: ")
>   print(message)
>   ```
>
>   输出语句：
>
>   ```python
>   Tell me something, and I will repeat it back to you: Hello everyone!
>   Hello everyone!
>   ```

### 7.1.1 编写清晰的程序

>   ​		每当你使用函数input()时，都应指定清晰而易于明白的提示，准确地指出你希望用户提供什么样的信息。
>
>   ​		通过在提示末尾包含一个空格，可将提示与用户输入分开，让用户清楚地知道其输入始于何处。
>
>   ​		有时候，提示可能超过一行。在这种情况下，可将提示存储在一个变量中，再将该变量传递给函数input()。这样，即便提示超过一行，input()语句也非常清晰。
>
>   ​		运算符+=可在字符串末尾附加一个字符串。
>
>   
>
>   示例1：
>
>   ```python
>   # greeter.py
>   name = input("Please enter your name: ")
>   print("Hello, " + name + "!")
>   ```
>
>   输出语句：
>
>   ```python
>   Please enter your name: Eric
>   Hello, Eric!
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # greeter.py
>   prompt = "If you tell us who you are, we can personalize the message you see."
>   prompt += "\nWhat is your first name? "
>   
>   name = input(prompt)
>   print("\nHello, " + name + "!")
>   ```
>
>   输出语句：
>
>   ```python
>   If you tell us who you are, we can personalize the message you see.
>   What is your first name? Eric
>   
>   Hello, Eric!
>   ```

### 7.1.2 使用 int()来获取数值输入

>   ​		使用函数input()时，Python将用户输入解读为字符串。
>
>   ​		将数值输入用于计算和比较前，务必将其转换为数值表示。
>
>   ​		可使用函数int()，它让Python将输入视为数值。
>
>   
>
>   示例1：
>
>   ```python
>   age = input("How old are you? ")
>   print(age)
>   ```
>
>   输出语句：
>
>   ```python
>   How old are you? 21
>   21
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   age = input("How old are you? ")
>   print(age >= 18)
>   ```
>
>   输出语句：
>
>   ```python
>   How old are you? 21
>   Traceback (most recent call last):
>     File "/Users/hanchen/Desktop/pythontest.py", line 2, in <module>
>       print(age >= 18)
>   TypeError: '>=' not supported between instances of 'str' and 'int'
>   ```
>
>   
>
>   示例3：
>
>   ```python
>   age = input("How old are you? ")
>   age = int(age)
>   print(age >= 18)
>   ```
>
>   输出语句：
>
>   ```python
>   How old are you? 21
>   True
>   ```
>
>   
>
>   示例4：
>
>   ```python
>   # rollercoaster.py
>   height = input("How tall are you, in inches? ")
>   height = int(height)
>   
>   if height >= 36:
>        print("\nYou're tall enough to ride!")
>   else:
>        print("\nYou'll be able to ride when you're a little older.")
>   ```
>
>   输出语句：
>
>   ```python
>   How tall are you, in inches? 71
>   
>   You're tall enough to ride!
>   ```

### 7.1.3 求模运算符

>   ​		处理数值信息时，求模运算符（%）是一个很有用的工具，它将两个数相除并返回余数。
>
>   ​		如果一个数可被另一个数整除，余数就为0，因此求模运算符将返回0。
>
>   
>
>   示例1：
>
>   ```python
>   print(4 % 3)
>   print(5 % 3)
>   print(6 % 3)
>   print(7 % 3)
>   ```
>
>   输出语句：
>
>   ```python
>   1
>   2
>   0
>   1
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # even_or_odd.py
>   number = input("Enter a number, and I'll tell you if it's even or odd: ")
>   number = int(number)
>   
>   if number % 2 == 0:
>        print("\nThe number " + str(number) + " is even.")
>   else:
>        print("\nThe number " + str(number) + " is odd.")
>   ```
>
>   输出语句：
>
>   ```python
>   Enter a number, and I'll tell you if it's even or odd: 42
>   
>   The number 42 is even.
>   ```

### 7.1.4 在 Python 2.7 中获取输入

>   ​		如果你使用的是Python 2.7，应使用函数raw_input()来提示用户输入。这个函数与Python 3中的input()一样，也将输入解读为字符串。
>
>   ​		Python 2.7也包含函数input(),但它将用户输入解读为Python代码，并尝试运行它们。因此，最好的结果是出现错误，指出Python不明白输入的代码；而最糟的结果是，将运行你原本无意运行的代码。如果你使用的是Python 2.7，请使用raw_input()而不是input()来获取输入。

## 7.2 while 循环简介

>   ​		for循环用于针对集合中的每个元素的一个代码块，而while循环不断地运行，直到指定的条件不满足为止。

### 7.2.1 使用 while 循环

>   示例：
>
>   ```python
>   # counting.py
>   current_number = 1
>   while current_number <= 5:
>        print(current_number)
>        current_number += 1
>   ```
>
>   输出语句：
>
>   ```python
>   1
>   2
>   3
>   4
>   5
>   ```

### 7.2.2 让用户选择何时退出

>   ​		可使用while循环让程序在用户愿意时不断地运行。我们在其中定义了一个退出值，只要用户输入的不是这个值，程序就接着运行。
>
>   
>
>   示例1：
>
>   ```python
>   # parrot.py
>   prompt = "\nTell me something, and I will repeat it back to you:"
>   prompt += "\nEnter 'quit' to end the program. "
>   message = ""
>   while message != 'quit':
>        message = input(prompt)
>        print(message)
>   ```
>
>   输出语句：
>
>   ```python
>   Tell me something, and I will repeat it back to you:
>   Enter 'quit' to end the program. Hello everyone!
>   Hello everyone!
>   
>   Tell me something, and I will repeat it back to you:
>   Enter 'quit' to end the program. Hello again.
>   Hello again.
>   
>   Tell me something, and I will repeat it back to you:
>   Enter 'quit' to end the program. quit
>   quit
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # parrot.py
>   prompt = "\nTell me something, and I will repeat it back to you:"
>   prompt += "\nEnter 'quit' to end the program. "
>   message = ""
>   while message != 'quit':
>        message = input(prompt)
>       
>        if message != 'quit':
>       	print(message)
>   ```
>
>   输出语句：
>
>   ```python
>   Tell me something, and I will repeat it back to you:
>   Enter 'quit' to end the program. Hello everyone!
>   Hello everyone!
>   
>   Tell me something, and I will repeat it back to you:
>   Enter 'quit' to end the program. Hello again.
>   Hello again.
>   
>   Tell me something, and I will repeat it back to you:
>   Enter 'quit' to end the program. quit
>   ```

### 7.2.3 使用标志

>   ​		在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。这个变量被称为标志，充当了程序的交通信号灯。你可让程序在标志为True时继续运行，并在任何事件导致标志的值为False时让程序停止运行。这样，在while语句中就只需检查一个条件—标志的当前值是否为True，并将所有测试（是否发生了应将标志设置为False的事件）都放在其他地方，从而让程序变得更为整洁。
>
>   
>
>   示例：
>
>   ```python
>   prompt = "\nTell me something, and I will repeat it back to you:"
>   prompt += "\nEnter 'quit' to end the program. "
>   
>   active = True
>   while active:
>        message = input(prompt)
>       
>        if message == 'quit':
>            active = False
>        else:
>            print(message)
>   ```
>
>   输出语句：
>
>   ```python
>   Tell me something, and I will repeat it back to you:
>   Enter 'quit' to end the program. Hello everyone!
>   Hello everyone!
>   
>   Tell me something, and I will repeat it back to you:
>   Enter 'quit' to end the program. Hello again.
>   Hello again.
>   
>   Tell me something, and I will repeat it back to you:
>   Enter 'quit' to end the program. quit
>   ```

### 7.2.4 使用 break 退出循环

>   ​		要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break语句。
>
>   ​		break语句用于控制程序流程，可使用它来控制哪些代码行将执行，哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。
>
>   ​		注意：在任何Python循环中都可使用break语句。
>
>   
>
>   示例：
>
>   ```python
>   # cities.py
>   prompt = "\nPlease enter the name of a city you have visited:"
>   prompt += "\n(Enter 'quit' when you are finished.) "
>   
>   while True:
>        city = input(prompt)
>       
>        if city == 'quit':
>            break
>        else:
>            print("I'd love to go to " + city.title() + "!")
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Please enter the name of a city you have visited:
>   (Enter 'quit' when you are finished.) New York
>   I'd love to go to New York!
>   
>   Please enter the name of a city you have visited:
>   (Enter 'quit' when you are finished.) San Francisco
>   I'd love to go to San Francisco!
>   
>   Please enter the name of a city you have visited:
>   (Enter 'quit' when you are finished.) quit
>   ```

### 7.2.5 在循环中使用 continue

>   ​		要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句，它不像break语句那样不再执行余下的代码并退出整个循环。
>
>   ​		
>
>   示例：
>
>   ```python
>   # counting.py
>   current_number = 0
>   while current_number < 10:
>       current_number += 1
>       if current_number % 2 == 0:
>           continue
>       
>       print(current_number)
>   ```
>
>   输出语句：
>
>   ```python
>   1
>   3
>   5
>   7
>   9
>   ```

### 7.2.6 避免无限循环

>   ​		每个while循环都必须有停止运行的途径，这样才不会没完没了地执行下去。
>
>   ​		每个程序员都会偶尔因不小心而编写出无限循环，在循环的退出条件比较微妙时尤其如此。如果程序陷入无限循环，可按Ctrl+C，也可关闭显示程序输出的终端窗口。
>
>   ​		要避免编写无限循环，务必对每个while循环进行测试，确保它按预期那样结束。如果你希望程序在用户输入特定值时结束，可运行程序并输入这样的值；如果在这种情况下程序没有结束，请检查程序处理这个值的方式，确认程序至少有一个这样的地方能让循环条件为False或让break语句得以执行。
>
>   ​		注意：有些编辑器（如Sublime Text）内嵌了输出窗口，这可能导致难以结束无限循环，因此不得不关闭编辑器来结束无限循环。
>
>   
>
>   示例1：
>
>   ```python
>   # counting.py
>   x = 1
>   while x <= 5:
>       print(x)
>       x += 1
>   ```
>
>   输出语句：
>
>   ```python
>   1
>   2
>   3
>   4
>   5
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # 这个循环将没完没了地运行！
>   x = 1
>   while x <= 5:
>       print(x)
>   ```
>
>   输出语句：
>
>   ```python
>   1
>   1
>   1
>   1
>   --snip--
>   ```

