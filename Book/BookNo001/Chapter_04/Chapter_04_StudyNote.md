# 第4章：操作列表

>   ​		在本章中，你将学习如何遍历整个列表，这只需要几行代码，无论列表有多长。循环让你能够对列表的每个元素都采取一个或一系列相同的措施，从而高效地处理任何长度的列表，包括包含数千乃至数百万个元素的列表。

## 4.1 遍历整个列表

>   ​		你经常需要遍历列表的所有元素，对每个元素执行相同的操作。
>
>   ​		示例：
>
>   ​				magicians.py
>
>   ​				\# 定义了一个列表
>
>   ​				magicians = ['alice', 'david', 'carolina']
>
>   ​				\# 我们定义了一个for循环，这行代码让Python从列表magicians中取出一个名字，并将其存储在变量magician中。
>
>   ​				for magician in magicians:
>
>   ​				\# 最后，我们让Python打印前面存储到变量magician中的名字。
>
>   ​					print(magician)
>
>   ​				输出语句：
>   ​				alice
>
>   ​				david
>
>   ​				carolina

### 4.1.1 深入地研究循环

>   ​		循环这种概念很重要，因为它是让计算机自动完成重复工作的常见方式之一。
>
>   ​		刚开始使用循环时请牢记，对列表中的每个元素，都将执行循环指定的步骤，而不管列表包含多少个元素。
>
>   ​		另外，编写for循环时，对于用于存储列表中每个值的临时变量，可指定任何名称。然而，选择描述单个列表元素的有意义的名称大有帮助。
>
>   ​		这些命名约定有助于你明白for循环中将对每个元素执行的操作。使用单数和复数式名称，可帮助你判断代码段处理的是单个列表还是整个列表。
>
>   ​		示例：
>
>   ​				for cat in cats:
>
>   ​				for dog in dogs:
>
>   ​				for item in list_of_items:

### 4.1.2 在for循环中执行更多的操作

>​		在for循环中，可对每个元素执行任何操作。
>
>​		在for循环中，想包含多少行代码都可以。每个缩进的代码行都是循环的一部分，且将针对列表中的每个值都执行一次。
>
>​		实际上，你会发现使用for循环对每个元素执行众多不同的操作很有用。
>
>​		示例1：
>
>​				magicians = ['alice', 'david', 'carolina']
>
>​				for magician in magicians:
>
>​					print(magician.title() + ", that was a great trick!")
>
>​				输出语句：
>
>​				Alice, that was a great trick!
>
>​				David, that was a great trick!
>
>​				Carolina, that was a great trick!
>
>​		示例2：
>
>​				magicians = ['alice', 'david', 'carolina']
>
>​				for magician in magicians:
>
>​					print(magician.title() + ", that was a great trick!")
>
>​					\# 第二条print语句中的换行符"\n"在每次迭代结束后都插入一个空行，从而整洁地将针对各位魔术师的消息编组：
>
>​					print("I can't wait to see your next trick, " + magician.title() + ".\n")
>
>​				输出语句：
>
>​				Alice, that was a great trick!
>
>​				I can't wait to see your next trick, Alice.
>
>
>
>​				David, that was a great trick!
>
>​				I can't wait to see your next trick, David.
>
>
>
>​				Carolina, that was a great trick!
>
>​				I can't wait to see your next trick, Carolina.

### 4.1.3 在for循环结束后执行一些操作

>   ​		for循环结束后再怎么做呢？通常，你需要提供总结性输出或接着执行程序必须完成的其他任务。
>
>   ​		在for循环后面，没有缩进的代码都只执行一次，而不会重复执行。
>
>   ​		使用for循环处理数据是一种对数据集执行整体操作的不错的方式。
>
>   ​		示例：
>
>   ​				magicians = ['alice', 'david', 'carolina']
>
>   ​				for magician in magicians:
>
>   ​					print(magician.title() + ", that was a great trick!")
>
>   ​					print("I can't wait to see your next trick, " + magician.title() + ".\n")
>
>   ​				\# 打印一条向全体魔术师致谢的消息，感谢他们的精彩表演。
>
>   ​				print("Thank you, everyone. That was a great magic show!")
>
>   ​				输出语句：
>
>   ​				Alice, that was a great trick!
>
>   ​				I can't wait to see your next trick, Alice.
>
>   
>
>   ​				David, that was a great trick!
>
>   ​				I can't wait to see your next trick, David.
>
>   
>
>   ​				Carolina, that was a great trick!
>
>   ​				I can't wait to see your next trick, Carolina.
>
>   
>
>   ​				Thank you, everyone. That was a great magic show!					

## 4.2 避免缩进错误

