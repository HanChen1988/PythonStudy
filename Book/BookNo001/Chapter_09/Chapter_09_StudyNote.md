# 第9章：类

>   ​		面向对象编程是最有效的软件编写方法之一。在面向对象编程中，你编写表示现实世界中的事物和情景的类，并基于这些类来创建对象。编写类时，你定义一大类对象都有的通用行为。基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性。使用面向对象编程可模拟现实情景，其逼真程度达到了令你惊讶的地步。
>
>   ​		根据类来创建对象被称为实例化，这让你能够使用类的实例。
>
>   ​		理解面向对象编程有助于你像程序员那样看世界，还可以帮助你真正明白自己编写的代码；不仅是各行代码的作用，还有代码背后更宏大的概念。了解类背后的概念可培养逻辑思维，让你能够通过编写程序来解决遇到的几乎任何问题。
>
>   ​		随着面临的挑战日益严峻，类还能让你以及与你合作的其他程序员的生活更轻松。如果你与其他程序员基于同样的逻辑来编写代码，你们就能明白对方所做的工作；你编写的程序将能被众多合作者所理解，每个人都能事半功倍。

## 9.1 创建和使用类

### 9.1.1 创建 Dog 类

示例：

```python
# dog.py
class Dog():
    """一次模拟小狗的简单尝试"""
    
    def __init__(self, name, age):
        "初始化属性name和age"
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
```

#### 1.方法\__init__()

>   ​		类中的函数称为方法。
>
>   ​		方法\__init__()是一个特殊的方法，每当你根据类创建新实例时，Python都会自动运行它。在这个方法名中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。
>
>   ​		在这个方法的定义中，形参self必不可少，还必须位于其他形参的前面。
>
>   ​		为何必须在方法定义中包含形参self呢？
>
>   ​				因为Python调用这个\__init()__方法来创建类实例时，将自动传入实参self。每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
>
>   ​		以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量。像这样可通过实例访问的变量称为属性。

#### 2.在Python 2.7中创建类

>   ​		在Python 2.7中创建类时，需要做细微的修改—在括号内包含单词object:
>
>   ​				class ClassName(object):
>
>   ​						--snip--
>
>   ​		这让Python 2.7类的行为更像Python 3类，从而简化了你的工作。

### 9.1.2 根据类创建实例

>   ​		命名约定：我们通常可以认为首字母大写的名称指的是类，而小写的名称指的是根据类创建的实例。

示例：

```python
class Dog():
    """一次模拟小狗的简单尝试"""
    
    def __init__(self, name, age):
        "初始化属性name和age"
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
              
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
```

输出语句：

```python
My dog's name is Willie.
My dog is 6 years old.
```

#### 1.访问属性

>   ​		要访问实例的属性，可使用句点表示法。

#### 2.调用方法

>​		要调用方法，可指定实例的名称和要调用的方法，并用句点分隔它们。

示例：

```python
class Dog():
    """一次模拟小狗的简单尝试"""
    
    def __init__(self, name, age):
        "初始化属性name和age"
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
              
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()
```

输出语句：

```python
Willie is now sitting.
Willie rolled over!
```

#### 3.创建多个实例

>   ​		可按需求根据一个类创建任意数量的实例，条件是将每个实例都存储在不同的变量中，或占用列表或字典的不同位置。

示例：

```python
class Dog():
    """一次模拟小狗的简单尝试"""
    
    def __init__(self, name, age):
        "初始化属性name和age"
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
              
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
              
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
```

输出语句：

```python
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.
```

## 9.2 使用类和实例

