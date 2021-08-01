# 第3章：列表简介

>   ​		在本章和下一章中，你将学习列表是什么以及如何使用列表元素。列表让你能够在一个地方存储成组的信息，其中可以只包含几个元素，也可以包含数百万个元素。列表是新手可直接使用的最强大的Python功能之一，它融合了众多重要的编程概念。

## 3.1 列表是什么

>   ​		列表由一系列按特定顺序排列的元素组成。
>
>   ​		鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如：letters、digits或names）是个不错的主意。
>
>   ​		在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。
>
>   
>
>   示例：
>
>   ```python
>   # bicycles.py
>   bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>   # 如果你让Python将列表打印出来，Python将打印列表的内部表示，包括方括号。
>   print(bicycles)
>   ```
>
>   输出语句：
>
>   ```python
>   ['trek', 'cannondale', 'redline', 'specialized']
>   ```

### 3.1.1 访问列表元素

>   ​		列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可。
>
>   ​		要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内。
>
>   
>
>   示例1：
>
>   ```python
>   bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>   # 当你请求获取列表元素时，Python只返回该元素，而不包括方括号和引号。
>   print(bicycles[0])
>   ```
>
>   输出语句：
>
>   ```python
>   trek
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>   # 可使用方法title()让元素'trek'的格式更整洁
>   print(bicycles[0].title())
>   ```
>
>   输出语句：
>
>   ```python
>   Trek
>   ```

### 3.1.2 索引从0而不是1开始

>   ​		在Python中，第一个列表元素的索引为0，而不是1。在大多数编程语言中都是如此，这与列表操作的底层实现相关。
>
>   ​		Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让Python返回最后一个列表元素。
>
>   ​		这种约定也适用于其他负数索引，例如，索引-2返回倒数第二个列表元素，索引-3返回倒数第三个列表元素，以此类推。		
>
>   
>
>   示例1：
>
>   ```python
>   bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>   # 返回列表中的第二个和第四个元素
>   print(bicycles[1])
>   print(bicycles[3])
>   ```
>
>   输出语句：
>
>   ```python
>   cannondale
>   specialized
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>   # 返回列表最后一个元素
>   print(bicycles[-1])
>   ```
>
>   输出语句：
>
>   ```python
>   specialized
>   ```

### 3.1.3 使用列表中的各个值

>   ​		可像使用其他变量一样使用列表中的各个值。
>
>   
>
>   示例：
>
>   ```python
>   bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>   message = "My first bicycle was a " + bicycles[0].title() + "."
>   
>   print(message)
>   ```
>
>   输出语句：
>
>   ```python
>   My first bicycle was a Trek.
>   ```

## 3.2 修改、添加和删除元素

>   ​		你创建的大多数列表都将是动态的，这意味着列表创建后，将随着程序的运行增删元素。

### 3.2.1 修改列表元素

>   ​		修改列表元素的语法与访问列表元素的语法类似。
>
>   ​		要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
>
>   
>
>   示例：
>
>   ```python
>   # motorcycles.py
>   motorcycles = ['honda', 'yamaha', 'suzuki']
>   print(motorcycles)
>   
>   motorcycles[0] = 'ducati'
>   # 输出表明，第一个元素的值确实变了，但其他列表元素的值没变。
>   print(motorcycles)
>   ```
>
>   输出语句：
>
>   ```python
>   ['honda', 'yamaha', 'suzuki']
>   ['ducati', 'yamaha', 'suzuki']
>   ```

### 3.2.2 在列表中添加元素

>   ​		Python提供了多种在既有列表中添加新数据的方式。

#### 1.在列表末尾添加元素

>   ​		在列表中添加新元素时，最简单的方式是将元素附加到列表末尾。
>
>   ​		方法append()让动态地创建列表易如反掌。
>
>   ​		为控制用户，可首先创建一个空列表，用于存储用户将要输入的值，然后将用户提供的每个新值附加到列表中。这种创建列表的方式及其常见，因为经常要等程序运行后，你才知道用户要在程序中存储哪些数据。
>
>   
>
>   示例1：
>
>   ```python
>   motorcycles = ['honda', 'yamaha', 'suzuki']
>   print(motorcycles)
>   
>   # 方法append()将元素'ducati'添加到了列表末尾，而不影响列表中的其他所有元素。
>   motorcycles.append('ducati')
>   print(motorcycles)
>   ```
>
>   输出语句：
>
>   ```python
>   ['honda', 'yamaha', 'suzuki']
>   ['honda', 'yamaha', 'suzuki', 'ducati']
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   motorcycles = []
>   
>   motorcycles.append('honda')
>   motorcycles.append('yamaha')
>   motorcycles.append('suzuki')
>   
>   print(motorcycles)
>   ```
>
>   输出语句：
>
>   ```python
>   ['honda', 'yamaha', 'suzuki']
>   ```

#### 2.在列表中插入元素

>   ​		使用方法insert()可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。
>
>   
>
>   示例：
>
>   ```python
>   motorcycles = ['honda', 'yamaha', 'suzuki']
>   
>   # 方法insert()在索引0处添加空间，并将值'ducati'存储到这个地方。这种操作将列表中既有的每个元素都右移一个位置。
>   motorcycles.insert(0, 'ducati')
>   print(motorcycles)
>   ```
>
>   输出语句：
>
>   ```python
>   ['ducati', 'honda', 'yamaha', 'suzuki']
>   ```

### 3.2.3 从列表中删除元素

>   ​		你经常需要从列表中删除一个或多个元素。

#### 1.使用del语句删除元素

>   ​		如果知道要删除的元素在列表中的位置，可使用del语句。
>
>   ​		使用del语句将值从列表中删除后，你就无法再访问它了。
>
>   
>
>   示例：
>
>   ```python
>   motorcycles = ['honda', 'yamaha', 'suzuki']
>   print(motorcycles)
>   
>   # 使用del删除了列表motorcycles中第一个元素—'honda'
>   del motorcycles[0]
>   print(motorcycles)
>   ```
>
>   输出语句：
>
>   ```python
>   ['honda', 'yamaha', 'suzuki']
>   ['yamaha', 'suzuki']
>   ```

#### 2.使用方法pop()删除元素

>   ​		方法pop()可删除列表末尾的元素，并让你能够接着使用它。术语弹出（pop）源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
>
>   
>
>   示例1：
>
>   ```python
>   # 定义并打印列表motorcycles
>   motorcycles = ['honda', 'yamaha', 'suzuki']
>   print(motorcycles)
>   
>   # 我们从这个列表中弹出一个值，并将其存储到变量popped_motorcycle中。
>   popped_motorcycle = motorcycles.pop()
>   # 我们打印这个列表，以核实从其中删除了一个值。
>   print(motorcycles)
>   # 我们打印弹出的值，以证明我们依然能够访问被删除的值。
>   print(popped_motorcycle)
>   ```
>
>   输出语句：
>
>   ```python
>   ['honda', 'yamaha', 'suzuki']
>   ['honda', 'yamaha']
>   suzuki
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   motorcycles = ['honda', 'yamaha', 'suzuki']
>   
>   last_owned = motorcycles.pop()
>   # 输出是一个简单的句子，指出了最新购买的是那款摩托车
>   print("The last motorcycles I owned was a " + last_owned.title() + ".")
>   ```
>
>   输出语句：
>
>   ```python
>   The last motorcycles I owned was a Suzuki.
>   ```

#### 3.弹出列表中任何位置处的元素

>   ​		实际上，你可以使用pop()来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。
>
>   ​		别忘了，每当你使用pop()时，被弹出的元素就不再列表中了。
>
>   ​		**使用del语句还是pop方法，有一个简单的判断标准：如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续使用它，就使用方法pop()。**
>
>   
>
>   示例：
>
>   ```python
>   motorcycles = ['honda', 'yamaha', 'suzuki']
>   
>   # 我们弹出了列表中的第一款摩托车
>   first_owned = motorcycles.pop(0)
>   # 然后打印了一条有关这辆摩托车的消息。输出是一个简单的句子，描述了我购买的第一辆摩托车。
>   print('The first motorcycle I owned was a ' + first_owned.title() + '.')
>   ```
>
>   输出语句：
>
>   ```python
>   The first motorcycle I owned was a Honda.
>   ```

#### 4.根据值删除元素

>   ​		有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法remove()。
>
>   ​		**注意：方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。**
>
>   
>
>   示例1：
>
>   ```python
>   motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
>   print(motorcycles)
>   
>   # 让Python确定‘ducati'出现在列表的什么地方，并将该元素删除
>   motorcycles.remove('ducati')
>   print(motorcycles)
>   ```
>
>   输出语句：
>
>   ```python
>   ['honda', 'yamaha', 'suzuki', 'ducati']
>   ['honda', 'yamaha', 'suzuki']
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # 定义列表
>   motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
>   print(motorcycles)
>   
>   # 将值'ducati'存储在变量too_expensive中。
>   too_expensive = 'ducati'
>   # 我们使用这个变量来告诉Python将哪个值从列表中删除
>   motorcycles.remove(too_expensive)
>   print(motorcycles)
>   # 最'ducati'已经从列表中删除，但它还存储在变量too_expensive中，让我们能够打印一条消息，指出将'ducati'从列表motorcycles中删除的原因
>   print("\nA " + too_expensive.title() + " is too expensive for me.")
>   ```
>
>   输出语句：
>
>   ```python
>   ['honda', 'yamaha', 'suzuki', 'ducati']
>   ['honda', 'yamaha', 'suzuki']
>   
>   A Ducati is too expensive for me.
>   ```

## 3.3 组织列表

>   ​		在你创建的列表中，元素的排列顺序常常是无法预测的，因为你并非总能控制用户提供数据的顺序。这虽然在大多数情况下都是不可避免的，但你经常需要以特定的顺序呈现信息。有时候，你希望保留列表元素最初的排列顺序，而有时候又需要调整排列顺序。Python提供了很多组织列表的方式，可根据具体情况选用。

### 3.3.1 使用方法sort()对列表进行永久性排序

>   ​		方法sort()永久性地修改了列表元素的排列顺序。
>
>   ​		还可以按与字母顺序相反的顺序排列列表元素，为此，只需向sort()方法传递参数reverse=True。
>
>   
>
>   示例1：
>
>   ```python
>   # cars.py
>   cars = ['bmw', 'audi', 'toyota', 'subaru']
>   cars.sort()
>   print(cars)
>   ```
>
>   输出语句：
>
>   ```python
>   ['audi', 'bmw', 'subaru', 'toyota']
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   cars = ['bmw', 'audi', 'toyota', 'subaru']
>   cars.sort(reverse=True)
>   print(cars)
>   ```
>
>   输出语句：
>
>   ```python
>   ['toyota', 'subaru', 'bmw', 'audi']
>   ```

### 3.3.2 使用函数sorted()对列表进行临时排序

>   ​		要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数sorted()。
>
>   ​		函数sorted()让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。
>
>   ​		如果你要按与字母顺序相反的顺序显示列表，也可向函数sorted()传递参数reverse=True。
>
>   ​		**注意：并非所有的值都是小写时，按字母顺序排列列表要复杂些。决定排列顺序时，有多种解读大写字母的方式，要指定准确的排列顺序，可能比我们这里所做的要复杂。然而，大多数排序方式都基于本节介绍的知识。**
>
>   
>
>   示例：
>
>   ```python
>   cars = ['bmw', 'audi', 'toyota', 'subaru']
>   
>   # 首先按原始顺序打印列表
>   print("Here is the original list:")
>   print(cars)
>   
>   # 再按字母顺序显示该列表
>   print("\nHere is the sorted list:")
>   print(sorted(cars))
>   
>   # 以特定顺序显示列表后，我们进行核实，确认列表元素的排列顺序与以前相同
>   print("\nHere is the original list again:")
>   print(cars)
>   ```
>
>   输出语句：
>
>   ```python
>   Here is the original list:
>   ['bmw', 'audi', 'toyota', 'subaru']
>   
>   Here is the sorted list:
>   ['audi', 'bmw', 'subaru', 'toyota']
>   
>   Here is the original list again:
>   ['bmw', 'audi', 'toyota', 'subaru']
>   ```

### 3.3.3 倒着打印列表

>   ​		要反转列表元素的排列顺序，可使用方法reverse()。
>
>   ​		**注意，reverse()不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序。方法reverse()永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用reverse()即可。**
>
>   
>
>   示例：
>
>   ```python
>   cars = ['bmw', 'audi', 'toyota', 'subaru']
>   print(cars)
>   
>   cars.reverse()
>   print(cars)
>   ```
>
>   输出语句：
>
>   ```python
>   ['bmw', 'audi', 'toyota', 'subaru']
>   ['subaru', 'toyota', 'audi', 'bmw']
>   ```

### 3.3.4 确定列表的长度

>   ​		使用函数len()可快速获悉列表的长度。
>
>   ​		**注意：Python计算列表元素数时从1开始，因此确定列表长度时，你应该不会遇到差一错误。**	
>
>   
>
>   示例：
>
>   ```python
>   cars = ['bmw', 'audi', 'toyota', 'subaru']
>   print(len(cars))
>   ```
>
>   输出语句：
>
>   ```python
>   4
>   ```

## 3.4 使用列表时避免索引错误

>   ​		索引错误意味着Python无法理解你指定的索引。程序发生索引错误时，请尝试将你指定的索引减1，然后再次运行程序，看看结果是否正确。
>
>   ​		别忘了，每当需要访问最后一个列表元素时，都可使用索引-1。
>
>   ​		仅当列表为空时，这种访问最后一个元素的方式才会导致错误。
>
>   ​		**注意：发送索引错误却找不到解决办法时，请尝试将列表或其长度打印出来。列表可能与你以为的截然不同，在程序对其进行了动态处理时尤其如此。通过查看列表或其包含的元素数，可帮助你找出这种逻辑错误。**
>
>   
>
>   示例1：
>
>   ```python
>   motorcycles = ['honda', 'yamaha', 'suzuki']
>   print(motorcycles[3])
>   ```
>
>   输出语句：
>
>   ```python
>   Traceback (most recent call last):
>     File "/Users/hanchen/Desktop/pythontest.py", line 2, in <module>
>       print(motorcycles[3])
>   IndexError: list index out of range
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   motorcycles = ['honda', 'yamaha', 'suzuki']
>   print(motorcycles[-1])
>   ```
>
>   输出语句：
>
>   ```python
>   suzuki
>   ```
>
>   
>
>   示例3：
>
>   ```python
>   motorcycles = []
>   # 列表motorcycles不包含任何元素，因此Python返回一条索引错误消息
>   print(motorcycles[-1])
>   ```
>
>   输出语句：
>
>   ```python
>   Traceback (most recent call last):
>     File "/Users/hanchen/Desktop/pythontest.py", line 3, in <module>
>       print(motorcycles[-1])
>   IndexError: list index out of range
>   ```

## 3.5 小结

>   ​		在本章中，你学习了：列表是什么以及如何使用其中的元素；如何定义列表以及如何增删元素；如何对列表进行永久性排序，以及如何为展示列表而进行临时排序；如何确定列表的长度，以及在使用列表时如何避免索引错误。

