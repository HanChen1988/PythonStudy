# 第6章：字典

>   ​		在本章中，你将学习能够将相关信息关联起来的Python字典。你将学习如何访问和修改字典中的信息。鉴于字典可存储的信息量几乎不受限制，因此我们会演示如何遍历字典中的数据。另外，你还将学习存储字典的列表、存储列表的字典和存储字典的字典。
>
>   ​		理解字典后，你就能够更准确地为各种真实物体建模。

## 6.1 一个简单的字典

>   ​		与大多数编程概念一样，要熟练使用字典，也需要一段时间的练习。使用字典一段时间后，你就会明白为何它们能够高效地模拟现实世界中的情形。
>
>   
>
>   示例：
>
>   ```python
>   # alien.py
>   # 字典alien_0存储了外星人的颜色和点数。
>   alien_0 = {'color': 'green', 'points': 5}
>   
>   print(alien_0['color'])
>   print(alien_0['points'])
>   ```
>
>   输出语句：
>
>   ```python
>   green
>   5
>   ```

## 6.2 使用字典

>   ​		在Python中，字典是一系列键-值对，字典用放在花括号{}中的一系列键-值对表示。
>
>   ​		键-值对是两个相关联的值。指定键时，Python将返回与之相关联的值。
>
>   ​		键和值之间用冒号分隔，而键-值对之间用逗号分隔。
>
>   ​		在字典中，你想存储多少个键-值对都可以。最简单的字典只有一个键-值对。

### 6.2.1 访问字典中的值

>   ​		要获取与键相关联的值，可依次指定字典名和放在方括号内的键。
>
>   
>
>   示例1：
>
>   ```python
>   alien_0 = {'color': 'green'}
>   print(alien_0['color'])
>   ```
>
>   输出语句：
>
>   ```python
>   green
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   alien_0 = {'color': 'green', 'points': 5}
>   
>   # 从这个字典中获取与键'points'相关联的值，并将这个值存储在变量new_points中。
>   new_points = alien_0['points']
>   # 将这个整数转换为字符串，并打印一条消息，指出玩家获得了多少个点。
>   print("You just earned " + str(new_points) + " points!")
>   ```
>
>   输出语句：
>
>   ```python
>   You just earned 5 points!
>   ```

### 6.2.2 添加键-值对

>   ​		字典是一种动态结构，可随时在其中添加键-值对。要添加键-值对，可依次指定字典名、用方括号括起的键和相关联的值。
>
>   ​		注意，键-值对的排列顺序与添加顺序不同。Python不关心键-值对的添加顺序，而只关心键和值之间的关联关系。
>
>   
>
>   示例：
>
>   ```python
>   alien_0 = {'color': 'green', 'points': 5}
>   print(alien_0)
>   
>   # 在这个字典中新增了一个键-值对，其中的键为'x_position'，而值为0。
>   alien_0['x_position'] = 0
>   alien_0['y_position'] = 25
>   print(alien_0)
>   ```
>
>   输出语句：
>
>   ```python
>   {'color': 'green', 'points': 5}
>   {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
>   ```

### 6.2.3 先创建一个空字典

>   ​		有时候，在空字典中添加键-值对是为了方便，而有时候必须这样做。
>
>   ​		使用字典来存储用户提供的数据或在编写能自动生成大量键-值对的代码时，通常都需要先定义一个空字典。
>
>   
>
>   示例：
>
>   ```python
>   # 定义空字典alien_0
>   alien_0 = {}
>   
>   # 在其中添加颜色和点数
>   alien_0['color'] = 'green'
>   alien_0['points'] = 5
>   print(alien_0)
>   ```
>
>   输出语句：
>
>   ```python
>   {'color': 'green', 'points': 5}
>   ```

### 6.2.4 修改字典中的值

>   ​		要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。
>
>   
>
>   示例1：
>
>   ```python
>   alien_0 = {'color': 'green'}
>   print("The alien is " + alien_0['color'] + ".")
>   
>   alien_0['color'] = 'yellow'
>   print("The alien is now " + alien_0['color'] + ".") 
>   ```
>
>   输出语句：
>
>   ```python
>   The alien is green.
>   The alien is now yellow.
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
>   print("Original x-position: " + str(alien_0['x_position']))
>   
>   # 向右移动外星人
>   # 据外星人当前速度决定将其移动多远
>   if alien_0['speed'] == 'slow':
>       x_increment = 1
>   elif alien_0['speed'] == 'medium':
>       x_increment = 2
>   else:
>       # 这个外星人的速度一定很快
>       x_increment = 3
>   
>   # 新位置等于老位置加上增量
>   alien_0['x_position'] = alien_0['x_position'] + x_increment
>   print("New x-position: " + str(alien_0['x_position']))
>   ```
>
>   输出语句：
>
>   ```python
>   Original x-position: 0
>   New x-position: 2
>   ```

### 6.2.5 删除键-值对

>   ​		对于字典中不再需要的信息，可使用del语句将相应的键-值对彻底删除。使用del语句时，必须指定字典名和要删除的键。
>
>   ​		注意：删除的键-值对永远消失了。
>
>   
>
>   示例：
>
>   ```python
>   alien_0 = {'color': 'green', 'points': 5}
>   print(alien_0)
>   
>   del alien_0['points']
>   print(alien_0)
>   ```
>
>   输出语句：
>
>   ```python
>   {'color': 'green', 'points': 5}
>   {'color': 'green'}
>   ```

