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
>        x_increment = 1
>   elif alien_0['speed'] == 'medium':
>        x_increment = 2
>   else:
>        # 这个外星人的速度一定很快
>        x_increment = 3
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

### 6.2.5 由类似对象组成的字典

>   ​		我们将一个较大的字典放在了多行中。
>
>   ​		确定需要使用多行来定义字典时，在输入左花括号后按回车键，再在下一行缩进四个空格，指定第一个键-值对，并在它后面加上一个逗号。此后你再次按回车键时，文本编辑器将自动缩进后续键-值对，且缩进量与第一个键-值对相同。
>
>   ​		定义好字典后，在最后一个键-值对的下一行添加一个右花括号，并缩进四个空格，使其与字典中的键对齐。
>
>   ​		另外一种不错的做法是在最后一个键-值对后面也加上逗号，为以后在下一行添加键-值对做好准备。
>
>   ​		注意：对于较长的列表和字典，大多数编辑器都有以类似方式设置其格式的功能。对于较长的字典，还有其他一些可行的格式设置方式，因此在你的编辑器或其他源代码中，你可能会看到稍微不同的格式设置方式。
>
>   ​		
>
>   ​		我们将一个较长的print语句分成多行。
>
>   ​		请选择在合适的地方拆分要打印的内容，并在第一行末尾加上一个拼接运算符（+）。按回车键进入print语句的后续各行，并使用Tab键将它们对齐并缩进一级。指定要打印的所有内容后，在print语句的最后一行末尾加上右括号。
>
>   
>
>   示例：
>
>   ```python
>   # favorite_languages.py
>   favorite_languages = {
>       'jen': 'python',
>       'sarah': 'c',
>       'edward': 'ruby',
>       'phil': 'python',
>   }
>   
>   print("Sarah's favorite language is " +
>   	favorite_languages['sarah'].title() +
>   	".")
>   ```
>
>   输出语句：
>
>   ```python
>   Sarah's favorite language is C.
>   ```

## 6.3 遍历字典

>   ​		一个Python字典可能只包含几个键-值对，也可能包含数百万个键-值对。鉴于字典可能包含大量的数据，Python支持对字典遍历。字典可用于以各种方式存储信息，因此有多种遍历字典的方式：可遍历字典的所有键-值对、键或值。

### 6.3.1 遍历所有的键-值对

>   ​		注意：即便遍历字典时，键-值对的返回顺序也与存储顺序不同。Python不关心键-值对的存储顺序，而只跟踪键和值之间的关联关系。
>
>   
>
>   示例1：
>
>   ```python
>   # user.py
>   user_0 = {
>       'username': 'efermi',
>       'first': 'enrico',
>       'last': 'fermi',
>   }
>   
>   for key, value in user_0.items():
>   	print("\nKey:" + key)
>        print("Value:" + value)
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Key:username
>   Value:efermi
>   
>   Key:first
>   Value:enrico
>   
>   Key:last
>   Value:fermi
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # favorite_languages.py
>   favorite_languages = {
>       'jen': 'python',
>       'sarah': 'c',
>       'edward': 'ruby',
>       'phil': 'python',
>   }
>   
>   for name, language in favorite_languages.items():
>    	print(name.title() + "'s favorite language is " +
>        	language.title() +
>            ".")
>   ```
>
>   输出语句：
>
>   ```python
>   Jen's favorite language is Python.
>   Sarah's favorite language is C.
>   Edward's favorite language is Ruby.
>   Phil's favorite language is Python.
>   ```

### 6.3.2 遍历字典中的所有键

>   ​		在不需要使用字典中的值时，方法keys()很有用。
>
>   ​		遍历字典时，会默认遍历所有的键。
>
>   ​		如果显示地使用方法keys()可让代码更容易理解，你可以选择这样做，但如果你愿意，也可省略它。
>
>   ​		方法keys()并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键。
>
>   
>
>   示例1：
>
>   ```python
>   favorite_languages = {
>       'jen': 'python',
>       'sarah': 'c',
>       'edward': 'ruby',
>       'phil': 'python',
>   }
>   
>   for name in favorite_languages.keys():
>    	print(name.title())
>   ```
>
>   输出语句：
>
>   ```python
>   Jen
>   Sarah
>   Edward
>   Phil
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   favorite_languages = {
>       'jen': 'python',
>       'sarah': 'c',
>       'edward': 'ruby',
>       'phil': 'python',
>   }
>   
>   friends = ['phil', 'sarah']
>   for name in favorite_languages.keys():
>        print(name.title())
>       
>        if name in friends:
>            print(" Hi " + name.title() +
>            	", I see your favorite_language is " +
>                favorite_languages[name].title() + "!")
>   ```
>
>   输出语句：
>
>   ```python
>   Jen
>   Sarah
>    Hi Sarah, I see your favorite_language is C!
>   Edward
>   Phil
>    Hi Phil, I see your favorite_language is Python!
>   ```
>
>   
>
>   示例3：
>
>   ```python
>   favorite_languages = {
>       'jen': 'python',
>       'sarah': 'c',
>       'edward': 'ruby',
>       'phil': 'python',
>   }
>   
>   if 'erin' not in favorite_languages.keys():
>        print("Erin, please take our poll!")
>   ```
>
>   输出语句：
>
>   ```python
>   Erin, please take our poll!
>   ```

### 6.3.3 按顺序遍历字典中的所有键

>   ​		字典总是明确地记录键和值之间的关联关系，但获取字典的元素时，获取顺序是不可预测的。这不是问题，因为通常你想要的只是获取与键相关联的正确的值。
>
>   ​		要以特定的顺序返回元素，一种办法是在for循环中对返回的键进行排序。为此，可使用函数sorted()来获得按特定顺序排列的键列表的副本。
>
>   
>
>   示例：
>
>   ```python
>   favorite_languages = {
>       'jen': 'python',
>       'sarah': 'c',
>       'edward': 'ruby',
>       'phil': 'python',
>   }
>   
>   for name in sorted(favorite_languages.keys()):
>        print(name.title() + ", thank you for taking the poll.")
>   ```
>
>   输出语句：
>
>   ```python
>   Edward, thank you for taking the poll.
>   Jen, thank you for taking the poll.
>   Phil, thank you for taking the poll.
>   Sarah, thank you for taking the poll.
>   ```

### 6.3.4 遍历字典中的所有值

>   ​		如果你感兴趣的主要是字典包含的值，可使用方法values()，它返回一个值列表，而不包含任何键。
>
>   ​		这种做法提取字典中所有的值，而没有考虑是否重复。
>
>   ​		为剔除重复项，可使用集合（set）。集合类似于列表，但每个元素都必须是独一无二的。
>
>   
>
>   示例1：
>
>   ```python
>   favorite_languages = {
>       'jen': 'python',
>       'sarah': 'c',
>       'edward': 'ruby',
>       'phil': 'python',
>   }
>   
>   print("The following languages have been mentioned:")
>   for language in favorite_languages.values():
>        print(language.title())
>   ```
>
>   输出语句：
>
>   ```python
>   The following languages have been mentioned:
>   Python
>   C
>   Ruby
>   Python
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   favorite_languages = {
>       'jen': 'python',
>       'sarah': 'c',
>       'edward': 'ruby',
>       'phil': 'python',
>   }
>   
>   print("The following languages have been mentioned:")
>   for language in set(favorite_languages.values()):
>        print(language.title())
>   ```
>
>   输出语句：
>
>   ```python
>   The following languages have been mentioned:
>   Python
>   Ruby
>   C
>   ```

## 6.4 嵌套

>   ​		有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。
>
>   ​		你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。

### 6.4.1 字典列表

>示例1：
>
>```python
># aliens.py
>alien_0 = {'color': 'green', 'points': 5}
>alien_1 = {'color': 'yellow', 'points': 10}
>alien_2 = {'color': 'red', 'points': 15}
>
>aliens = [alien_0, alien_1, alien_2]
>
>for alien in aliens:
>    print(alien)
>```
>
>输出语句：
>
>```python
>{'color': 'green', 'points': 5}
>{'color': 'yellow', 'points': 10}
>{'color': 'red', 'points': 15}
>```
>
>
>
>示例2：
>
>```python
># 创建一个用于存储外星人的空列表
>aliens = []
>
># 创建30个绿色的外星人
>for alien_number in range(30):
>    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
>    aliens.append(new_alien)
>
># 显示前五个外星人
>for alien in aliens[:5]:
>    print(alien)
>print("...")
>
># 显示创建了多少个外星人
>print("Total number of aliens: " + str(len(aliens)))
>```
>
>输出语句：
>
>```python
>{'color': 'green', 'points': 5, 'speed': 'slow'}
>{'color': 'green', 'points': 5, 'speed': 'slow'}
>{'color': 'green', 'points': 5, 'speed': 'slow'}
>{'color': 'green', 'points': 5, 'speed': 'slow'}
>{'color': 'green', 'points': 5, 'speed': 'slow'}
>...
>```
>
>
>
>示例3：
>
>```python
># 创建一个用于存储外星人的空列表
>aliens = []
>
># 创建30个绿色的外星人
>for alien_number in range(30):
>    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
>    aliens.append(new_alien)
>    
>for alien in aliens[0:3]:
>    if alien['color'] == 'green':
>     	alien['color'] = 'yellow'
>         alien['speed'] = 'medium'
>         alien['points'] = 10
>
># 显示前五个外星人
>for alien in aliens[:5]:
>    print(alien)
>print("...")
>
># 显示创建了多少个外星人
>print("Total number of aliens: " + str(len(aliens)))
>```
>
>输出语句：
>
>```python
>{'color': 'yellow', 'points': 10, 'speed': 'medium'}
>{'color': 'yellow', 'points': 10, 'speed': 'medium'}
>{'color': 'yellow', 'points': 10, 'speed': 'medium'}
>{'color': 'green', 'points': 5, 'speed': 'slow'}
>{'color': 'green', 'points': 5, 'speed': 'slow'}
>...
>```
>
>
>
>示例4：
>
>```python
># 创建一个用于存储外星人的空列表
>aliens = []
>
># 创建30个绿色的外星人
>for alien_number in range(30):
>    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
>    aliens.append(new_alien)
>    
>for alien in aliens[0:3]:
>    if alien['color'] == 'green':
>         alien['color'] = 'yellow'
>         alien['speed'] = 'medium'
>         alien['points'] = 10
>    elif alien['color'] == 'yellow':
>         alien['color'] = 'red'
>         alien['speed'] = 'fast'
>         alien['points'] = 15
>
># 显示前五个外星人
>for alien in aliens[:5]:
>    print(alien)
>print("...")
>
># 显示创建了多少个外星人
>print("Total number of aliens: " + str(len(aliens)))
>```
>
>输出语句：
>
>```python
>{'color': 'yellow', 'points': 10, 'speed': 'medium'}
>{'color': 'yellow', 'points': 10, 'speed': 'medium'}
>{'color': 'yellow', 'points': 10, 'speed': 'medium'}
>{'color': 'green', 'points': 5, 'speed': 'slow'}
>{'color': 'green', 'points': 5, 'speed': 'slow'}
>...
>```

### 6.4.2 在字典中存储列表

>   ​		有时候，需要将列表存储在字典中，而不是将字典存储在列表中。
>
>   ​		注意：列表和字典的嵌套层级不应太多。
>
>   
>
>   示例1：
>
>   ```python
>   # pizza.py
>   # 存储所点比萨的信息
>   pizza = {
>       'crust': 'thick',
>       'toppings': ['mushrooms', 'extra cheese'],
>   }
>   
>   # 概述所点的比萨
>   print("You ordered a " + pizza['crust'] + "-crust pizza" +
>       "with the following toppings:")
>   
>   for topping in pizza['toppings']:
>        print("\t" + topping)
>   ```
>
>   输出语句：
>
>   ```python
>   You ordered a thick-crust pizzawith the following toppings:
>        mushrooms
>        extra cheese
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # favorite_languages.py
>   favorite_languages = {
>       'jen': ['python', 'ruby'],
>       'sarah': ['c'],
>       'edward': ['ruby', 'go'],
>       'phil': ['python', 'haskell']
>   }
>   
>   for name, languages in favorite_languages.items():
>        print("\n" + name.title() + "'s favorite languages are:")
>        for language in languages:
>            print("\t" + language.title())
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Jen's favorite languages are:
>        Python
>        Ruby
>   
>   Sarah's favorite languages are:
>        C
>   
>   Edward's favorite languages are:
>        Ruby
>        Go
>   
>   Phil's favorite languages are:
>        Python
>        Haskell
>   ```

### 6.4.3 在字典中存储字典

>   ​		可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。
>
>   
>
>   示例：
>
>   ```python
>   # many_users.py
>   users = {
>       'aeinstein': {
>           'first': 'albert',
>           'last': 'einstein',
>           'location': 'princeton',
>       },
>       'mcurie':{
>           'first': 'marie',
>           'last': 'curie',
>           'location': 'paris',
>       }
>   }
>   
>   for username, user_info in users.items():
>        print("\nUsername: " + username) 
>   	full_name = user_info['first'] + " " + user_info['last']
>        location = user_info['location']
>       
>        print("\tFull name: " + full_name.title())
>        print("\tLocation: " + location.title())
>   ```
>
>   输出语句：
>
>   ```python
>   
>   Username: aeinstein
>        Full name: Albert Einstein
>        Location: Princeton
>   
>   Username: mcurie
>        Full name: Marie Curie
>        Location: Paris
>   ```

## 6.5 小结

>   ​		在本章中，你学习了：如何定义字典，以及如何使用存储在字典中的信息；如何访问和修改字典中的元素，以及如何遍历字典中的所有信息；如何遍历字典中所有的键-值对、所有的键和所有的值；如何在列表中嵌套字典、在字典中嵌套列表以及在字典中嵌套字典。

