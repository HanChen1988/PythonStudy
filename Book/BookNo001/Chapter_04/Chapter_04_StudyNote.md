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
>        print("Thank you everyone, that was a great magic show!")
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

## 4.3 创建数字列表

>​		列表非常适合用于存储数字集合，而Python提供了很多工具，可帮助你高效地处理数字列表。明白如何有效地使用这些工具后，即便列表包含数百万个元素，你编写的代码也能运行得很好。

### 4.3.1 使用函数 range()

>​		Python函数range()让你能够轻松地生成一系列的数字。
>
>​		使用range()时，如果输出不符合预期，请尝试将指定的值加1或减1。
>
>
>
>示例1：
>
>```python
># numbers.py
>for value in range(1,5):
>    # range()只是打印数字1~4，这是你在编程语言中经常看到的差一行为的结果。函数range()让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值。
>    print(value)
>```
>
>输出语句：
>
>```python
>1
>2
>3
>4
>```
>
>
>
>示例2：
>
>```python
>for value in range(1,6):
>    print(value)
>```
>
>输出语句：
>
>```python
>1
>2
>3
>4
>5
>```

### 4.3.2 使用range()创建数字列表

>   ​		要创建数字列表，可使用函数list()将range()的结果直接转换为列表。如果将range()作为list()的参数，输出将为一个数字列表。
>
>   ​		使用函数range()时，还可指定步长。
>
>   ​		使用函数range()几乎能够创建任何需要的数字集。
>
>   ​		有时候，使用临时变量会让代码更易读；而在其他情况下，这样做只会让代码无谓地变长。你首先应该考虑的是，编写清晰易懂且能完成所需功能的代码；等到审核代码时，再考虑采用更高效的方法。
>
>   
>
>   示例1：
>
>   ```python
>   numbers = list(range(1,6))
>   print(numbers)
>   ```
>
>   输出语句：
>
>   ```python
>   [1, 2, 3, 4, 5]
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # even_numbers.py
>   even_numbers = list(range(2,11,2))
>   print(even_numbers)
>   ```
>
>   输出语句：
>
>   ```python
>   [2, 4, 6, 8, 10]
>   ```
>
>   
>
>   示例3：
>
>   ```python
>   # squares.py
>   # 创建了一个空列表
>   squares = []
>   # 使用函数range()让Python遍历1~10的值
>   for value in range(1,11):
>       # 在循环中，计算当前值的平方，并将结果存储到变量square中。在Python中，两个星号（**）表示乘方运算。
>       square = value**2
>       # 将新计算得到的平方值附加到列表squares末尾。
>       squares.append(square)
>   # 循环结束后，打印列表squares
>   print(squares)
>   ```
>
>   输出语句：
>
>   ```python
>   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>   ```
>
>   
>
>   示例4：
>
>   ```python
>   squares = []
>   for value in range(1,11):
>       # 在循环中，计算每个值的平方，并立即将结果附加到列表squares的末尾。
>       squares.append(value**2)
>   
>   print(squares)
>   ```
>
>   输出语句：
>
>   ```python
>   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>   ```

### 4.3.3 对数字列表执行简单的统计计算

>   ​		**注意：出于版面考虑，本节使用的数字列表都很短，但这里介绍的知识也适用于包含数百万个数字的列表。**
>
>   
>
>   示例：
>
>   ```python
>   digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>   # 取最小值
>   print(min(digits))
>   # 取最大值
>   print(max(digits))
>   # 求和
>   print(sum(digits))
>   ```
>
>   输出语句：
>
>   ```python
>   0
>   9
>   45
>   ```

### 4.3.4 列表解析

>​		列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。
>
>​		要使用这种语法，首先指定一个描述性的列表名；然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。请注意，这里的for语句末尾没有冒号。	
>
>​		要创建自己的列表解析，需要经过一定的练习，但能够熟练地创建常规列表后，你会发现这样做是完全值得的。当你觉得编写三四行代码来生成列表有点繁复时，就应考虑创建列表解析了。
>
>
>
>示例1：
>
>```python
># squares.py
>squares = [value**2 for value in range(1,11)]
>print(squares)
>```
>
>输出语句：
>
>```python
>[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>```

## 4.4 使用列表的一部分

>   ​		可以处理列表的部分元素—Python称之为切片。

### 4.4.1 切片

>   ​		要创建切片，可指定要使用的第一个元素的索引和最后一个元素的索引加1。与函数range()一样，Python在到达你指定的第二个索引前面的元素后停止。
>
>   ​		你可以生成列表的任何子集。
>
>   ​		如果你没有指定第一个索引，Python将自动从列表开头开始，要让切片终止于列表末尾，也可使用类似的语法。
>
>   ​		负数索引返回离列表末尾相应距离的元素，因此你可以输出列表末尾的任何切片。
>
>   
>
>   示例1：
>
>   ```python
>   # players.py
>   players = ['charles', 'martina', 'michael', 'florence', 'eli']
>   # 输出也是一个列表，其中包含前三名队员。
>   print(players[0:3])
>   ```
>
>   输出语句：
>
>   ```python
>   ['charles', 'martina', 'michael']
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   players = ['charles', 'martina', 'michael', 'florence', 'eli']
>   # 提取列表的第2~4个元素，可将起始索引指定为1，并将终止索引指定为4
>   print(players[1:4])
>   ```
>
>   输出语句：
>
>   ```python
>   ['martina', 'michael', 'florence']
>   ```
>
>   
>
>   示例3：
>
>   ```python
>   players = ['charles', 'martina', 'michael', 'florence', 'eli']
>   # 由于没有指定起始索引，Python从列表开头开始提取
>   print(players[:4])
>   ```
>
>   输出语句：
>
>   ```python
>   ['charles', 'martina', 'michael', 'florence']
>   ```
>
>   
>
>   示例4：
>
>   ```python
>   players = ['charles', 'martina', 'michael', 'florence', 'eli']
>   # 提取从第3个元素到列表末尾的所有元素，可将起始索引指定为2，并省略终止索引
>   print(players[2:])
>   ```
>
>   输出语句：
>
>   ```python
>   ['michael', 'florence', 'eli']
>   ```
>
>   
>
>   示例5：
>
>   ```python
>   players = ['charles', 'martina', 'michael', 'florence', 'eli']
>   # 打印名单上的最后三名队员
>   print(players[-3:])
>   ```
>
>   输出语句：
>
>   ```python
>   ['michael', 'florence', 'eli']
>   ```

### 4.4.2 遍历切片

>   ​		如果要遍历列表的部分元素，可在for循环中使用切片。
>
>   
>
>   示例1：
>
>   ```python
>   players = ['charles', 'martina', 'michael', 'florence', 'eli']
>   
>   print("Here are the first three players on my team:")
>   for player in players[:3]:
>        print(player.title())
>   ```
>
>   输出语句：
>
>   ```python
>   Here are the first three players on my team:
>   Charles
>   Martina
>   Michael
>   ```

### 4.4.3 复制列表

>   ​		你经常需要根据既有列表创建全新的列表。
>
>   ​		要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。
>
>   ​		**注意：当你试图使用列表的副本时，如果结果出乎意料，请确认你使用切片复制了列表。**
>
>   
>
>   示例1：
>
>   ```python
>   # foods.py
>   # 创建一个名为my_foods的食品列表
>   my_foods = ['pizza', 'falafel', 'carrot cake']
>   # 创建一个名为friend_foods的新列表
>   friend_foods = my_foods[:]
>   
>   print("My favorite foods are:")
>   print(my_foods)
>   
>   print("\nMy friend's favorite foods are:")
>   print(friend_foods)
>   ```
>
>   输出语句：
>
>   ```python
>   My favorite foods are:
>   ['pizza', 'falafel', 'carrot cake']
>   
>   My friend's favorite foods are:
>   ['pizza', 'falafel', 'carrot cake']
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # foods.py
>   my_foods = ['pizza', 'falafel', 'carrot cake']
>   friend_foods = my_foods[:]
>   
>   # 在列表my_foods中添加'cannoli'
>   my_foods.append('cannoli')
>   # 在friend_foods中添加'ice cream'
>   friend_foods.append('ice cream')
>   
>   print("My favorite foods are:")
>   print(my_foods)
>   
>   print("\nMy friend's favorite foods are:")
>   print(friend_foods)
>   ```
>
>   输出语句：
>
>   ```python
>   My favorite foods are:
>   ['pizza', 'falafel', 'carrot cake', 'cannoli']
>   
>   My friend's favorite foods are:
>   ['pizza', 'falafel', 'carrot cake', 'ice cream']
>   ```
>
>   
>
>   示例3：
>
>   ```python
>   # foods.py
>   my_foods = ['pizza', 'falafel', 'carrot cake']
>   
>   # 这行不通，这里将my_foods赋给friend_foods，而不是将my_foods的副本存储到friend_foods。因此这两个变量都指向同一个列表。
>   friend_foods = my_foods
>   
>   my_foods.append('cannoli')
>   friend_foods.append('ice cream')
>   
>   print("My favorite foods are:")
>   print(my_foods)
>   
>   print("\nMy friend's favorite foods are:")
>   print(friend_foods)
>   ```
>
>   输出语句：
>
>   ```python
>   My favorite foods are:
>   ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
>   
>   My friend's favorite foods are:
>   ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
>   ```

## 4.5 元组

>   ​		列表非常适合用于存储在程序运行期间可能变化的数据集。然而，有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。
>
>   ​		相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组。
>
>   ​		Python将不能修改的值称为不可变的，而不可变的列表称为元组。

### 4.5.1 定义元组

>   ​		元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
>
>   
>
>   示例1：
>
>   ```python
>   # dimensions.py
>   # 定义了元组dimensions，为此我们使用了圆括号。
>   dimensions = (200, 50)
>   # 分别打印该元组的各个元素
>   print(dimensions[0])
>   print(dimensions[1])
>   ```
>
>   输出语句：
>
>   ```python
>   200
>   50
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   dimensions = (200, 50)
>   # 试图修改第一个元素的值，导致Python返回类型错误信息。
>   dimensions[0] = 250
>   ```
>
>   输出语句：
>
>   ```python
>   Traceback (most recent call last):
>     File "/Users/hanchen/Desktop/pythontest.py", line 2, in <module>
>       dimensions[0] = 250
>   TypeError: 'tuple' object does not support item assignment
>   ```

### 4.5.2 遍历元组中的所有值

>​		使用for循环来遍历元组中的所有值。
>
>
>
>示例：
>
>```python
>dimensions = (200, 50)
>for dimension in dimensions:
>    print(dimension)
>```
>
>输出语句：
>
>```python
>200
>50
>```

### 4.5.3 修改元组变量

>​		虽然不能修改元组的元素，但可以给存储元组的变量赋值。
>
>​		
>
>示例：
>
>```python
># 将一个元组存储到变量dimensions中
>dimensions = (200, 50)
>print("Original dimensions:")
>for dimension in dimensions:
>    print(dimension)
># 将一个新元组存储到变量dimensions中  
>dimensions = (400, 100)
>print("\nModified dimensions:")
>for dimension in dimensions:
>    print(dimension)
>```
>
>输出语句：
>
>```python
>Original dimensions:
>200
>50
>
>Modified dimensions:
>400
>100
>```

## 4.6 设置代码格式

>   ​		随着你编写的程序越来越长，有必要了解一些代码格式设置约定。请花时间让你的代码尽可能易于阅读；让代码易于阅读有助于你掌握程序是做什么的，也可以帮助他人理解你编写的代码。
>
>   ​		为确保所有人编写的代码的结构都大致一致，Python程序员都遵循一些格式设置约定。学会编写整洁的Python后，就能明白他人编写的Python代码的整体结构—只要他们和你遵循相同的指南。要成为专业程序员，应从现在开始就遵循这些指南，以养成良好的习惯。

### 4.6.1 格式设置指南

>​		PEP 8是最古老的PEP之一，它向Python程序员提供了代码格式设置指南。PEP8的篇幅很长，但大都与复杂的编码结构相关。
>
>​		Python格式设置指南的编写者深知，代码被阅读的次数比编写的次数多。代码编写出来后，调试时你需要阅读它；给程序添加新功能时，需要花很长的时间阅读代码；与其他程序员分享代码时，这些程序员也将阅读它们。
>
>​		如果一定要在让代码易于编写和易于阅读之间做出选择，Python程序员几乎总是会选择后者。

### 4.6.2 缩进

>   ​		PEP8建议每级缩进都使用四个空格，这既可提高可读性，又留下了足够的多级缩进空间。
>
>   ​		在字处理文档中，大家常常使用制表符而不是空格来缩进。对于字处理文档来说，这样做的效果很好，但混合使用制表符和空格会让Python解释器感到迷惑。每款文本编辑器都提供了一种设置，可将输入的制表符转换为指定数量的空格。你在编写代码时应该使用制表符键，但一定要对编辑器进行设置，使其在文档中插入空格而不是制表符。
>
>   ​		在程序中混合使用制表符和空格可能导致极难解决的问题。如果你混合使用了制表符和空格，可将文件中所有的制表符转换为空格，大多数编辑器都提供了这样的功能。

### 4.6.3 行长

>   ​		很多Python程序员都建议每行不超过80字符。
>
>   ​		在大多数计算机中，终端窗口每行只能容纳79字符。
>
>   ​		PEP 8还建议注释的行长都不超过72字符。
>
>   ​		PEP 8中有关行长的指南并非不可逾越的红线，有些小组将最大行长设置为99字符。但协作编写程序时，大家几乎都遵守PEP 8指南。
>
>   ​		在大多数编辑器中，都可设置一个视觉标志—通常是一条竖线，让你知道不能越过的界线在什么地方。

### 4.6.4 空格

>   ​		要将程序的不同部分分开，可使用空行。你应该使用空行来组织程序文件，但也不能滥用；只要按照示例展示的那样做，就能掌握其中的平衡。
>
>   ​		空行不会影响代码的运行，但会影响代码的可读性。Python解释器根据水平缩进情况来解读代码，但不关心垂直间距。

### 4.6.5 其他格式设置指南

>   ​		PEP 8还有很多其他的格式设置建议，但这些指南针对的程序大都比目前为止本书提到的程序复杂。

## 4.7 小结

>   ​		在本章中，你学习了：如何高效地处理列表中的元素；如何使用for循环遍历列表，Python如何根据缩进来确定程序的结构以及如何避免一些常见的缩进错误；如何创建简单的数字列表，以及可对数字列表执行的一些操作；如何通过切片来使用列表的一部分和复制列表。你还学习了元组（它对不应变化的值提供了一定程度的保护），以及在代码变得越来越复杂时如何设置格式，使其易于阅读。

