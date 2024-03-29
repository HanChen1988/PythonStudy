# 第2章：变量和简单数据类型

>   ​		在本章中，你将学习可在Python程序中使用的各种数据，还将学习如何将数据存储到变量中，以及如何在程序中使用这些变量。

## 2.1 运行hello_world.py时发生的情况

>   ​		运行hello_world.py时，Python都做了些什么呢？
>
>   ​		运行文件hello_world.py时，末尾的.py指出这是一个Python程序，因此编辑器将使用Python解释器来运行它。Python解释器读取整个程序，确定其中每个单词的含义。例如，看到单词print时，解释器就会将括号中的内容打印到屏幕，而不会管括号中的内容是什么。
>
>   ​		编写程序时，编辑器会以各种方式突出程序的不同部分。例如，它知道print是一个函数的名称，因此将其显示为蓝色；它知道“Hello Python world!”不是Python代码，因此将其显示为橙色。这种功能称为语法突出，在你刚开始编写程序时很有帮助。
>
>   
>
>   示例：
>
>   ```python
>   # hello_world.py
>   print("Hello Python world!")
>   ```
>
>   输出语句：
>
>   ```python
>   Hello Python world!
>   ```

## 2.2 变量

>   ​		每个变量都存储了一个值—与变量相关联的信息。
>
>   ​		在程序中可随时修改变量的值，而Python将始终记录变量的最新值。
>
>   
>
>   示例1：
>
>   ```python
>   message = "Hello Python world!"
>   print(message)
>   ```
>
>   输出语句：
>
>   ```python
>   Hello Python world!
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   message = "Hello Python world!"
>   print(message)
>   
>   message = "Hello Python Crash Course world!"
>   print(message)
>   ```
>
>   输出语句：
>
>   ```python
>   Hello Python world!
>   Hello Python Crash Course world!
>   ```

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
>   ​		程序存在错误时，Python解释器将竭尽所能地帮助你找出问题所在。程序无法成功地运行时，解释器会提供一个traceback。traceback是一条记录，指出了解释器尝试运行代码时，在什么地方陷入了困境。
>
>   ​		Python解释器不会对代码做拼写检查，但要求变量名的拼写一致。
>
>   ​		**注意：要理解新的编程概念，最佳的方式是尝试在程序中使用它们。如果你在做本书的练习时陷入了困境，请尝试做点其他的事情。如果这样做后依然无法摆脱困境，请复习相关内容。**
>
>   
>
>   示例：
>
>   ```python
>   message = "Hello Python Crash Course reader!"
>   # 解释器指出，文件hello_world.py的第2行存在错误；它列出了这行代码，旨在帮助你快速找出错误；它还指出了它发现的是什么样的错误。在这里，解释器发现了一个名称错误，并指出打印的变量mesage未定义：Python无法识别你提供的变量名。名称错误通常意味着两种情况：要么是使用变量前忘记了给它赋值，要么是输入变量名时拼写不正确。
>   print(mesage)
>   ```
>
>   输出语句：
>
>   ```python
>   Traceback (most recent call last):
>     File "/Users/hanchen/Desktop/pythontest.py", line 2, in <module>
>       print(mesage)
>   NameError: name 'mesage' is not defined
>   ```

## 2.3 字符串

>   ​		大多数程序都定义并收集某种数据，然后使用它们来做些有意义的事情。鉴于此，对数据进行分类大有裨益。
>
>   ​		字符串就是一系列字符。在Python中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号。
>
>   ​		这种灵活性让你能够在字符串中包含引号和撇号。

### 2.3.1 使用方法修改字符串的大小写

>   ​		方法是Python可对数据执行的操作。每个方法后面都跟着一对括号，这是因为方法通常需要额外的信息来完成其工作。这种信息是在括号内提供的。
>
>   ​		对于字符串，可执行的最简单的操作之一是修改其中的单词的大小写。
>
>   ​		title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。
>
>   ​		存储数据时，方法lower()很有用。很多时候，你无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，再存储它们。以后需要显示这些信息时，再将其转换为最合适的大小写方式。
>
>   
>
>   示例1：
>
>   ```python
>   # name.py
>   # 小写的字符串"ada lovelace"存储到了变量name中。
>   name = "ada lovelace"
>   # 在print()语句中，方法title()出现在这个变量的后面。在name.title()中，name后面的句点（.）让python对变量name执行方法title()指定的操作。函数title()不需要额外的信息，因此它后面的括号是空的。
>   print(name.title())
>   ```
>
>   输出语句：
>
>   ```python
>   Ada Lovelace
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   name = "Ada Lovelace"
>   print(name.upper())
>   print(name.lower())
>   ```
>
>   输出语句：
>
>   ```python
>   ADA LOVELACE
>   ada lovelace
>   ```

### 2.3.2 合并（拼接）字符串

>   ​		在很多情况下，都需要合并字符串。
>
>   ​		Python使用加号（+）来合并字符串。
>
>   ​		这种合并字符串的方法称为拼接。通过拼接，可使用存储在变量中的信息来创建完整的消息。
>
>   
>
>   示例：
>
>   ```python
>   first_name = "ada"
>   last_name = "lovelace"
>   full_name = first_name + " " + last_name
>   
>   message = "Hello，" + full_name.title() + "!"
>   print(message)
>   ```
>
>   输出语句：
>
>   ```python
>   Hello，Ada Lovelace!
>   ```

### 2.3.3 使用制表符或换行符来添加空白

>   ​		在编程中，空白泛指任何非打印字符，如空格、制表符和换行符。你可以使用空白来组织输出，以使其更已读。
>
>   ​		要在字符串中添加制表符，可使用字符组合\t。
>
>   ​		要在字符串中添加换行符，可使用字符组合\n。
>
>   ​		要在同一个字符串中同时包含制表符和换行符，可使用字符组合\n\t。
>
>   
>
>   示例1：
>
>   ```python
>   print("Python")
>   print("\tPython")
>   ```
>
>   输出语句：
>
>   ```python
>   Python
>       Python
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   print("Languages:\nPython\nC\nJavaScript")
>   ```
>
>   输出语句：
>
>   ```python
>   Languages:
>   Python
>   C
>   JavaScript
>   ```
>
>   
>
>   示例3：
>
>   ```python
>   print("Languages:\n\tPython\n\tC\n\tJavaScript")
>   ```
>
>   输出语句：
>
>   ```python
>   Languages:
>        Python
>        C
>        JavaScript
>   ```

### 2.3.4 删除空白

>   ​		在程序中，额外的空白可能令人迷惑。对程序员来说，'python'和'python '看起来几乎没什么两样，但对程序来说，它们却是两个不同的字符串。
>
>   ​		空白很重要，因为你经常需要比较两个字符串是否相同。
>
>   ​		Python能够找出字符串开头和末尾多余的空白。
>
>   ​		要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中。
>
>   ​		在实际程序中，这些剥除函数最常用于在存储用户输入前对其进行清理。
>
>   
>
>   示例1：
>
>   ```python
>   # 临时删除字符串中的空白
>   favorite_language = 'python '
>   print(favorite_language)
>   print(favorite_language.rstrip())
>   print(favorite_language)
>   ```
>
>   输出语句：
>
>   ```python
>   python 
>   python
>   python 
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # 永久删除字符串中的空白
>   favorite_language = 'python '
>   favorite_language = favorite_language.rstrip()
>   print(favorite_language)
>   ```
>
>   输出语句：
>
>   ```python
>   python
>   ```
>
>   
>
>   示例3：
>
>   ```python
>   favorite_language = ' python '
>   # 删除末尾的空格
>   print(favorite_language.rstrip())
>   # 删除开头的空格
>   print(favorite_language.lstrip())
>   # 删除两端的空格
>   print(favorite_language.strip())
>   ```
>
>   输出语句：
>
>   ```python
>    python
>   python 
>   python
>   ```

### 2.3.5 使用字符串时避免语法错误

>   ​		语法错误是一种时不时会遇到的错误。程序中包含非法的Python代码时，就会导致语法错误。
>
>   ​		例如，在用单引号括起的字符串中，如果包含撇号，就将导致错误。这是因为这会导致Python将第一个单引号和撇号之间的内容视为一个字符串，进而将余下的文本视为Python代码，从而引发错误。
>
>   ​		**注意：编写程序时，编辑器的语法突出功能可帮助你快速找出某些语法错误。看到Python代码以普通句子的颜色显示，或者普通句子以Python代码的颜色显示时，就可能意味着文件中存在引号不匹配的情况。**
>
>   
>
>   示例1：
>
>   ```python
>   # apostrophe.py
>   message = "One of Python's strengths is its diverse community."
>   # 撇号位于两个双引号之间，因此Python解释器能够正确地理解这个字符串。
>   print(message)
>   ```
>
>   输出语句：
>
>   ```python
>   One of Python's strengths is its diverse community.
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # 如果你使用单引号，Python将无法正确地确定字符串的结束位置。
>   message = 'One of Python's strengths is its diverse community.'
>   print(message)
>   ```
>
>   输出语句：
>
>   ```python
>     File "/Users/hanchen/Desktop/pythontest.py", line 1
>       message = 'One of Python's strengths is its diverse community.'
>                                ^
>   SyntaxError: invalid syntax
>   ```

### 2.3.6 Python2中的print语句

>   ​		在Python2中，无需将要打印的内容放在括号内。从技术上说，Python3中的print是一个函数，因为括号比不可少。有些Python2 print语句也包含括号，但其行为与Python3中稍有不同。
>
>   ​		简单地说，在Python2代码中，有些print语句包含括号，有些不包含。
>
>   
>
>   示例：
>
>   ```python
>   # python2.7
>   print "Hello Python 2.7 world!"
>   ```
>
>   输出语句：
>
>   ```python
>   Hello Python 2.7 world!
>   ```

## 2.4 数字

>   ​		在编程中，经常使用数字来记录游戏得分、表示可视化数据、存储Web应用信息等。Python根据数字的用法以不同的方式处理它们。

### 2.4.1 整数

>   ​		在Python中，可对整数执行加（+）减（-）乘（*）除（/）运算。
>
>   ​		Python使用两个乘号表示乘方运算。
>
>   ​		Python还支持运算次序，因此你可在同一个表达式中使用多种运算。你还可以使用括号来修改运算次序，让Python按你指定的次序执行运算。
>
>   ​		空格不影响Python计算表达式的方式，它们的存在旨在让你阅读代码时，能迅速确定先执行哪些运算。
>
>   
>
>   示例1：
>
>   ```python
>   print(2 + 3)
>   print(3 - 2)
>   print(2 * 3)
>   print(3 / 2)
>   ```
>
>   输出语句：
>
>   ```python
>   5
>   1
>   6
>   1.5
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   print(3 ** 2)
>   print(3 ** 3)
>   print(10 ** 6)
>   ```
>
>   输出语句：
>
>   ```python
>   9
>   27
>   1000000
>   ```
>
>   
>
>   示例3：
>
>   ```python
>   print(2 + 3*4)
>   print((2 + 3) * 4)
>   ```
>
>   输出语句：
>
>   ```python
>   14
>   20
>   ```

### 2.4.2 浮点数

>   ​		Python将带小数点的数字都称为浮点数。
>
>   ​		在很大程度上说，使用浮点数时都无需考虑其行为。你只需输入要使用的数字，Python通常都会按你期望的方式处理它们。
>
>   ​		但需要注意的是，结果包含的小数位数可能是不确定的。
>
>   ​		所有语言都存在这种问题，没有什么可担心的。Python会尽力找到一种方式，以尽可能精确地表示结果，但鉴于计算机内部表示数字的方式，这在有些情况下很难。就现在而言，暂时忽略多余的小数位数即可。
>
>   
>
>   示例1：
>
>   ```python
>   print(0.1 + 0.1)
>   print(0.2 + 0.2)
>   print(2 * 0.1)
>   print(2 * 0.2)
>   ```
>
>   输出语句：
>
>   ```python
>   0.2
>   0.4
>   0.2
>   0.4
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   print(0.2 + 0.1)
>   print(3 * 0.1)
>   ```
>
>   输出语句：
>
>   ```python
>   0.30000000000000004
>   0.30000000000000004
>   ```

### 2.4.3 使用函数str()避免类型错误

>   ​		你经常需要在消息中使用变量的值。
>
>   ​		大多数情况下，在Python中使用数字都非常简单。如果结果出乎意料，请检查Python是否按你期望的方式将数字解读为了数值或字符串。
>
>   
>
>   示例1：
>
>   ```python
>   # birthday.py
>   age = 23
>   # Python发现你使用了一个值为整数（int）的变量，但它不知道该如何解读这个值。Python知道，这个变量表示的可能是数值23，也可能是字符2和3。
>   message = "Happy " + age + "rd Birthday!"
>   
>   print(message)
>   ```
>
>   输出语句：
>
>   ```python
>   # 这是一个类型错误，意味着Python无法识别你使用的信息。
>   Traceback (most recent call last):
>     File "/Users/hanchen/Desktop/pythontest.py", line 3, in <module>
>       message = "Happy " + age + "rd Birthday!"
>   TypeError: can only concatenate str (not "int") to str
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # birthday.py
>   age = 23
>   # 在字符串中使用整数时，需要显示地指出你希望Python将这个整数用作字符串。为此，可调用函数str()，它让Python将非字符串值表示为字符串。
>   message = "Happy " + str(age) + "rd Birthday!"
>   
>   print(message)
>   ```
>
>   输出语句：
>
>   ```python
>   Happy 23rd Birthday!
>   ```

### 2.4.4 Python2中的整数

>   ​		在Python2中，整数除法的结果只包含整数部分，小数部分被删除。请注意，计算整数结果时，采取的方式不是四舍五入，而是小数部分直接删除。
>
>   ​		在Python2中，若要避免这种情况，务必确保至少有一个操作数为浮点数，这样结果也将为浮点数。
>
>   ​		从Python3转而用Python2或从Python2转而用Python3时，这种除法行为常常会令人迷惑。使用或编写同时使用浮点数和整数的代码时，一定要注意这种异常行为。
>
>   
>
>   示例1：
>
>   ```python
>   # python2.7
>   # Python返回的结果为1，而不是1.5。
>   3 / 2
>   ```
>
>   输出语句：
>
>   ```python
>   1
>   ```
>
>   
>
>   示例2：
>
>   ```python
>   # python2.7
>   print(3 / 2)
>   print(3.0 / 2)
>   print(3 / 2.0)
>   print(3.0 / 2.0)
>   ```
>
>   输出语句：
>
>   ```python
>   1
>   1.5
>   1.5
>   1.5
>   ```

## 2.5 注释

>   ​		在大多数编程语言中，注释都是一项很有用的功能。
>
>   ​		前面编写的程序中都只包含Python代码，但随着程序越来越大、越来越复杂，就应在其中添加说明，对你解决问题的方法进行大致的阐述。
>
>   ​		注释让你能够使用自然语言在程序中添加说明。

### 2.5.1 如何编写注释

>   ​		在Python中，注释用井号（#）标识。井号后面的内容都会被Python解释器忽略。
>
>   
>
>   示例：
>
>   ```python
>   # comment.py
>   # 向大家问好
>   print("Hello Python people!")
>   ```
>
>   输出语句：
>
>   ```python
>   Hello Python people!
>   ```

### 2.5.2 该编写什么样的注释

>   ​		编写注释的主要目的是阐述代码要做什么，以及是如何做的。在开发项目期间，你对各个部分如何协同工作了如执掌，但过段时间后，有些细节你可能不记得了。当然，你总是可以通过研究代码来确定各个部分的工作原理，但通过编写注释，以清晰的自然语言对解决方案进行概述，可节省很多时间。
>
>   ​		要成为专业程序员或其他程序员合作，就必须编写有意义的注释。当前，大多数软件都是合作编写的，编写者可能是同一家公司的多名员工，也可能是众多致力于同一个开源项目的人员。训练有素的程序员都希望代码中包含注释，因此你最好从现在开始就在程序中添加描述性注释。作为新手，最值得养成的习惯之一是，在代码中编写清晰、简洁的注释。
>
>   ​		如果不确定是否要编写注释，就问问自己，找到合理的解决方案前，是否考虑了多个解决方案。如果答案是肯定的，就编写注释对你的解决方案进行说明吧。相比回过头去再添加注释，删除多余的注释要容易得多。

## 2.6 Python之禅

>   ​		经验丰富的程序员倡导尽可能避繁就简。
>
>   ​		Python社区的理念都包含在Tim Peters撰写的“Python之禅”中。要获悉只需在解释器中执行命令import this。
>
>   ​		Python程序员笃信代码可以编写得漂亮而优雅。编程是要解决问题的，设计良好、高效而漂亮的解决方案都会让程序员心生敬意。
>
>   ​		如果有两个解决方案，一个简单，一个复杂，但都行之有效，就选择简单的解决方案吧。
>
>   ​		现实是复杂的，有时候可能没有简单的解决方案。在这种情况下，就选择最简单可行的解决方案吧。
>
>   ​		即便是复杂的代码，也要让它易于理解。开发的项目涉及复杂代码时，一定要为这些代码编写有益的注释。

## 2.7 小结

>   ​		在本章中，你学习了：如何使用变量；如何创建描述性变量名以及如何消除名称错误和语法错误；字符串是什么，以及如何使用小写、大写和首字母大写方式显示字符串；使用空白来显示整洁的输出，以及如何剔除字符串中多余的空白；如何使用整数和浮点数；使用数值数据时需要注意的意外行为。你还学习了如何编写说明性注释，让代码对你和其他人来说更容易理解。最后，你了解了让代码尽可能简单的理念。

