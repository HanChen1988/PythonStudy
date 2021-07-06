# 第2章：变量和简单数据类型

>   ​		在本章中，你将学习可在Python程序中使用的各种数据，还将学习如何将数据存储到变量中，以及如何在程序中使用这些变量。

## 2.1 运行hello_world.py时发生的情况

>   ​		运行hello_world.py时，Python都做了些什么呢？
>
>   ​				hello_world.py
>
>   ​				print("Hello Python world!")
>
>   ​		运行上述代码时，你将看到如下输出：
>
>   ​				Hello Python world!
>
>   ​		运行文件hello_world.py时，末尾的.py指出这是一个Python程序，因此编辑器将使用Python解释器来运行它。Python解释器读取整个程序，确定其中每个单词的含义。例如，看到单词print时，解释器就会将括号中的内容打印到屏幕，而不会管括号中的内容是什么。
>
>   ​		编写程序时，编辑器会以各种方式突出程序的不同部分。例如，它知道print是一个函数的名称，因此将其显示为蓝色；它知道“Hello Python world!”不是Python代码，因此将其显示为橙色。这种功能称为语法突出，在你刚开始编写程序时很有帮助。

## 2.2 变量

>   ​		下面来尝试在hello_world.py中使用一个变量。
>
>   ​				如下所示：
>
>   ​				message = "Hello Python world!"
>
>   ​				print(message)
>
>   ​		运行这个程序，看看结果如何。你会发现，输出与以前相同：
>
>   ​				Hello Python world!
>
>   ​		我们添加了一个名为message的变量。每个变量都存储了一个值—与变量相关联的信息。
>
>   ​				进一步扩展这个程序：修改hello_world.py，使其再打印一条消息。
>
>   ​				message = "Hello Python world!"
>
>   ​				print(message)
>
>   ​				
>
>   ​				message = "Hello Python Crash Course world!"
>
>   ​				print(message)
>
>   ​		现在如果运行这个程序，将看到两行输出：
>
>   ​				Hello Python world!
>
>   ​				Hello Python Crash Course world!
>
>   ​		在程序中可随时修改变量的值，而Python将始终记录变量的最新值。

### 2.2.1 变量的命名和使用

>   ​		在Python中使用变量时，需要遵守一些规则和指南。违反这些规则将引发错误，而指南旨在让你编写的代码更容易阅读和理解。
>
>   ​		请务必牢记下述有关变量的规则。

-   变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头。

    >   ​		例如，可将变量命名为message_1，但不能将其命名为1_message。

-   变量名不能包含空格，但可使用下划线来分隔其中的单词。

    >   ​		例如，变量名greeting_message可行，但变量名greeting message会引发错误。

-   不要将Python关键字和函数名。

    >   ​		即不要使用Python保留用于特殊用途的单词，如print。

-   变量名应既简短又具有描述性。

    >   ​		例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。

-   慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。

>   ​		要创建良好的变量名，需要经过一定的实践，在程序复杂而有趣时尤其如此。随着你编写的程序越来越多，并开始阅读别人编写的代码，将越来越善于创建有意义的变量名。
>
>   ​		**注意：就目前而言，应使用小写的Python变量名。在变量名中使用大写字母虽然不会导致错误，但避免使用大写字母是个不错的主意。**

### 2.2.2 使用变量时避免命名错误

>   ​		程序员都会犯错，而且大多数程序员每天都会犯错。虽然优秀的程序员也会犯错，但他们也知道如何高效地消除错误。
>
>   ​				错误的代码：
>
>   ​				message = "Hello Python Crash Course reader!"
>
>   ​				print(**mesage**)
>
>   ​		程序存在错误时，Python解释器将竭尽所能地帮助你找出问题所在。程序无法成功地运行时，解释器会提供一个traceback。traceback是一条记录，指出了解释器尝试运行代码时，在什么地方陷入了困境。
>
>   ​				Python解释器提供的traceback：
>
>   ​				Traceback（most recent call last）：
>
>   ​						File "hello_world.py", line 2, in <module>
>
>   ​						print(mesage)
>
>   ​				NameError：name 'mesage' is not defined
>
>   ​		解释器指出，文件hello_world.py的第2行存在错误；它列出了这行代码，旨在帮助你快速找出错误；它还指出了它发现的是什么样的错误。在这里，解释器发现了一个名称错误，并指出打印的变量mesage未定义：Python无法识别你提供的变量名。名称错误通常意味着两种情况：要么是使用变量前忘记了给它赋值，要么是输入变量名时拼写不正确。
>
>   ​		Python解释器不会对代码做拼写检查，但要求变量名的拼写一致。
>
>   ​		**注意：要理解新的编程概念，最佳的方式是尝试在程序中使用它们。如果你在做本书的练习时陷入了困境，请尝试做点其他的事情。如果这样做后依然无法摆脱困境，请复习相关内容。**

## 2.3 字符串

>   ​		大多数程序都定义并收集某种数据，然后使用它们来做些有意义的事情。鉴于此，对数据进行分类大有裨益。
>
>   ​		字符串就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号。
>
>   ​		这种灵活性让你能够在字符串中包含引号和撇号。

### 2.3.1 使用方法修改字符串的大小写

>   ​		对于字符串，可执行的最简单的操作之一是修改其中的单词的大小写。
>
>   ​				name.py
>
>   ​				name = "ada lovelace"
>
>   ​				print(name.title())
>
>   ​		在这个示例中，小写的字符串"ada lovelace"存储到了变量name中。在print()语句中，方法title()出现在这个变量的后面。方法是Python可对数据执行的操作。在name.title()中，name后面的句点（.）让python对变量name执行方法title()指定的操作。每个方法后面都跟着一对括号，这是因为方法通常需要额外的信息来完成其工作。这种信息是在括号内提供的。函数title()不需要额外的信息，因此它后面的括号是空的。
>
>   ​		title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。
>
>   ​		还有其他几个很有用的大小写处理方法。例如，要将字符串改为全部大写或全部小写，可以像下面这样做：
>
>   ​				name = "Ada Lovelace"
>
>   ​				print(name.upper())
>
>   ​				print(name.lower())
>
>   ​				这些代码的输出如下：
>
>   ​				ADA LOVELACE
>
>   ​				ada lovelace
>
>   ​		存储数据时，方法lower()很有用。很多时候，你无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，再存储它们。以后需要显示这些信息时，再将其转换为最合适的大小写方式。

### 2.3.2 合并（拼接）字符串

>   ​		在很多情况下，都需要合并字符串。
>
>   ​		Python使用加号（+）来合并字符串。
>
>   ​		这种合并字符串的方法称为拼接。通过拼接，可使用存储在变量中的信息来创建完整的消息。
>
>   ​		示例：
>
>   ​				first_name = "ada"
>
>   ​				last_name = "lovelace"
>
>   ​				full_name = first_name + " " + last_name
>
>   ​				
>
>   ​				message = "Hello，" + full_name.title() + "!"
>
>   ​				print(message)

### 2.3.3 使用制表符或换行符来添加空白

>   ​		在编程中，空白泛指任何非打印字符，如空格、制表符和换行符。你可以使用空白来组织输出，以使其更已读。
>
>   ​		要在字符串中添加制表符，可使用字符组合\t，如下述代码所示：
>
>   ​				>>>print("Python")
>
>   ​				Python
>
>   ​				>>>print("\tPython")
>
>   ​					  Python
>
>   ​		要在字符串中添加换行符，可使用字符组合\n，如下述代码所示：
>
>   ​				>>>print("Languages:\nPython\nC\nJavaScript")
>
>   ​				Languages:
>
>   ​				Python
>
>   ​				C
>
>   ​				JavaScript
>
>   ​		还可在同一个字符串中同时包含制表符和换行符，可使用字符组合\n\t，如下述代码所示：
>
>   ​				>>>print("Languages:\n\tPython\n\tC\n\tJavaScript")
>
>   ​				Languages:
>
>   ​						Python
>
>   ​						C
>
>   ​						JavaScript

### 2.3.4 删除空白

>   ​		在程序中，额外的空白可能令人迷惑。对程序员来说，'python'和'python '看起来几乎没什么两样，但对程序来说，它们却是两个不同的字符串。
>
>   ​		空白很重要，因为你经常需要比较两个字符串是否相同。
>
>   ​		Python能够找出字符串开头和末尾多余的空白。
>
>   ​				临时删除字符串中的空白：
>
>   ​						>>>favorite_language = 'python'
>
>   ​						>>>favorite_language
>
>   ​						'python '
>
>   ​						>>>favorite_language.rstrip()
>
>   ​						'python'
>
>   ​						>>>favorite_language
>
>   ​						'python '
>
>   ​				永久删除字符串中的空白：
>
>   ​						>>>favorite_language = 'python '
>
>   ​						>>>favorite_language = favorite_language.rstrip()
>
>   ​						>>>favorite_language
>
>   ​						'python'
>
>   ​				要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中。
>
>   ​		分别删除末尾、开头和两端的空格。在实际程序中，这些剥除函数最常用于在存储用户输入前对其进行清理。
>
>   ​				>>>favorite_language = ' python '
>
>   ​				>>>favorite_language.rstrip()
>
>   ​				' python'
>
>   ​				>>>favorite_language.lstrip()
>
>   ​				'python '
>
>   ​				>>>favorite_language.strip()
>
>   ​				'python'

### 2.3.5 使用字符串时避免语法错误

>   ​		语法错误是一种时不时会遇到的错误。程序中包含非法的Python代码时，就会导致语法错误。
>
>   ​		例如，在用单引号括起的字符串中，如果包含撇号，就将导致错误。这是因为这会导致Python将第一个单引号和撇号之间的内容视为一个字符串，进而将余下的文本视为Python代码，从而引发错误。
>
>   ​				apostrophe.py
>
>   ​						message = "One of Python's strengths is its diverse community."
>
>   ​						print(message)
>
>   ​				撇号位于两个双引号之间，因此Python解释器能够正确地理解这个字符串：
>
>   ​						One of Python's strengths is its diverse community.
>
>   ​				然而，如果你使用单引号，Python将无法正确地确定字符串的结束位置：
>
>   ​						message = 'One of Python's strengths is its diverse community.'
>
>   ​						print(message)
>
>   ​				而你将看到如下输出：
>
>   ​						File "apostrophe.py", line 1
>
>   ​						  message = 'One of Python's strengths is its diverse community.'
>
>   ​								                               ^
>
>   ​						SyntaxError：invalid syntax
>
>   ​		**注意：编写程序时，编辑器的语法突出功能可帮助你快速找出某些语法错误。看到Python代码以普通句子的颜色显示，或者普通句子以Python代码的颜色显示时，就可能意味着文件中存在引号不匹配的情况。**

### 2.3.6 Python2中的print语句

>   ​		在Python2中，print语句的语法稍有不同：
>
>   ​				> python2.7
>
>   ​				>>>print "Hello Python 2.7 world!"
>
>   ​				Hello Python 2.7 world!
>
>   ​		在Python2中，无需将要打印的内容放在括号内。从技术上说，Python3中的print是一个函数，因为括号比不可少。有些Python2 print语句也包含括号，但其行为与Python3中稍有不同。
>
>   ​		简单地说，在Python2代码中，有些print语句包含括号，有些不包含。

## 2.4 数字

>   ​		在编程中，经常使用数字来记录游戏得分、表示可视化数据、存储Web应用信息等。Python根据数字的用法以不同的方式处理它们。

### 2.4.1 整数

>   ​		在Python中，可对整数执行加（+）减（-）乘（*）除（/）运算。
>
>   ​				>>> 2 + 3
>
>   ​				5
>
>   ​				>>> 3 - 2
>
>   ​				1
>
>   ​				>>> 2 * 3
>
>   ​				6
>
>   ​				>>> 3 / 2
>
>   ​				1.5
>
>   ​		在终端会话中，Python直接返回运算结果。
>
>   ​		Python使用两个乘号表示乘方运算：
>
>   ​				>>> 3 ** 2
>
>   ​				9
>
>   ​				>>> 3 ** 3
>
>   ​				27
>
>   ​				>>> 10 ** 6
>
>   ​				1000000
>
>   ​		Python还支持运算次序，因此你可在同一个表达式中使用多种运算。你还可以使用括号来修改运算次序，让Python按你指定的次序执行运算。
>
>   ​				>>> 2 + 3*4
>
>   ​				14
>
>   ​				>>> (2 + 3) * 4
>
>   ​				20
>
>   ​		空格不影响Python计算表达式的方式，它们的存在旨在让你阅读代码时，能迅速确定先执行哪些运算。

### 2.4.2 浮点数

>   ​		Python将带小数点的数字都称为浮点数。
>
>   ​		在很大程度上说，使用浮点数时都无需考虑其行为。你只需输入要使用的数字，Python通常都会按你期望的方式处理它们：
>
>   ​				>>> 0.1 + 0.1
>
>   ​				0.2
>
>   ​				>>> 0.2 + 0.2
>
>   ​				0.4
>
>   ​				>>> 2 * 0.1
>
>   ​				0.2
>
>   ​				>>> 2 * 0.2
>
>   ​				0.4
>
>   ​		但需要注意的是，结果包含的小数位数可能是不确定的：
>
>   ​				>>> 0.2 + 0.1
>
>   ​				0.30000000000000004
>
>   ​				>>> 3 * 0.1
>
>   ​				0.30000000000000004		
>
>   ​		所有语言都存在这种问题，没有什么可担心的。Python会尽力找到一种方式，以尽可能精确地表示结果，但鉴于计算机内部表示数字的方式，这在有些情况下很难。就现在而言，暂时忽略多余的小数位数即可。			

### 2.4.3 使用函数str()避免类型错误

>   ​		你经常需要在消息中使用变量的值。
>
>   ​		大多数情况下，在Python中使用数字都非常简单。如果结果出乎意料，请检查Python是否按你期望的方式将数字解读为了数值或字符串。
>
>   ​		如：
>
>   ​				birthday.py
>
>   ​				age = 23
>
>   ​				message = "Happy " + age + "rd Birthday!"
>
>   ​				print(message)
>
>   ​		你可能认为，上述代码会打印一条简单的生日祝福语：Happy 23rd birthday!。但如果你运行这些代码，将发现它们会引发错误：
>
>   ​				Traceback（most recent call last）：
>
>   ​					File "birthday.py"，line 2, in<module>
>
>   ​						message = "Happy " + age + "rd Birthday!"
>
>   ​				TypeError：Can't convert 'int' object to str inplicitly
>
>   ​		这是一个**类型错误**，意味着Python无法识别你使用的信息。在这个示例中，Python发现你使用了一个值为整数（int）的变量，但它不知道该如何解读这个值。Python知道，这个变量表示的可能是数值23，也可能是字符2和3。
>
>   ​		像上面这样在字符串中使用整数时，需要显示地指出你希望Python将这个整数用作字符串。为此，可调用函数str()，它让Python将非字符串值表示为字符串。
>
>   ​		birthday.py修改如下：
>
>   ​				age = 23
>
>   ​				message = "Happy " + str(age) + "rd Birthday!"
>
>   ​				print(message)
>
>   ​		打印结果：
>
>   ​				Happy 23rd Birthday!

### 2.4.4 Python2中的整数

>   ​		在Python2中，整数除法的结果只包含整数部分，小数部分被删除。请注意，计算整数结果时，采取的方式不是四舍五入，而是小数部分直接删除。
>
>   ​		从Python3转而用Python2或从Python2转而用Python3时，这种除法行为常常会令人迷惑。使用或编写同时使用浮点数和整数的代码时，一定要注意这种异常行为。
>
>   
>
>   ​		在Python2中，将两个整数相除得到的结果稍有不同：
>
>   ​				>>>python2.7
>
>   ​				>>>3 / 2
>
>   ​				1
>
>   ​		Python返回的结果为1，而不是1.5。
>
>   
>
>   ​		在Python2中，若要避免这种情况，务必确保至少有一个操作数为浮点数，这样结果也将为浮点数：
>
>   ​				>>> 3 / 2
>
>   ​				1
>
>   ​				>>> 3.0 / 2
>
>   ​				1.5
>
>   ​				>>> 3 / 2.0
>
>   ​				1.5
>
>   ​				>>> 3.0 / 2.0
>
>   ​				1.5

## 2.5 注释

>   ​		在大多数编程语言中，注释都是一项很有用的功能。
>
>   ​		前面编写的程序中都只包含Python代码，但随着程序越来越大、越来越复杂，就应在其中添加说明，对你解决问题的方法进行大致的阐述。
>
>   ​		注释让你能够使用自然语言在程序中添加说明。
