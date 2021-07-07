# 第3章：列表简介

>   ​		在本章和下一章中，你将学习列表是什么以及如何使用列表元素。列表让你能够在一个地方存储成组的信息，其中可以只包含几个元素，也可以包含数百万个元素。列表是新手可直接使用的最强大的Python功能之一，它融合了众多重要的编程概念。

## 3.1 列表是什么

>   ​		列表由一系列按特定顺序排列的元素组成。
>
>   ​		鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如：letters、digits或names）是个不错的主意。
>
>   ​		在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。
>
>   ​		示例：
>
>   ​				bicycles.py
>
>   ​				bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>
>   ​				print(bicycles)
>
>   ​				如果你让Python将列表打印出来，Python将打印列表的内部表示，包括方括号：
>
>   ​				['trek','cannondale','redline','specialized']

### 3.1.1 访问列表元素

>   ​		列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可。
>
>   ​		要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内。
>
>   ​		示例：
>
>   ​				bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>
>   ​				print(bicycles[0])
>
>   ​				当你请求获取列表元素时，Python只返回该元素，而不包括方括号和引号：
>
>   ​				trek
>
>   ​				可使用方法title()让元素'trek'的格式更整洁：
>
>   ​				bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>
>   ​				print(bicycles[0].title())
>
>   ​				Trek

### 3.1.2 索引从0而不是1开始

>   ​		在Python中，第一个列表元素的索引为0，而不是1。在大多数编程语言中都是如此，这与列表操作的底层实现相关。
>
>   ​		示例：
>
>   ​				bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>
>   ​				print(bicycles[1])
>
>   ​				print(bicycles[3])
>
>   ​				返回列表中的第二个和第四个元素：
>
>   ​				cannondale
>
>   ​				specialized
>
>   ​		Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让Python返回最后一个列表元素：
>
>   ​		示例：
>
>   ​				bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>
>   ​				print(bicycles[-1])
>
>   ​				返回列表最后一个元素：
>
>   ​				specialized
>
>   ​		这种约定也适用于其他负数索引，例如，索引-2返回倒数第二个列表元素，索引-3返回倒数第三个列表元素，以此类推。

### 3.1.3 使用列表中的各个值

>   ​		可像使用其他变量一样使用列表中的各个值。
>
>   ​		示例：
>
>   ​				bicycles = ['trek', 'cannondale', 'redline', 'specialized']
>
>   ​				message = "My first bicycle was a " + bicycles[0].title() + "."
>
>   ​				print(message)
>
>   ​				输出
>
>   ​				My first bicycle was a Trek.

## 3.2 修改、添加和删除元素

>   ​		你创建的大多数列表都将是动态的，这意味着列表创建后，将随着程序的运行增删元素。

### 3.2.1 修改列表元素

>   ​		修改列表元素的语法与访问列表元素的语法类似。
>
>   ​		要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
>
>   ​		示例：
>   ​				motorcycles.py
>
>   ​				motorcycles = ['honda', 'yamaha', 'suzuki']
>   ​				print(motorcycles)
>
>   
>
>   ​				motorcycles[0] = 'ducati'
>
>   ​				print(motorcycles)
>
>   ​				输出表明，第一个元素的值确实变了，但其他列表元素的值没变。
>
>   ​				['honda', 'yamaha', 'suzuki']
>
>   ​				['ducati', 'yamaha', 'suzuki']
>
>   ​		你可以修改任何列表元素的值，而不仅仅是第一个元素的值。

### 3.2.2 在列表中添加元素

>   ​		Python提供了多种在既有列表中添加新数据的方式。

#### 1.在列表末尾添加元素

>   ​		在列表中添加新元素时，最简单的方式是将元素附加到列表末尾。
>
>   ​		示例1：
>
>   ​				motorcycles = ['honda', 'yamaha', 'suzuki']
>
>   ​				print(motorcycles)
>
>   ​				motorcycles.append('ducati')
>
>   ​				
>
>   ​				motorcycles.append('ducati')
>
>   ​				print(motorcycles)
>
>   ​				方法append()将元素'ducati'添加到了列表末尾，而不影响列表中的其他所有元素。
>
>   ​				['honda', 'yamaha', 'suzuki']
>
>   ​				['honha', 'yamaha', 'suzuki', 'ducati']
>
>   ​		方法append()让动态地创建列表易如反掌。
>
>   ​		为控制用户，可首先创建一个空列表，用于存储用户将要输入的值，然后将用户提供的每个新值附加到列表中。这种创建列表的方式及其常见，因为经常要等程序运行后，你才知道用户要在程序中存储哪些数据。
>
>   ​		示例2：
>
>   ​				motorcycles = []
>
>   
>
>   ​				motorcycles.append('honda')
>
>   ​				motorcycles.append('yamaha')
>
>   ​				motorcycles.append('suzuki')
>
>   
>
>   ​				print(motorcycles)
>
>   ​				最终的列表与前述示例中的列表完全相同：
>
>   ​				['honda', 'yamaha', 'suzuki']

#### 2.在列表中插入元素

>   ​		使用方法insert()可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。
>
>   ​		示例：
>
>   ​				motorcycles = ['honda', 'yamaha', 'suzuki']
>
>   ​				
>
>   ​				motorcycles.insert(0, 'ducati')
>
>   ​				print(motorcycles)
>
>   ​				方法insert()在索引0处添加空间，并将值'ducati'存储到这个地方。这种操作将列表中既有的每个元素都右移一个位置：
>
>   ​				['ducati', 'honda', 'yamaha', 'suzuki']

### 3.2.3 从列表中删除元素

>   ​		你经常需要从列表中删除一个或多个元素。

#### 1.使用del语句删除元素

>   ​		如果知道要删除的元素在列表中的位置，可使用del语句。
>
>   ​		使用del语句将值从列表中删除后，你就无法再访问它了。
>
>   ​		示例：
>
>   ​				motorcycles = ['honda', 'yamaha', 'suzuki']
>
>   ​				print(motorcycles)
>
>   
>
>   ​				del motorcycles[0]
>
>   ​				print(motorcycles)
>
>   ​				使用del删除了列表motorcycles中第一个元素—'honda':
>
>   ​				['honda', 'yamaha', 'suzuki']
>
>   ​				['yamaha', 'suzuki']

#### 2.使用方法pop()删除元素



​	







