# 第10章：文件和异常

>   ​		在本章中，你将学习处理文件，让程序能够快速地分析大量的数据；你将学习错误处理，避免程序在面对意外情形时崩溃；你将学习异常，它们是Python创建的特殊对象，用于管理程序运行时出现的错误；你还将学习模块json，它让你能够保存用户数据，以免在程序停止运行后丢失。
>
>   ​		学习处理文件和保存数据可让你的程序使用起来更容易：用户将能够选择输入什么样的数据，以及在什么时候输入；用户使用你的程序做一些工作后，可将程序关闭，以后再接着往下做。学习处理异常可帮助你应对文件不存在的情形，以及处理其他可能导致程序崩溃的问题。这让你的程序在面对错误的数据时更健壮—不管这些错误数据源自无意的错误，还是源自破坏程序的恶意企图。你在本章学习的技能可提高程序的适用性、可用性和稳定性。

## 10.1 从文件中读取数据

>   ​		文本文件可存储的数据量多得难以置信。
>
>   ​		每当需要分析或修改存储在文件中的信息时，读取文件都很有用，对数据分析应用程序来说尤其如此。
>
>   ​		要使用文本文件中的信息，首先需要将信息读取到内存中。为此，你可以一次性读取文件的全部内容，也可以以每次一行的方式逐步读取。

### 10.1.1 读取整个文件

>   ​		要读取文件，需要一个包含几行文本的文件。
>
>   ​		要以任何方式使用文件—哪怕仅仅是打印其内容，都得先打开文件，这样才能访问它。
>
>   ​		函数open()接受一个参数：要打开的文件的名称。Python在当前执行的文件所在的目录中查找指定的文件。
>
>   ​		函数open()返回一个表示文件的对象。Python将这个对象存储在我们将在后面使用的变量中。
>
>   ​		关键字with在不再需要访问文件后将其关闭。
>
>   ​		read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。要删除末尾的空行，可在print语句中使用rstrip()删除字符串末尾的空白。

示例1：

```python
# file_reader.py
with open('/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

输出语句：

```python
3.1415926535
  8979323846
  2643383279

```

示例2：

```python
# file_reader.py
with open('/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
```

输出语句：

```python
3.1415926535
  8979323846
  2643383279
```

### 10.1.2 文件路径

>   ​		要让Python打开不与程序文件位于同一个目录中的文件，需要提供文件路径，它让Python到系统的特定位置去查找。
>
>   ​		相对文件路径：让Python到指定的位置去查找，而该位置是相对于当前运行的程序所在目录的。
>
>   ​		绝对文件路径：可读取系统任何地方的文件。
>
>   ​		注意：Windows系统有时能够正确地解读文件路径中的斜杠。如果你使用的是Windows系统，且结果不符合预期，请确保在文件路径中使用的是反斜杠。另外，由于反斜杠在Python中被视为转义标记，为在Windows中确保万无一失，应以原始字符串的方式指定路径，即在开头的单引号前加上r。

示例1：

```python
# 相对路径
# 在Linux和OS X中
with open('text_files/filename.txt') as file_object

# 在Windows系统中
with open('text_files\filename.txt') as file_object
```

示例2：

```python
# 绝对路径
# 在Linux和OS X中
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:

# 在Windows系统中
file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
with open(file_path) as file_object:
```

### 10.1.3 逐行读取

>   ​		读取文件时，常常需要检查其中的每一行：你可能要在文件中查找特定的信息，或者要以某种方式修改文件中的文本。
>
>   ​		要以每次一行的方式检查文件，可对文件对象使用for循环。
>
>   ​		调用open()，将一个表示文件及其内容的对象存储到变量file_object中。
>
>   ​		使用关键字with，让Python负责妥善地打开和关闭文件。
>
>   ​		每行末尾都有两个换行符：一个来自文件，另一个来自print语句。要消除这些多余的空白行，可在print语句中使用rstrip()。

示例1：

```python
# file_reader.py
filename = 'pi_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    for line in file_object:
        print(line)
```

输出语句：

```python
3.1415926535

  8979323846

  2643383279

```

示例2：

```python
# file_reader.py
filename = 'pi_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())
```

输出语句：

```python
3.1415926535
  8979323846
  2643383279
```

### 10.1.4 创建一个包含文件各行内容的列表

>   ​		使用关键字with时，open()返回的文件对象只在with代码块内可用。
>
>   ​		如果要在with代码块外访问文件的内容，可在with代码块内将文件的各行存储在一个列表中，并在with代码块外使用该列表：你可以立即处理文件的各个部分，也可推迟到程序后面再处理。
>
>   ​		方法readlines()从文件中读取每一行，并将其存储到一个列表中。

示例：

```python
# file_reader.py
filename = 'pi_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
```

输出语句：

```python
3.1415926535
  8979323846
  2643383279
```

### 10.1.5 使用文件的内容

>   ​		将文件读取到内存中后，就可以以任何方式使用这些数据了。
>
>   ​		注意：读取文本文件时，Python将其中的所有文本都解读为字符串。如果你读取的是数字，并要将其作为数值使用，就必须使用函数int()将其转换为整数，或使用函数float()将其转换为浮点数。

示例1：

```python
# pi_string.py
filename = 'pi_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
```

输出语句：

```python
3.1415926535  8979323846  2643383279
36
```

示例2：

```python
# pi_string.py
filename = 'pi_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
```

输出语句：

```python
3.141592653589793238462643383279
32
```

### 10.1.6 包含一百万位的大型文件

>   ​		对于你可处理的数据量，Python没有任何限制；只要系统的内存足够多，你想处理多少数据都可以。

示例：

```python
# pi_string.py
filename = 'pi_million_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
```

输出语句：

```python
3.14159265358979323846264338327950288419716939937510...
1000002
```

### 10.1.7 圆周率值中包含你的生日吗

示例：

```python
# pi_string.py
filename = 'pi_million_digits.txt'
filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename

with open(filepath) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```

输出语句：

```python
Enter your birthday, in the form mmddyy: 120372
Your birthday appears in the first million digits of pi!
```

## 10.2 写入文件

>   ​		保存数据的最简单的方式之一是将其写入到文件中。通过将输出写入文件，即便关闭包含程序输出的终端窗口，这些输出也依然存在：你可以在程序结束运行后查看这些输出，可与别人分享输出文件，还可编写程序来将这些输出读取到内存中并进行处理。

### 10.2.1 写入空文件

>   ​		要将文本写入文件，你在调用open()时需要提供另一个实参，告诉Python你要写入打开的文件。
>
>   ​		调用open()时提供了两个实参。第一个实参是要打开的文件的名称；第二个实参（'w'）告诉Python，我们要以写入模式打开这个文件。
>
>   ​		打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'）。如果你省略了模式实参，Python将以默认的只读模式打开文件。
>
>   ​		如果你要写入的文件不存在，函数open()将自动创建它。
>
>   ​		然而，以写入（'w'）模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。
>
>   ​		注意：Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。

示例：

```python
# write_message.py
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```

输出语句：

```python
# programming.txt
I love programming.
```

### 10.2.2 写入多行

>   ​		函数write()不会在你写入的文件末尾添加换行符，因此如果你写入多行时没有指定换行符，文件看起来可能不是你希望的那样。
>
>   ​		像显示到终端的输出一样，还可以使用空格、制表符和空行来设置这些输出的格式。

示例1：

```python
# write_message.py
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
```

输出语句：

```python
# programming.txt
I love programming.I love creating new games.
```

示例2：

```python
# write_message.py
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```

输出语句：

```python
# programming.txt
I love programming.
I love creating new games.

```

### 10.2.3 附加到文件

>   ​		如果你要给文件添加内容，而不是覆盖原有的内容，可以附加模式打开文件。
>
>   ​		附加模式打开文件时，Python不会在返回文件对象前清空文件，而你写入到文件的行都将添加到文件末尾。
>
>   ​		如果指定的文件不存在，Python将为你创建一个空文件。

示例：

```python
# write_message.py
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
```

输出语句：

```python
# programming.txt
I love programming.
I love creating new games.
I also love finding meaning in large datasets.
I love creating apps that can run in a browser.
```

## 10.3 异常

>   ​		Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。
>
>   ​		每当发生让Python不知所错的错误时，它都会创建一个异常对象。
>
>   ​		如果你编写了处理该异常的代码，程序将继续运行；如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。
>
>   ​		异常是使用try-except代码块处理的。
>
>   ​		try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。使用了try-except代码块时，即便出现异常，程序也将继续运行：显示你编写的友好的错误消息，而不是令用户迷惑的traceback。

### 10.3.1 处理 ZeroDivisionError 异常

>   ​		在traceback中，指出的错误ZeroDivisionError是一个异常对象。
>
>   ​		Python无法按你的要求做时，就会创建这种对象。
>
>   ​		在这种情况下，Python将停止运行程序，并指出引发了哪种异常，而我们可根据这些信息对程序进行修改。

示例：

```python
# division.py
print(5/0)
```

输出语句：

```python
Traceback (most recent call last):
  File "/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/example/division.py", line 8, in <module>
    print(5/0)
ZeroDivisionError: division by zero
```

### 10.3.2 使用 try-except 代码块

>   ​		当你认为可能发生了错误时，可编写一个try-except代码块来处理可能引发的异常。你让Python尝试运行一些代码，并告诉它如果这些代码引发了指定的异常，该怎么办。
>
>   ​		如果try代码块中的代码运行起来没有问题，Python将跳过except代码块；
>
>   ​		如果try代码块中的代码导致了错误，Python将查找这样的except代码块，并运行其中的代码，即其中指定的错误与引发的错误相同。
>
>   ​		如果try-except代码块后面还有其他代码，程序将接着运行。

示例：

```python
# division.py
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

输出语句：

```python
You can't divide by zero!
```

### 10.3.3 使用异常避免崩溃

>   ​		发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。这种情况经常会出现在要求用户提供输入的程序中；如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。
>
>   ​		程序崩溃可不好，让用户看到traceback也不是好主意。不懂技术的用户会被它们搞糊涂，而且如果用户怀有恶意，他会通过traceback获悉你不希望他知道的信息。有时候，训练有素的攻击者可根据这些信息判断出可对你的代码发起什么样的攻击。

示例：

```python
# division.py
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
		break
    second_number = input("Second number: ")
    if second_number == 'q':
		break
    answer = int(first_number) / int(second_number)
    print(answer)
```

输出语句：

```python
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
Traceback (most recent call last):
  File "/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/example/division.py", line 33, in <module>
    answer = int(first_number) / int(second_number)
ZeroDivisionError: division by zero
```

### 10.3.4 else 代码块

>   ​		try-except-else代码块的工作原理大致如下：
>
>   ​		Python尝试执行try代码块中的代码；只有可能引发异常的代码才需要放在try语句中。
>
>   ​		有时候，有一些仅在try代码块成功执行时才需要运行的代码；这些代码应放在else代码块中。
>
>   ​		except代码块告诉Python，如果它尝试运行try代码块中的代码时引发了指定的异常，该怎么办。
>
>   ​		通过预测可能发生错误的代码，可编写健壮的程序，它们即便面临无效数据或缺少资源，也能继续运行，从而能够抵御无意的用户错误和恶意的攻击。

示例：

```python
# division.py
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```

输出语句：

```python
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
You can't divide by 0!

First number: 5
Second number: 2
2.5

First number: q
```

### 10.3.5 处理 FileNotFoundError 异常

>   ​		使用文件时，一种常见的问题是找不到文件：你要查找的文件可能在其他地方、文件名可能不正确或者这个文件根本就不存在。对于所有这些情形，都可使用try-except代码块以直观的方式进行处理。
>
>   ​		如果文件不存在，这个程序什么都不做，因此错误处理代码的意义不大。

示例1：

```python
# alice.py
filename = 'alice.txt'

with open(filename) as f_obj:
    contents = f_obj.read()
```

输出语句：

```python
Traceback (most recent call last):
  File "/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/example/alice.py", line 10, in <module>
    with open(filename) as f_obj:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```

示例2：

```python
# alice.py
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
```

输出语句：

```python
Sorry, the file alice.txt does not exist.
```

### 10.3.6 分析文件

>   ​		可以分析包含整本书的文本文件。
>
>   ​		很多经典文学作品都是以简单文本文件的方式提供的，因为它们不受版权限制。
>
>   ​		本节使用的文本来自项目Gutenberg（http://gutenberg.org/），这个项目提供了一系列不受版权限制的文学作品，如果你要在编程项目中使用文学文本，这是一个很不错的资源。
>
>   
>
>   ​		方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点。
>
>   ​		使用len()来确定这个列表的长度。		

示例1：

```python
title = "Alice in Wonderland"
print(title.split())
```

输出语句：

```python
['Alice', 'in', 'Wonderland']
```

示例2：

```python
# alice.py
filename = 'alice.txt'
filepath = "/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/" + filename

try:
    with open(filepath) as f_obj:
        contents = f_obj.read()
except:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
```

输出语句：

```python
The file alice.txt has about 29461 words.
```

### 10.3.7 使用多个文件

>   ​		使用try-except代码块提供了两个重要的优点：
>
>   ​		避免让用户看到traceback；
>
>   ​		让程序能够继续分析能够找到的其他文件。
>
>   ​		如果不捕获因找不到文件而引发的FileNotFoundError异常，用户将看到完整的traceback，而程序将在引发异常后停止运行。

示例1：

```python
# word_count.py
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename
    
    try:
        with open(filepath) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
    	
filename = 'alice.txt'
count_words(filename)
```

输出语句：

```python
The file alice.txt has about 29461 words.
```

示例2：

```python
# word_count.py
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename
    
    try:
        with open(filepath) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
    	
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```

输出语句：

```python
The file alice.txt has about 29461 words.
Sorry, the file siddhartha.txt does not exist.
The file moby_dick.txt has about 215136 words.
The file little_women.txt has about 189079 words.
```

### 10.3.8 失败时一声不吭

>   ​		Python有一个pass语句，可在代码块中使用它来让Python什么都不要做。
>
>   ​		pass语句还充当了占位符，她提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些什么。

示例：

```python
# word_count.py
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    filepath = '/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_10/python_work/text_files/' + filename
    
    try:
        with open(filepath) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
    	
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```

输出语句：

```python
The file alice.txt has about 29461 words.
The file moby_dick.txt has about 215136 words.
The file little_women.txt has about 189079 words.
```

### 10.3.9 决定报告哪些错误

>   ​		在什么情况下该向用户报告错误？在什么情况下又应该在失败时一声不吭呢？
>
>   ​		如果用户知道要分析哪些文件，它们可能希望在有文件没有分析时出现一条消息，将其中的原因告诉他们。
>
>   ​		如果用户只想看到结果，而并不知道要分析哪些文件，可能就无需在有些文件不存在时告知他们。
>
>   ​		向用户显示他不想看到的信息可能会降低程度的可用性。Python的错误处理结构让你能够细致地控制与用户分享错误信息的程度，要分享多少信息由你决定。
>
>   ​		编写得很好且经过详尽测试的代码不容易出现内部错误，如语法或逻辑错误，但只要程序依赖于外部因素，如用户输入、存在指定的文件、有网络链接，就有可能出现异常。凭借经验可判断该在程序的什么地方包含异常处理块，以及出现错误时该向用户提供多少相关的信息。



