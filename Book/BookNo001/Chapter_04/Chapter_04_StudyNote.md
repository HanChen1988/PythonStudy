# 第4章：操作列表

>   ​		在本章中，你将学习如何遍历整个列表，这只需要几行代码，无论列表有多长。循环让你能够对列表的每个元素都采取一个或一系列相同的措施，从而高效地处理任何长度的列表，包括包含数千乃至数百万个元素的列表。

## 4.1 遍历整个列表

>   ​		你经常需要遍历列表的所有元素，对每个元素执行相同的操作。
>
>   
>
>   示例：
>
>   ```python
>   # magicians.py
>   # 定义了一个列表
>   magicians = ['alice', 'david', 'carolina']
>   # 我们定义了一个for循环，这行代码让Python从列表magicians中取出一个名字，并将其存储在变量magician中。
>   for magician in magicians:
>   # 最后，我们让Python打印前面存储到变量magician中的名字。
>   	print(magician)
>   ```
>
>   输出语句：
>
>   ```python
>   alice
>   david
>   carolina
>   ```

### 4.1.1 深入地研究循环

>   ​		循环这种概念很重要，因为它是让计算机自动完成重复工作的常见方式之一。
>
>   ​		刚开始使用循环时请牢记，对列表中的每个元素，都将执行循环指定的步骤，而不管列表包含多少个元素。
>
>   ​		另外，编写for循环时，对于用于存储列表中每个值的临时变量，可指定任何名称。然而，选择描述单个列表元素的有意义的名称大有帮助。
>
>   ​		这些命名约定有助于你明白for循环中将对每个元素执行的操作。使用单数和复数式名称，可帮助你判断代码段处理的是单个列表还是整个列表。
>
>   
>
>   示例：
>
>   ```python
>   for cat in cats:
>   for dog in dogs:
>   for item in list_of_items:
>   ```

### 4.1.2 在for循环中执行更多的操作

>​		在for循环中，可对每个元素执行任何操作。
>
>​		在for循环中，想包含多少行代码都可以。每个缩进的代码行都是循环的一部分，且将针对列表中的每个值都执行一次。
>
>​		实际上，你会发现使用for循环对每个元素执行众多不同的操作很有用。
>
>
>
>示例1：
>
>```python
>magicians = ['alice', 'david', 'carolina']
>for magician in magicians:
>	print(magician.title() + ", that was a great trick!")
>```
>
>输出语句：
>
>```python
>Alice, that was a great trick!
>David, that was a great trick!
>Carolina, that was a great trick!
>```
>
>
>
>示例2：
>
>```python
>magicians = ['alice', 'david', 'carolina']
>for magician in magicians:
>	print(magician.title() + ", that was a great trick!")
>	# 第二条print语句中的换行符"\n"在每次迭代结束后都插入一个空行，从而整洁地将针对各位魔术师的消息编组：
>	print("I can't wait to see your next trick, " + magician.title() + ".\n")
>```
>
>输出语句：
>
>```python
>Alice, that was a great trick!
>I can't wait to see your next trick, Alice.
>
>David, that was a great trick!
>I can't wait to see your next trick, David.
>
>Carolina, that was a great trick!
>I can't wait to see your next trick, Carolina.
>```

### 4.1.3 在for循环结束后执行一些操作

>   ​		for循环结束后再怎么做呢？通常，你需要提供总结性输出或接着执行程序必须完成的其他任务。
>
>   ​		在for循环后面，没有缩进的代码都只执行一次，而不会重复执行。
>
>   ​		使用for循环处理数据是一种对数据集执行整体操作的不错的方式。
>
>   
>
>   示例：
>
>   ```python
>   magicians = ['alice', 'david', 'carolina']
>   for magician in magicians:
>   	print(magician.title() + ", that was a great trick!")
>   	print("I can't wait to see your next trick, " + magician.title() + ".\n")
>   
>   # 打印一条向全体魔术师致谢的消息，感谢他们的精彩表演。
>   print("Thank you, everyone. That was a great magic show!")
>   ```
>
>   输出语句：
>
>   ```python
>   Alice, that was a great trick!
>   I can't wait to see your next trick, Alice.
>   
>   David, that was a great trick!
>   I can't wait to see your next trick, David.
>   
>   Carolina, that was a great trick!
>   I can't wait to see your next trick, Carolina.
>   
>   Thank you, everyone. That was a great magic show!
>   ```

## 4.2 避免缩进错误

>   ​		Python根据缩进来判断代码行与前一行代码行的关系。
>
>   ​		Python通过使用缩进让代码更易读；简单地说，它要求你使用缩进让代码整洁而结构清晰。在较长的Python程序中，你将看到缩进程度各不相同的代码块，这让你对程序的组织结构有大致的认识。
>
>   ​		当你开始编写必须正确缩进的代码时，需要注意一些常见的缩进错误。例如，有时候，程序员会将不需要缩进的代码块缩进，而对于必须缩进的代码块却忘了缩进。通过查看这样的错误示例，有助于你以后避开它们，以及在它们出现在程序中时进行修复。
>
>   ​		下面来看一些较为常见的缩进错误。

### 4.2.1 忘记缩进

>   ​		对于位于for语句后面且属于循环组成部分的代码行，一定要缩进。如果你忘记缩进，Python会提醒你。
>
>   ​		通常，将紧跟在for语句后面的代码行缩进，可消除这种缩进错误。
>
>   
>
>   示例：
>
>   ```python
>   # magicians.py
>   magicians = ['alice', 'david', 'carolina']
>   for magician in magicians:
>   print(magician)
>   ```
>
>   输出语句：
>
>   ```python
>     File "/Users/hanchen/Desktop/pythontest.py", line 4
>       print(magician)
>           ^
>   IndentationError: expected an indented block
>   ```

### 4.2.2 忘记缩进额外的代码行

>   ​		有时候，循环能够运行而不会报告错误，但结果可能会出乎意料。试图在循环中执行多项任务，却忘记缩进其中的一些代码行时，就会出现这种情况。
>
>   ​		这是一个*逻辑错误*。从语法上看，这些Python代码是合法的，但由于存在逻辑错误，结果并不符合预期。如果你预期某项操作将针对每个列表元素都执行一次，但它却只执行了一次，请确定是否需要将一行或多行代码缩进。
>
>   
>
>   示例：
>
>   ```python
>   magicians = ['alice', 'david', 'carolina']
>   for magician in magicians:
>   	print(magician.title() + ", that was a great trick!")
>   # 第二条print语句原本需要缩进，但没有缩进。Python发现for语句后面有一行代码是缩进的，因此它没有报告错误。
>   print("I can't wait to see your next trick, " + magician.title() + ".\n")
>   ```
>
>   输出语句：
>
>   ```python
>   Alice, that was a great trick!
>   David, that was a great trick!
>   Carolina, that was a great trick!
>   I can't wait to see your next trick, Carolina.
>   ```

### 4.2.3 不必要的缩进

>   ​		如果你不小心缩进了无需缩进的代码行，Python将指出这一点。
>
>   ​		为避免意外缩进错误，请只缩进需要缩进的代码。
>
>   
>
>   示例：
>
>   ```python
>   # hello_world.py
>   message = "Hello Python world!"
>   	print(message)
>   ```
>
>   输出语句：
>
>   ```python
>     File "/Users/hanchen/Desktop/pythontest.py", line 2
>       print(message)
>       ^
>   IndentationError: unexpected indent
>   ```

### 4.2.4 循环后不必要的缩进

>   ​		如果你不小心缩进了应在循环结束后执行的代码，这些代码将针对每个列表元素重复执行。在有些情况下，这可能导致Python报告语法错误，但在大多数情况下，这只会导致逻辑错误。
>
>   ​		Python不知道你的本意，只要代码符合语法，它就会运行。如果原本只应执行一次的操作执行了多次，请确定你是否不应该缩进执行该操作的代码。
>
>   
>
>   示例：
>
>   ```python
>   magicians = ['alice', 'david', 'carolina']
>   for magician in magicians:
>   	print(magician.title() + ", that was a great trick!")
>   	print("I can't wait to see your next trick, " + magician.title() + ".\n")
>   	
>       print("Thank you everyone, that was a great magic show!")
>   ```
>
>   输出语句：
>
>   ```python
>   Alice, that was a great trick!
>   I can't wait to see your next trick, Alice.
>   
>   Thank you everyone, that was a great magic show!
>   David, that was a great trick!
>   I can't wait to see your next trick, David.
>   
>   Thank you everyone, that was a great magic show!
>   Carolina, that was a great trick!
>   I can't wait to see your next trick, Carolina.
>   
>   Thank you everyone, that was a great magic show!
>   ```

### 4.2.5 遗漏了冒号

>   ​		for语句末尾的冒号告诉Python,下一行是循环的第一行。
>
>   ​		如果你不小心遗漏了冒号，将导致语法错误，因为Python不知道你意欲何为。这种错误虽然易于消除，但并不那么容易发现。程序员为找出这样的单字符错误，花费的时间多得令人惊讶。这样的错误之所以难以发现，是因为通常在我们的意料之外。
>
>   
>
>   示例：
>
>   ```python
>   magicians = ['alice', 'david', 'carolina']
>   for magician in magicians
>   	print(magician)
>   ```
>
>   输出语句：
>
>   ```python
>     File "<stdin>", line 1
>       for magician in magicians
>                               ^
>   SyntaxError: invalid syntax
>   ```
