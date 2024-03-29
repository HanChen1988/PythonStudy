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

>   ​		你可以使用类来模拟现实世界中的很多情景。类编写好后，你的大部分时间都将花在使用根据类创建的实例上。你需要执行的一个重要任务是修改实例的属性。你可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。

### 9.2.1 Car类

示例：

```python
# car.py
class Car():
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
```

输出语句：

```python
2016 Audi A4
```

### 9.2.2 给属性指定默认值

>   ​		类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法\__init__()内指定这种初始值是可行的；如果你对某个属性这样做了，就无需包含为它提供初始值的形参。

示例：

```python
class Car():
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()      
```

输出语句：

```python
2016 Audi A4
This car has 0 miles on it.
```

### 9.2.3 修改属性的值

>   ​		可以以三种不同的方式修改属性的值：直接通过实例进行修改；通过方法进行设置；通过方法进行递增（增加特定的值）。

#### 1.直接修改属性的值

>   ​		要修改属性的值，最简单的方式是通过实例直接访问它。

示例：

```python
class Car():
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

输出语句：

```python
2016 Audi A4
This car has 23 miles on it.
```

#### 2.通过方法修改属性的值

>   ​		如果有替你更新属性的方法，将大有裨益。这样，你就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新。

示例1：

```python
class Car():
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
```

输出语句：

```python
2016 Audi A4
This car has 23 miles on it.
```

示例2：

```python
class Car():
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
        	print("You can't roll back an odometer!")
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
```

输出语句：

```python
2016 Audi A4
This car has 23 miles on it.
```

#### 3.通过方法对属性的值进行递增

>   ​		有时候需要将属性值递增特定的量，而不是将其设置为全新的值。
>
>   ​		注意：你可以使用方法来控制用户修改属性值的方式，但能够访问程序的人都可以通过直接访问属性来将里程表修改为任何值。要确保安全，除了进行类似于前面的基本检查外，还需特别注意细节。

示例：

```python
class Car():
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
        	print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        
my_new_car = Car('subaru', 'outback', 2013)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()
```

输出语句：

```python
2013 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.
```

## 9.3 继承

>   ​		编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

### 9.3.1 子类的方法\__init__()

>   ​		创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。为此，子类的方法\__init__()需要父类施以援手。
>
>   ​		创建子类时，父类必须包含在当前文件中，且位于子类前面。
>
>   ​		super()是一个特殊函数，帮助Python将父类和子类关联起来。父类也称为超类（superclass），名称super因此而得名。

示例：

```python
# electric_car.py
class Car():
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
        	print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        

class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

输出语句：

```python
2016 Tesla Model S
```

### 9.3.2 Python 2.7 中的继承

>​		在Python 2.7中，继承语法稍有不同。
>
>​		函数super()需要两个实参：子类名和对象self。为帮助Python将父类和子类关联起来，这些实参必不可少。另外，在Python 2.7中使用继承时，务必在定义父类时在括号内指定object。

示例：

```python
# electric_car.py
class Car(object):
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
        	print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        

class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super(ElectricCar, self).__init__(make, model, year)
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

输出语句：

```python
2016 Tesla Model S
```

### 9.3.3 给子类定义属性和方法

>   ​		让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。

示例：

```python
# electric_car.py
class Car(object):
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
        	print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        

class ElectricCar(Car):
    """
    电动汽车的独特之处
    初始化父类的属性，再初始化电动汽车特有的属性
    """
    
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super(ElectricCar, self).__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

输出语句：

```python
2016 Tesla Model S
This car has a 70-kWh battery.
```

### 9.3.4 重写父类的方法

>   ​		对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。

示例：

```python
# 假设Car类有一个名为fill_gas_tank()的方法。
class ElectricCar(Car):
    --snip--
    
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
```

### 9.3.5 将实例用作属性

>   ​		使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来越长。在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。你可以将大型类拆分成多个协同工作的小类。

示例1：

```python
# electric_car.py
class Car(object):
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
        	print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    """
    电动汽车的独特之处
    初始化父类的属性，再初始化电动汽车特有的属性
    """
    
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```

输出语句：

```python
2016 Tesla Model S
This car has a 70-kWh battery.
```

示例2：

```python
# electric_car.py
class Car(object):
    """一次模拟汽车的简单尝试"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
        	print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """
    电动汽车的独特之处
    初始化父类的属性，再初始化电动汽车特有的属性
    """
    
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

输出语句：

```python
2016 Tesla Model S
This car has a 70-kWh battery.
This car can go approximately 240 miles on a full charge.
```

### 9.3.6 模拟实物

>   ​		解决问题时，你从较高的逻辑层面（而不是语法层面）考虑；你考虑的不是Python，而是如何使用代码来表示实物。到达这种境界后，你经常会发现，现实世界的建模方法并没有对错之分。有些方法的效率更高，但要找出效率最高的表示法，需要经过一定的实践。只要代码像你希望的那样运行，就说明你做得很好！即便你发现自己不得不多次尝试使用不同的方法来重写类，也不必气馁；要编写出高效、准确的代码，都得经过这样的过程。

## 9.4 导入类

>   ​		随着你不断地给类添加功能，文件可能变得很长，即便你妥善地使用了继承亦如此。为遵循Python的总体理念，应让文件尽可能整洁。为在这方面提供帮助，Python允许你将类存储在模块中，然后在主程序中导入所需的模块。
>
>   ​		导入类是一种有效的编程方式。通过将导入类移到一个模块中，并导入该模块，你依然可以使用其所有功能，但主程序文件变得整洁而易于阅读了。这还能让你将大部分逻辑存储在独立的文件中；确实类像你希望的那样工作后，你就可以不管这些文件，而专注于主程序的高级逻辑了。

### 9.4.1 导入单个类

示例：

```python
# my_car.py
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

输出语句：

```python
2016 Audi A4
This car has 23 miles on it.
```

### 9.4.2 在一个模块中存储多个类

>   ​		虽然同一个模块中的类之间应存在某种相关性，但可根据需要在一个模块中存储任意数量的类。

示例：

```python
# my_electric_car.py
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

输出语句：

```python
2016 Tesla Model S
This car has a 70-kWh battery.
This car can go approximately 240 miles on a full charge.
```

### 9.4.3 从一个模块中导入多个类

>​		可根据需要在程序文件中导入任意数量的类。

示例：

```python
# my_cars.py
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

输出语句：

```python
2016 Volkswagen Beetle
2016 Tesla Roadster
```

### 9.4.4 导入整个模块

>   ​		还可以导入整个模块，再使用句点表示法访问需要的类。这种导入方法很简单，代码也易于阅读。由于创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突。

示例：

```python
# my_cars.py
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

输出语句：

```python
2016 Volkswagen Beetle
2016 Tesla Roadster
```

### 9.4.5 导入模块中的所有类

>   ​		要导入模块中的每个类，可使用下面的语法：
>
>   ​				from module_name import *
>
>   ​		不推荐使用这种导入方式，其原因有二。首先，如果只要看一下文件开头的import语句，就能清楚地知道程序使用了哪些类，将大有裨益；但这种导入方式没有明确地指出你使用了模块中的哪些类。这种导入方式还可能引发名称方面的困惑。如果你不小心导入了一个与程序文件中其他东西同名的类，将引发难以诊断的错误。这里之所以介绍这种导入方式，是因为虽然不推荐使用这种方式，但你可能会在别人编写的代码中见到它。
>
>   ​		需要从一个模块中导入很多类时，最好导入整个模块，并使用module_name.class_name语法来访问类。这样做时，虽然文件开头并没有列出用到的所有类，但你清楚地知道在程序的那些地方使用了导入的模块；你还避免了导入模块中的每个类可能引发的名称冲突。

### 9.4.6 在一个模块中导入另一个模块

>   ​		有时候，需要将类分散到多个模块中，以免模块太大，或在同一个模块中存储不相关的类。将类存储在多个模块中时，你可能会发现一个模块中的类依赖于另一个模块中的类。在这种情况下，可在前一个模块中导入必要的类。

示例：

```python
# my_cars.py
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

输出语句：

```python
2016 Volkswagen Beetle
2016 Tesla Roadster
```

### 9.4.7 自定义工作流程

>   ​		正如你看到的，在组织大型项目的代码方面，Python提供了很多选项。熟悉所有这些选项很重要，这样你才能确定哪种项目组织方式是最佳的，并能理解别人开发的项目。
>
>   ​		一开始应让代码结构尽可能简单。先尽可能在一个文件中完成所有的工作，确定一切都能正确运行后，再将类移到独立的模块中。如果你喜欢模块和文件的交互方式，可在项目开始时就尝试将类存储到模块中。先找出让你能够编写出可行代码的方式，再尝试让代码更为组织有序。

## 9.5 Python标准库

>   ​		Python标准库是一组模块，安装的Python都包含它。你现在对类的工作原理已有大致的了解，可以开始使用其他程序员编写好的模块了。可使用标准库中的任何函数和类，为此只需在程序开头包含一条简单的import语句。
>
>   ​		字典让你能够将信息关联起来，但它们不记录你添加键-值对的顺序。要创建字典并记录其中的键-值对的添加顺序，可使用模块collections中的OrderedDict类。OrderedDict实例的行为几乎与字典相同，区别只在与记录了键-值对的添加顺序。
>
>   ​		这是一个很不错的类，它兼具列表和字典的主要优点（在将信息关联起来的同时保留原来的顺序）。等你开始对关心的现实情形建模时，可能会发现有序字典正好能够满足需求。随着你对标准库的了解越来越深入，将熟悉大量可帮助你处理常见情形的模块。

示例：

```python
# favorite_languages.py
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
         language.title() + ".")
```

输出语句：

```python
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
```

## 9.6 类编码风格

>​		你必须熟悉有些与类相关的编码风格问题，在你编写的程序较复杂时尤其如此。
>
>​		类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加上下划线。
>
>​		对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
>
>​		可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。
>
>​		需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，再添加一个空行，然后编写导入你自己编写的模块的import语句。在包含多条import语句的程序中，这种做法让人更容易明白程序使用的各个模块都来自何方。

## 9.7 小结

>   ​		在本章中，你学习了：如何编写类；如何使用属性在类中存储信息，以及如何编写方法，以让类具备所需的行为；如何编写方法\__init__()，以便根据类创建包含所需属性的实例。你见识了如何修改实例的属性—包括直接修改以及通过方法进行修改。你还了解了：使用继承可简化相关类的创建工作；将一个类的实例用作另一个类的属性可让类更简洁。
>
>   ​		你了解到，通过将类存储在模块中，并在需要使用这些类的文件中导入它们，可让项目组织有序。你学习了Python标准库，并见识了一个使用模块collections中的OrderedDict类的示例。最后，你学习了编写类时应遵循的Python约定。
