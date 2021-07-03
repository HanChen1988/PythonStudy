# 第1章：起步

>   ​		在本章中，你将运行自己的第一个程序—hello_world.py。为此，你首先需要检查自己的计算机是否安装了Python；如果没有安装，你需要安装它。你还要安装一个文本编辑器，用于编写和运行Python程序。你输入Python代码时，这个文本编辑器能够识别它们并突出显示不同的部分，让你能够轻松地了解代码的结构。

## 1.1 搭建编程环境

>   ​		在不同的操作系统中，Python存在细微的差别。
>
>   ​		这里将介绍大家使用的两个主要的Python版本，并简要介绍Python的安装步骤。

### 1.1.1 Python2和Python3

>   ​		注意：如果你的系统安装的是Python3，那么有些使用Python2编写的代码可能无法正确地运行。

### 1.1.2 运行Python代码片段

>   ​		Python自带了一个在终端窗口中运行的解释器，让你无需保存并运行整个程序就能尝试运行Python代码片段。
>
>   ​		本书将以如下方式列出代码片段：
>
>   ​		>>> print("Hello Python interpreter!")

### 1.1.3 Hello World程序

>   ​		要使用Python来编写这种Hello World程序，只需一行代码：
>
>   ​		print("Hello world!")

## 1.2 在不同操作系统中搭建Python编程环境

>   ​		Python是一种跨平台的编程语言，这意味着它能够运行在所有主要的操作系统中。在所有安装了Python的现代计算机上，都能够运行你编写的任何Python程序。然而，在不同的操作系统中，安装Python的方法存在细微的差别。

### 1.2.1 在Linux系统中搭建Python编程环境

>   ​		Linux系统是为编程而设计的，因此在大多数Linux计算机中，都默认安装了Python。

#### 1.检查Python版本

>   ​		在你的系统中运行应用程序Terminal（如果你使用的是Ubuntu，可按Ctrl + Alt + T），打开一个终端窗口。
>
>   ​		为确定是否安装了Python，执行命令python（请注意，其中的p是小写的）。要检查系统是否安装了Python3，可能需要指定相应的版本。
>
>   ​		如果要退出Python并返回到终端窗口，可按Ctrl + D或执行命令exit()。

#### 2.安装文本编辑器

>   ​		Geany是一款简单的文本编辑器：它易于安装；让你能够直接运行几乎所有的程序（而无需通过终端来运行）；使用不同的颜色来显示代码，以突出代码语法；在终端窗口中运行代码，让你能够习惯使用终端。
>
>   ​		在大多数Linux系统中，都只需执行一个命令就可以安装Geany:
>
>   ​		$ sudo apt-get install geany
>
>   ​		如果这个命令不管用，请参阅[安装说明](http://geany.org/Download/ThirdPartyPackages/)。

#### 3.运行Hello World程序

>   ​		为编写第一个程序，需要启动Geany。
>
>   ​		接下来，创建一个用于存储项目的文件夹，并将其命名为python_work（在文件名和文件夹名中，最好使用小写字母，并使用下划线来表示空格，因为这是Python采用的命名约定）。
>
>   ​		将文件hello_world.py保存到文件夹python_work。
>
>   ​		在文件hello_world.py中保留下面一行代码：
>
>   ​				print("Hello Python world!")
>
>   ​		运行程序hello_world.py。

#### 4.在终端会话中运行Python代码

>   ​		你可以打开一个终端窗口并执行命令python或python3，在尝试运行Python代码片段。

### 1.2.2 在OS X系统中搭建Python编程环境

>   ​		大多数OS X系统都默认安装了Python。确定安装了Python后，你还需安装一个文本编辑器，并确保其配置正确无误。

