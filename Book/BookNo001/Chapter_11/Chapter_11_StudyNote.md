# 第11章：测试代码

>   ​		编写函数或类时，还可为其编写测试。通过测试，可确定代码面对各种输入都能够按要求的那样工作。测试让你信心满满，深信即便有更多的人使用你的程序，它也能正确地工作。在程序中添加新代码时，你也可以对其进行测试，确认它们不会破坏程序既有的行为。程序员都会犯错，因此每个程序员都必须经常测试其代码，在用户发现问题前找出它们。
>
>   ​		在本章中，你将学习如何使用Python模块unittest中的工具来测试代码。你将学习编写测试用例，核实一系列输入都将得到预期的输出。你将看到测试通过了是什么样子，测试未通过又是什么样子，还将知道测试未通过如何有助于改进代码。你将学习如何测试函数和类，并将知道该位项目编写多少个测试。

## 11.1 测试函数

>   ​		要学习测试，得有要测试的代码。
>
>   ​		函数 get_formatted_name() 将名和姓合并成姓名，在名和姓之间加上一个空格，并将它们的首字母都大写，再返回结果。为核实get_formatted_name()像期望的那样工作，我们来编写一个使用这个函数的程序。程序names.py让用户输入名和姓，并显示整洁的全名。
>
>   ​		Python提供了一种自动测试函数输出的高效方式。倘若我们对get_formatted_name()进行自动测试，就能始终信心满满，确信给这个函数提供我们测试过的姓名时，它都能正确地工作。

示例1：

```python
# name_function.py
def get_formatted_name(first, last):
    """生成整洁的姓名"""
    full_name = first + ' ' + last
    return full_name.title()
```

输出语句：

```python
```

示例2：

```python
# names.py
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
	if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".") 
```

输出语句：

```python
Enter 'q' at any time to quit.

Please give me a first name: janis
Please give me a last name: joplin
	Neatly formatted name: Janis Joplin.

Please give me a first name: bob
Please give me a last name: dylan
	Neatly formatted name: Bob Dylan.

Please give me a first name: q
```

### 11.1.1 单元测试和测试用例

>   ​		Python标准库中的模块unittest提供了代码测试工具。
>
>   ​		单元测试用于核实函数的某个方面没有问题；
>
>   ​		测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。
>
>   ​		良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。
>
>   ​		全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。对于大型项目，要实现全覆盖可能很难。通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。

### 11.1.2 可通过的测试

>   ​		创建测试用例的语法需要一段时间才能习惯，但测试用例创建后，再添加针对函数的单元测试就很简单了。
>
>   ​		要为函数编写测试用例，可先导入模块unittest以及要测试的函数，再创建一个继承unittest.TestCase的类，并编写一系列方法对函数行为的不同方面进行测试。
>
>   
>
>   ​		类命名包含字样Test，类必须继承unittest.TestCase类，这样Python才知道如何运行你编写的测试。
>
>   ​		方法名必须以test_打头。
>
>   ​		使用了unittest类最有用的功能之一：一个断言方法。断言方法assertEqual(a, b)用来核实得到的结果是否与期望的结果一致。
>
>   ​		代码行unittest.main()让Python运行这个文件中的测试。
>
>   ​		
>
>   ​		第1行的句点表明有一个测试通过了。
>
>   ​		接下来的一行指出Python运行了一个测试，消耗的时间不到0.001秒。
>
>   ​		最后的OK表明该测试用例中的所有单元测试都通过了。

示例：

```python
# test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
```

输出语句：

```python
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

### 11.1.3 不能通过的测试

>   ​		第1行输出只有一个字母E，它指出测试用例中有一个单元测试导致了错误。
>
>   ​		接下来，我们看到NamesTestCase中的test_first_last_name()导致了错误。测试用例包含众多单元测试时，知道哪个测试未通过至关重要。
>
>   ​		接下来，我们看到了一个标准的traceback，它指出函数调用get_formatted_name('janis', 'joplin')有问题，因为它缺少一个必不可少的位置实参。
>
>   ​		接下来，我们还看到运行了一个单元测试。
>
>   ​		最后，还看到了一条消息，它指出整个测试用例都未通过，因为运行该测试用例时发生了一个错误。

示例1：

```python
# name_function.py
def get_formatted_name(first, middle, last):
    """生成整洁的姓名"""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
```

输出语句：

```python
```

示例2：

```python
# test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
```

输出语句：

```python
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
能够正确地处理像Janis Joplin这样的姓名吗？
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/hanchen/Desktop/PythonStudy/Book/BookNo001/Chapter_11/python_work/example/test_name_function.py", line 17, in test_first_last_name
    formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### 11.1.4 测试未通过时怎么办

>   ​		测试未通过时怎么办呢？
>
>   ​		测试未通过时，不要修改测试，而应修复导致测试不能通过的代码：检查刚对函数所做的修改，找出导致函数行为不符合预期的修改。
>
>   
>
>   ​		要将中间名设置为可选的，可在函数定义中将形参middle移到形参列表末尾，并将其默认值指定为一个空字符串。
>
>   ​		我们还要添加一个if测试，以便根据是否提供了中间名相应地创建姓名。

示例1：

```python
# name_function.py
def get_formatted_name(first, last, middle=''):
    """生成整洁的姓名"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
```

输出语句：

```python
```

示例2：

```python
# test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
```

输出语句：

```python
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

### 11.1.5 添加新测试

示例：

```python
# test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
        	'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
```

输出语句：

```python
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## 11.2 测试类

>   ​		很多程序中都会用到类，因此能够证明你的类能够正确地工作会大有裨益。
>
>   ​		如果针对类的测试通过了，你就能确信对类所做的改进没有意外地破坏其原有的行为。

### 11.2.1 各种断言方法

>   ​		Python在unittest.TestCase类中提供了很多断言方法。
>
>   ​		断言方法检查你认为应该满足的条件是否确实满足。
>
>   ​		如果该条件确实满足，你对程序行为的假设就得到了确认，你就可以确信其中没有错误。
>
>   ​		如果你认为应该满足的条件实际上并不满足，Python将引发异常。
>
>   ​		使用断言方法可核实返回的值等于或不等于预期的值、返回的值为True或False。

<center>表11-1 unittest Module中的断言方法</center>

|          方法           | 用途               |
| :---------------------: | :----------------- |
|    assertEqual(a, b)    | 核实a == b         |
|  assertNotEqual(a, b)   | 核实a != b         |
|      assertTrue(x)      | 核实x为True        |
|     assertFalse(x)      | 核实x为False       |
|  assertIn(item, list)   | 核实item在list中   |
| assertNotIn(item, list) | 核实item不在list中 |

### 11.2.2 一个要测试的类

示例1：

```python
# survey.py
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
        
    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)
        
    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
```

输出语句：

```python
```

示例2：

```python
# language_survey.py
from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```

输出语句：

```python
What language did you first learn to speak?
Enter 'q' at any time to quit.

Language: English
Language: Spanish
Language: English
Language: Mandarin
Language: q

Thank you to everyone who participated in the survey!
Survey results:
- English
- Spanish
- English
- Mandarin
```

### 11.2.3 测试 AnonymousSurvey 类

示例1：

```python
# test_survey.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        
        self.assertIn('English', my_survey.responses)

unittest.main()
```

输出语句：

```python
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

示例2：

```python
# test_survey.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        
        self.assertIn('English', my_survey.responses)
        
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()
```

输出语句：

```python
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

### 11.2.4 方法 setUp()

>   ​		unittest.TestCase类包含方法setUp()，让我们只需创建对象一次，并在每个测试方法中使用它们。
>
>   ​		如果你在TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以test_打头的方法。
>
>   
>
>   ​		测试自己编写的类时，方法setUp()让测试方法编写起来更容易：可在setUp()方法中创建一系列实例并设置它们的属性，再在测试方法中直接使用这些实例。相比于在每个测试方法中都创建实例并设置其属性，这要容易得多。
>
>   
>
>   ​		注意：运行测试用例时，每完成一个单元测试，Python都打印一个字符：测试通过时打印一个句点；测试引发错误时打印一个E；测试导致断言失败时打印一个F。
>
>   ​		这就是你运行测试用例时，在输出的第一行中看到的句点和字符数量各不相同的原因。
>
>   ​		如果测试用例包含很多单元测试，需要运行很长时间，就可通过观察这些结果来获悉有多少个测试通过了。

示例：

```python
# test_survey.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        
    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
```

输出语句：

```python
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```


## 11.3 小结

>   ​		在本章中，你学习了：如何使用模块unittest中的工具来为函数和类编写测试；如何编写继承unittest.TestCase的类，以及如何编写测试方法，以核实函数和类的行为符合预期；如何使用方法setUp()来根据类高效地创建实例并设置其属性，以便在类的所有测试方法中都可使用它们。
>
>   ​		测试是很多初学者都不熟悉的主题。作为初学者，并非必须为你尝试的所有项目编写测试；但参与工作量较大的项目时，你应对自己编写的函数和类的重要行为进行测试。这样你就能够更加确定自己所做的工作不会破坏项目的其他部分，你就能够随心所欲地改进既有代码了。如果不小心破坏了原来的功能，你马上就会知道，从而能够轻松地修复问题。相比于等到不满意的用户报告bug后再采取措施，在测试未通过时采取措施要容易得多。
>
>   ​		如果你在项目中包含了初步测试，其他程序员将更敬佩你，他们将能够更得心应手地尝试使用你编写的代码，也更愿意与你合作开发项目。如果你要跟其他程序员开发的项目共享代码，就必须证明你编写的代码通过了既有测试，通常还需要为你添加的新行为编写测试。
>
>   ​		请通过多开展测试来熟悉代码测试过程。对于自己编写的函数和类，请编写针对其重要行为的测试，但在项目早期，不要试图去编写全覆盖的测试用例，除非有充分的理由这样做。		
