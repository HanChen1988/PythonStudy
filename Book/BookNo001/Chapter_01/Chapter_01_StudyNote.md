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

#### 1.检查是否安装了Python

>   ​		在文件夹Applications/Utilities中，选择Terminal，打开一个终端窗口；你也可以按Command+空格键，再输入terminal并按回车。
>
>   ​		为确定是否安装了Python，请执行命令python（注意，其中的p是小写的）。要检查系统是否安装了Python3，可能需要指定相应的版本。
>
>   ​		如果要退出Python并返回到终端窗口，可按Ctrl + D或执行命令exit()。

#### 2.在终端会话中运行Python代码

>   ​		在终端会话中输入如下代码行:
>
>   ​				print("Hello Python interpreter!")
>
>   ​		消息将直接打印到当前终端窗口中。别忘了，要关闭Python解释器，可按Ctrl+D或执行命令exit()。

#### 3.安装文本编辑器

>   ​		Sublime Text是一款简单的文本编辑器：它在OS X中易于安装；让你能够直接运行几乎所有程序（而无需通过终端）；使用不同的颜色来显示代码，以突出代码语法；在内嵌在Sublime Text窗口内的终端会话中运行代码，让你能够轻松地查看输出。

#### 4.配置Sublime Text使其使用Python3

>   ​		如果你启动Python终端会话时使用的命令不是python，就需要配置Sublime Text，让它知道到系统的什么地方去查找正确的Python版本。要获悉Python解释器的完整路径，请执行如下命令：
>
>   ​				$ type -a python3
>
>   ​				python3 is /usr/local/bin/python3
>
>   ​	   现在，启动Sublime Text，并选择菜单Tools$\longrightarrow$Build System$\longrightarrow$New Build System，这将打开一个新的配置文件。删除其中的所有内容，再输入如下内容：
>
>   ​				{
>
>   ​						"cmd":["/usr/local/bin/python3", "-u", "$file"],
>
>   ​				}
>
>   ​		这些代码让Sublime Text使用命令python3来运行当前打开的文件。请确保其中的路径为你在前一步使用命令type -a python3获悉的路径。将这个配置文件命令为Python3.sublime-build，并将其保存到默认目录—你选择菜单Save时Sublime Text打开的目录。

#### 5.运行Hello World程序

>   ​		为编写第一个程序，需要启动Sublime Text。
>
>   ​		接下来，创建一个用于存储项目的文件夹，并将其命名为python_work（在文件名和文件夹名中，最好使用小写字母，并使用下划线来表示空格，因为这是Python采用的命名约定）。
>
>   ​		将文件hello_world.py保存到文件夹python_work。
>
>   ​		在文件hello_world.py中保留下面一行代码：
>
>   ​				print("Hello Python world!")
>
>   ​		运行程序hello_world.py，就可选择菜单Tools$\longrightarrow$Build或按Ctrl+B来运行程序。

### 1.2.3 在Windows系统中搭建Python编程环境

>   ​		Windows系统并非都默认安装了Python，因此你可能需要下载并安装它，再下载并安装一个文本编辑器。

#### 1.安装Python

>   ​		首先，检查你的系统是否安装了Python。
>
>   ​		为此，在“开始”菜单中输入command并按回车以打开一个命令窗口；你也可按住Shift键并右击桌面，再选择“在此处打开命令窗口”。在终端窗口中输入python并按回车；如果出现了Python提示符（>>>），就说明你的系统安装了Python。然而，你也可能会看到一条错误消息，指出python是无法识别的命令。
>
>   ​	   没有安装python，请访问[python官网](http://python.org/downloads)。你将看到两个按钮，分别用于下载Python3和Python2。单击用于下载Python3的按钮，这会根据你的系统自动下载正确的安装程序。下载安装程序后，运行它。请务必选中复选框Add Python to PATH，让你能够更轻松地配置系统。

#### 2.启动Python终端会话

>   ​		通过配置系统，让其能够在终端会话中运行Python，可简化文本编辑器的配置工作。打开一个命令窗口，并在其中执行命令python。如果出现了Python提示符（>>>），就说明Windows找到了你刚安装的Python版本。
>
>   ​			C:\>python
>
>   ​			Python 3.5.0（v3.5.0:374f501f4567,Sep 13 2015, 22:15:05）[MSC v.1900 32 bit]
>
>   ​			（Intel）] on win32
>
>   ​			Type "help"，"copyright"，"credits" or "license" for more information.
>
>   ​		   >>>

#### 3.在终端会话中运行Python

>   ​		在Python会话中执行下面的命令，并确认看到了输出"Hello Python world!"。
>
>   ​				>>> print("Hello Python world!")
>
>   ​				Hello Python world!
>
>   ​				>>>
>
>   ​		每当要运行Python代码片段时，都请打开一个命令窗口并启动Python终端会话。要关闭该终端会话，可按Ctrl+Z，在按回车键，也可执行命令exit()。

#### 4.安装文本编辑器

>   ​		Geany是一款简单的文本编辑器：它易于安装；让你能够直接运行几乎所有的程序（而无需通过终端）；使用不同的颜色来显示代码，以突出代码语法；在终端窗口中运行代码，让你能够习惯使用终端。
>
>   ​		要下载Window Geany安装程序，可访问[Geany官网](http://geany.org/)，单击Download下的Releases，找到安装程序geany-1.25_setup.exe或类似的文件。下载安装程序后，运行它并接受所有默认设置。

#### 5.配置Geany

>   ​		要配置Geany，请选择菜单Build$\longrightarrow$Set Build Commands；你将看到文字Compile和Execute，它们旁边都有一个命令。默认情况下，编译命令和执行命令的开头都是python，但Geany不知道命令python存储在系统的什么地方，因此你需要在其中添加你在终端会话中使用的路径。
>
>   ​		为此，在编译命令和执行命令中，加上命令python所在的驱动器和文件夹。其中编译命令应类似于下面这样：
>
>   ​				C:\Python35\python -m py_compile "%f"
>
>   ​		在你的系统中，路径可能稍有不同，但请务必确保空格和大小写与这里显示的一致。
>
>   ​		执行命令应类似于下面这样：
>
>   ​				C:\Python35\python "%f"
>
>   ​		同样，指定执行命令时，务必确保空格和大小写与这里显示的一致。

#### 6.运行Hello World程序

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

## 1.3 解决安装问题

>   ​		如果你按前面的步骤做，应该能够成功地搭建编程环境。但如果你始终无法运行程序hello_world.py，可尝试如下几个解决方案。
>
>   ​		不要担心这会打扰经验丰富的程序员。每个程序员都遇到过问题，而大多数程序员都会乐意帮助你正确地设置系统。只要能清晰地说明你要做什么、尝试了哪些方法及其结果，就很可能有人能够帮到你。

### 解决方案

-   程序存在严重的错误时，Python将显示traceback。

    >   ​		Python会仔细研究文件，试图找出其中的问题。traceback可能会提供线索，让你知道是什么问题让程序无法运行。

-   离开计算机，先休息一会儿，再尝试。

    >   ​		别忘了，在编程中，语法非常重要，即便是少一个冒号、引号不匹配或括号不匹配，都可能导致程序无法正确地运行。

-   推倒重来。

    >   ​		你也许不需要把一切都推倒重来，但将文件hello_world.py删除并重新创建它也许是合理的选择。

-   让别人在你的计算机或其他计算机上按本章的步骤重做一遍，并仔细观察。

    >   ​		你可能遗漏了一小步，而别人刚好没有遗漏。

-   请懂Python的人帮忙。

    >   ​		当你有这样的想法时，可能会发现在你认识的人当中就有人使用Python。 

-   本章的安装说明在本书主页上也可以找到：ituring.cn/book/1861。对你来说，在线版也许更合适。

-   到网上寻求帮助。

    >   ​		在线资源，如论坛或在线聊天网站，你可以前往这些地方，请求解决过你面临的问题的人提供解决方案。

## 1.4 从终端运行Python程序

>   ​		你编写的大多数程序都将直接在文本编辑器中运行，但有时候，从终端运行程序很有用。例如，你可能想直接运行既有的程序。

### 1.4.1 在Linux和OS X系统中从终端运行Python程序

>   ​		在Linux和OS X系统中，从终端运行Python程序的方式相同。
>
>   ​		在终端会话中，可使用终端命令cd（表示切换目录，change directory）在文件系统中导航。命令ls（list的简写）显示当前目录中所有未隐藏的文件。
>
>   ​		为运行程序hello_world.py，请打开一个新的终端窗口，并执行下面的命令：
>
>   ​				~$ cd Desktop/python_work/
>
>   ​				~/Desktop/python_work$ ls
>
>   ​				hello_world.py
>
>   ​				~/Desktop/python_work$ python3 hello_world.py
>
>   ​				Hello Python world!
>
>   ​		这里使用了命令cd来切换到文件夹Desktop/python_work。接下来，使用命令ls来确认这个文件夹中包含文件hello_world.py。最后，使用命令python3 hello_world.py来运行这个文件。

### 1.4.2 在Windows系统中从终端运行Python程序

>   ​		在命令窗口中，要在文件系统中导航，可使用终端命令cd；要列出当前目录中的所有文件，可使用命令dir（表示目录，directory）。
>
>   ​		为运行程序hello_world.py，请打开一个新的终端窗口，并执行下面的命令：
>
>   ​				C:\\> cd Desktop\python_work
>
>   ​				C:\\Desktop\\python_work> dir
>
>   ​				hello_world.py
>
>   ​				C:\\Desktop\python_work> python3 hello_world.py
>
>   ​				Hello Python world!
>
>   ​		这里使用了命令cd来切换到文件夹Desktop\\python_work。接下来，使用命令dir来确认这个文件夹中包含文件hello_world.py。最后，使用命令python3 hello_world.py来运行这个文件。

## 1.5 小结

>   ​		在本章中，你大致了解了Python，并在自己的系统中安装了Python。你还安装了一个文本编辑器，以简化Python代码的编写工作。你学习了如何在终端会话中运行Python代码片段，并运行了第一个货真价实的程序—hello_world.py。你还大致了解了如何解决安装问题。

