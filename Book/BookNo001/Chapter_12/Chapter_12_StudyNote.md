# 第12章：武装飞船

>   ​		我们将使用Pygame，这是一组功能强大而有趣的模块，可用于管理图形、动画乃至声音，让你能够更轻松地开发复杂的游戏。通过使用Pygame来处理在屏幕上绘制图像等任务，你不用考虑众多烦琐而艰难的编程工作，而是将重点放在程序的高级逻辑上。
>
>   ​		在本章中，你将安装Pygame，再创建一艘能够根据用户输入而左右移动和射击的飞船。在接下来的两章中，你将创建一群作为射杀目标的外星人，并做其他的改进，如限制可供玩家使用的飞船数以及添加记分牌。
>
>   ​		从本章开始，你还将学习管理包含多个文件的项目。我们将重构很多代码，以提高代码的效率，并管理文件的内容，以确保项目组织有序。
>
>   ​		创建游戏是趣学语言的理想方式。看别人玩你编写的游戏让你很有满足感，而编写简单的游戏有助于你明白专业级游戏是怎么编写出来的。
>
>   ​		注意：游戏《外星人入侵》将包含很多不同的文件，因此请在你的系统中新建一个文件夹，并将其命名为alien_invasion。请务必将这个项目的所有文件都存储到这个文件夹中，这样相关的import语句才能正确地工作。		

## 12.1 规划项目

>   ​		开发大型项目时，做好规划后再动手编写项目很重要。规划可确保你不偏离轨道，从而提高项目成功的可能性。
>
>   ​		下面来编写有关游戏《外星人入侵》的描述，其中虽然没有涵盖这款游戏的所有细节，但能让你清楚地知道该如何动手开发它。
>
>   ​				在游戏《外星人入侵》中，玩家控制着一艘最初出现在屏幕底部中央的飞船。玩家可以使用箭头键左右移动飞船，还可使用空格键进行射击。游戏开始时，一群外星人出现在天空中，他们在屏幕中向下移动。玩家的任务是射杀这些外		星人。玩家将所有外星人都消灭干净后，将出现一群新的外星人，他们移动的速度更快。只要有外星人撞到了玩家的飞船或达到了屏幕底部，玩家就损失一艘飞船。玩家损失三艘飞船后，游戏结束。
>
>   ​		在第一个开发阶段，我们将创建一艘可左右移动的飞船，这艘飞船在用户按空格键时能够开火。设置好这种行为后，我们就能够将注意力转向外星人，并提高这款游戏的可玩性。

## 12.2 安装 Pygame

>   ​		开始编码前，先来安装Pygame。
>
>   ​		下面介绍如何在Linux、OS X和Microsoft Windows中安装Pygame。
>
>   ​		如果你使用的是Linux系统和Python3，或者是OS X系统，就需要使用pip来安装Pygame。pip是一个负责为你下载并安装Python包的程序。
>
>   ​		如果你使用的是LInux系统和Python2.7，或者是Windows系统，就无需使用pip来安装Pygame。

### 12.2.1 使用 pip 安装 Python 包

>   ​		大多数较新的Python版本都自带pip，因此首先可检查系统是否已经安装了pip。在Python 3中，pip有时被称为pip3。

#### 1.在Linux和OS X系统中检查是否安装了pip

>   ​		打开一个终端窗口，并执行如下命令：
>
>   ​		$ pip --version
>
>   ​		pip 7.0.3 from /usr/local/lib/python3.5/dist-packages（python 3.5）
>
>   ​		$
>
>   ​		如果出现了错误信息，请尝试将pip替换为pip3。
>
>   ​		如果这两个版本都没有安装到你的系统中，请调到“安装pip”。

#### 2.在Windows系统中检查是否安装了pip

>   ​		打开一个终端窗口，并执行如下命令：
>
>   ​		> python -m pip --version
>
>   ​		pip 7.0.3 from C:\Python35\lib\site-packages（python 3.5）
>
>   ​		>
>
>   ​		如果出现了错误信息，请尝试将pip替换为pip3。
>
>   ​		如果执行这两个命令时都出现错误信息，请跳到“安装pip”。

#### 3.安装pip

>   ​		要安装pip，请访问https://bootstrap.pypa.io/get-pip.py。如果出现对话框，请选择保存文件；如果get-pip.py的代码出现在浏览器中，请将这些代码复制并粘贴到文本编辑器中，再将文件保存为get-pip.py。将get-pip.py保存到计算机中后，你需要以管理员身份运行它，因为pip将在你的系统中安装新包。
>
>   ​		注意：如果你找不到get-pip.py，请访问https://pip.pypa.io/，单击左边面板中的Installation，再单击中间窗口中的连接get-pip.py。

#### 4.在Linux和OS X系统中安装pip

>   ​		使用下面的命令以管理员身份运行get-pip.py：
>
>   ​		$ sudo python get-pip.py
>
>   ​		注意：如果你启动终端会话时使用的是命令python3，那么在这里应使用命令 sudo python3 get-pip.py。
>
>   ​		这个程序运行后，使用命令pip --version（或pip3 --version）确认正确地安装了pip。

#### 5.在Windows系统中安装pip

>   ​		使用下面的命令运行get-pip.py
>
>   ​		> python get-pip.py
>
>   ​		如果你在终端中运行Python时使用的是另一个命令，也请使用这个命令来运行get-pip.py。例如，你可能需要使用命令python3 get-pip.py或C:\Python35\python get-pip.py。
>
>   ​		这个程序运行后，执行命令python -m pip --version以确认成功地安装了pip。

### 12.2.2 在 Linux 系统中安装 Pygame

>   ​		如果你使用的是Python 2.7，请使用包管理器来安装Pygame。为此，打开一个终端窗口，并执行下面的命令，这将下载Pygame，并将其安装到你的系统中：
>
>   ​		$ sudo apt-get install python-pygame
>
>   ​		执行如下命令，在终端会话中检查安装情况：
>
>   ​		$ python
>
>   ​		>>> import pygame
>
>   ​		>>>
>
>   ​		如果没有任何输出，就说明Python导入了Pygame。
>
>   
>
>   ​		如果你使用的是Python 3，就需要执行两个步骤：安装Pygame依赖的库；下载并安装Pygame。
>
>   ​		执行下面的命令来安装Pygame依赖的库（如果你开始终端会话时使用的是命令python3.5，请将python3-dev替换为python3.5-dev）：
>
>   ​		$ sudo apt-get install python3-dev mercurial
>
>   ​		$ sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
>
>   ​		这将安装运行《外星人入侵》时需要的库。如果你要启用Pygame的一些高级功能，如添加声音的功能，可安装下面这些额外的库：
>
>   ​		$ sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
>
>   ​		$ sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcodec-dev
>
>   ​		$ sudo apt-get install python-numpy
>
>   ​		接下来，执行下面的命令来安装Pygame（如有必要，将pip替换为pip3）：
>
>   ​		$ pip install pygame
>
>   ​		告知你Pygame找到了哪些库后，输出将暂停一段时间。请按回车键，即便有一些库没有找到。你将看到一条消息，说明成功地安装了Pygame。
>
>   ​		要确认安装成功，请启动一个Python终端会话，并尝试执行下面的命令来导入Pygame：
>
>   ​		$ python3
>
>   ​		>>> import pygame
>
>   ​		>>>
>
>   ​		如果没有任何输出，就说明Python导入了Pygame。

### 12.2.3 在 OS X 系统中安装 Pygame

>   ​		要按照Pygame依赖的有些包，需要Homebrew。
>
>   ​		为安装Pygame依赖的库，请执行下面的命令：
>
>   ​		$ brew install hg sdl sdl_image sdl_ttf
>
>   ​		这将安装运行游戏《外星人入侵》所需的库。每安装一个库后，输出都会向上滚动。
>
>   ​		如果你还想启用较高级的功能，如在游戏中包含声音，可安装下面两个额外的库：
>
>   ​		$ brew install sdl_mixer portmidi
>
>   ​		使用下面的命令来安装Pygame（如果你运行的是Python 2.7，请将pip3替换为pip）：
>
>   ​		$ pip3 install pygame
>
>   ​		启动一个Python终端会话，并导入Pygame以检查安装是否成功（如果你运行的是Python 2.7，请将python3替换为python）：
>
>   ​		$ python3
>
>   ​		>>> import pygame
>
>   ​		>>>
>
>   ​		如果没有任何输出，就说明Python导入了Pygame。

### 12.2.4 在 Windows 系统中安装 Pygame

>   ​		Pygame项目托管在代码分享网站Bitbucket中。要在Windows系统中安装Pygame，请访问https://bitbucket.org/pygame/pygame/downloads/，查找与你运行的Python版本匹配的Windows安装程序。
>
>   ​		如果在Bitbucket上找不到合适的安装程序，请去http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame看看。
>
>   ​		下载合适的文件后，如果它是.exe文件，就运行它。
>
>   ​		如果该文件的扩展名为.whl，就将它复制到你的项目文件夹中。再打开一个命令窗口，切换到该文件所在的文件夹，并使用pip来运行它：
>
>   ​		> python -m pip install --user pygame-1.9.2a0-cp35-none-win32.whl

## 12.3 开始游戏项目

>   ​		现在来开始开发游戏《外星人入侵》。
>
>   ​		首先创建一个空的Pygame窗口，供后面用来绘制游戏元素，如飞船和外星人。
>
>   ​		我们还将让这个游戏响应用户输入、设置背景色以及加载飞船图像。

### 12.3.1 创建 Pygame 窗口以及响应用户输入

>   ​		我们创建一个空的Pygame窗口。
>
>   ​		首先，我们导入了模块sys和pygame。模块pygame包含开发游戏所需的功能。玩家退出时，我们将使用模块sys来退出游戏。
>
>   ​		游戏《外星人入侵》的开头是函数run_game()。
>
>   ​		代码行pygame.init()初始化背景设置，让Pygame能够正确地工作。
>
>   ​		调用pygame.display.set_mode()来创建一个名为screen的显示窗口，这个游戏的所有图形元素都将在其中绘制。实参(1200, 800)是一个元组，指定了游戏窗口的尺寸。
>
>   ​		事件是用户玩游戏时执行的操作，如按键或移动鼠标。
>
>   ​				为让程序响应事件，我们编写一个事件循环，以侦听事件，并根据发生的事件执行相应的任务。
>
>   ​				为访问Pygame检测到的事件，我们使用方法pygame.event.get()。所有键盘和鼠标事件都将促使for循环运行。
>
>   ​				在这个循环中，我们将编写一系列的if语句来检测并响应特定的事件。例如：玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT事件，而我们调用sys.exit()来退出游戏。
>
>   ​		调用pygame.display.flip()命令Pygame让最近绘制的屏幕可见。
>
>   ​				在我们移动游戏元素时，pygame.display.flip()将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果。
>
>   ​		在这个基本的游戏结构中，最后一行调用run_game()，这将初始化游戏并开始主循环。
>
>   ​		如果此时运行这些代码，你将看到一个空的Pygame窗口。

示例：

```python
# alien_invasion.py
import sys

import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    # 开始游戏的主循环
    while True:
        
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

输出语句：

```python
```

### 12.3.2 设置背景色

>   ​		Pygame默认创建一个黑色屏幕。
>
>   ​		我们创建了一种背景色，并将其存储在bg_color中。该颜色只需指定一次，我们在进入主While循环前定义它。
>
>   ​		在Pygame中，颜色是以RGB值指定的。
>
>   ​				这种颜色由红色、绿色和蓝色值组成，其中每个值的可能取值范围都为0~255。
>
>   ​				颜色值(255,0,0)表示红色，(0,255,0)表示绿色，而(0,0,255)表示蓝色。
>
>   ​				通过组合不同的RGB值，可创建1600万种颜色。
>
>   ​				在颜色值(230,230,230)中，红色、蓝色和绿色量相同，它将背景设置为一种浅灰色。
>
>   ​		调用方法screen.fill()，用背景色填充屏幕；这个方法只接受一个实参：一种颜色。

示例：

```python
# alien_invasion.py
import sys

import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    # 设置背景色
    bg_color = (230, 230, 230)
    
    # 开始游戏的主循环
    while True:
        
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # 每次循环时都重绘屏幕
        screen.fill(bg_color)
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

输出语句：

```python
```

### 12.3.3 创建设置类

>   ​		每次给游戏添加新功能时，通常也将引入一些新设置。
>
>   ​		编写一个名为settings的模块，其中包含一个名为Settings的类，用于将所有设置存储在一个地方，以免在代码中到处添加设置。

示例1：

```python
# settings.py
class Settings():
    """存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
```

输出语句：

```python
```

示例2：

```python
# alien_invasion.py
import sys

import pygame

from settings import Settings

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 开始游戏的主循环
    while True:
        
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

输出语句：

```python
```

## 12.4 添加飞船图像

>   ​		下面将飞船加入到游戏中。
>
>   ​		为了在屏幕上绘制玩家的飞船，我们将加载一副图像，再使用Pygame方法blit()绘制它。
>
>   ​		为游戏选择素材时，务必要注意许可。
>
>   ​		在游戏中几乎可以使用任何类型的图像文件，但使用位图（.bmp）文件最为简单，因为Pygame默认加载位图。虽然可配置Pygame以使用其他文件类型，但有些文件类型要求你在计算机上安装相应的图像库。
>
>   ​		选择图像时，要特别注意其背景色。请尽可能选择背景透明的图像，这样可使用图像编辑器将其背景设置为任何颜色。图像的背景色与游戏的背景色相同时，游戏看起来最漂亮；你也可以将游戏的背景色设置成与图像的背景色相同。
>
>   ​		在主项目文件夹（alien_invasion）中新建一个文件夹，将其命名为images，并将文件ship.bmp保存到这个文件夹中。

### 12.4.1 创建 Ship 类

>   ​		选择用于表示飞船的图像后，需要将其显示到屏幕上。我们将创建一个名为ship的模块，其中包含Ship类，它负责管理飞船的大部分行为。
>
>   ​		Ship的方法\__init__()接受两个参数：引用self和screen，其中后者指定了要将飞船绘制到什么地方。
>
>   ​		为加载图像，我们调用了pygame.image.load()。这个函数返回一个表示飞船的surface，而我们将这个surface存储到了self.image中。
>
>   ​		加载图像后，我们使用get_rect()获取相应surface的属性rect。
>
>   ​		处理rect对象时，可使用矩形四角和中心的x和y坐标。可通过设置这些值来指定矩形的位置。
>
>   ​				要将游戏元素居中，可设置相应rect对象的属性center、centerx或centery；
>
>   ​				要让游戏元素与屏幕边缘对齐，可使用属性top、bottom、left或right；
>
>   ​				要调整游戏元素的水平或垂直位置，可使用属性x和y，它们分别是相应矩形左上角的x和y坐标。
>
>   ​		注意：在Pygame中，原点(0,0)位于屏幕左上角，向右下方移动时，坐标值将增大。在1200 x 800的屏幕上，原点位于左上角，而右下角的坐标为(1200,800)。
>
>   ​		方法blitme()，它根据self.rect指定的位置将图像绘制到屏幕上。

示例：

```python
# ship.py
import pygame


class Ship():

    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
```

输出语句：

```python
```

### 12.4.2 在屏幕上绘制飞船

示例：

```python
# alien_invasion.py
import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一艘飞船
    ship = Ship(screen)
    
    # 开始游戏的主循环
    while True:
        
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
```

输出语句：

```python
```

## 12.5 重构：模块 game_functions

>   ​		在大型项目中，经常需要在添加新代码前重构既有代码。重构旨在简化既有代码的结构，使其更容易扩展。

### 12.5.1 函数 check_events()

>   ​		把管理事件的代码移到一个名为check_events()的函数中，以简化run_game()并隔离事件管理循环。
>
>   ​		通过隔离事件循环，可将事件管理与游戏的其他方面（如更新屏幕）分离。

示例1：

```python
# game_functions.py
import sys

import pygame

def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
```

输出语句：

```python
```

示例2：

```python
# alien_invasion.py
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events()

        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
```

输出语句：

```python
```

### 12.5.2 函数 update_screen()

>   ​		将更新屏幕的代码移到一个名为update_screen()的函数中，并将这个函数放在模块game_functions.py中。
>
>   ​		新函数update_screen()包含三个形参：ai_settings、screen 和 ship。

示例1：
```python
# game_functions.py
import sys

import pygame

def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()
```

输出语句：

```python
```

示例2：

```python
# alien_invasion.py
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一艘飞船
    ship = Ship(screen)
    
    # 开始游戏的主循环
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()
```

输出语句：

```python
```

## 12.6 驾驶飞船

>   ​		下面来让玩家能够左右移动飞船。
>
>   ​		为此，我们将编写代码，在用户按左或按右箭头做出响应。

### 12.6.1 响应按键

>   ​		每当用户按键时，都将在Pygame中注册一个事件。
>
>   ​		事件都是通过方法pygame.event.get()获取的，因此在函数check_events()中，我们需要指定要检查那些类型的事件。
>
>   ​		每次按键都被注册为一个KEYDOWN事件。
>
>   ​		检查到KEYDOWN事件时，我们需要检查按下的是否是特定的键。

示例1：

```python
# game_functions.py
import sys

import pygame

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.rect.centerx += 1
            
def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()
```

输出语句：

```python
```

示例2：

```python
# alien_invasion.py
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一艘飞船
    ship = Ship(screen)
    
    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

run_game()
```

输出语句：

```python
```

### 12.6.2 允许不断移动

>   ​		我们将结合使用pygame.KEYDOWN和pygame.KEYUP事件，以及一个名为moving_right的标志来实现持续移动。
>
>   ​		飞船不动时，标志moving_right将为False。玩家按下右箭头键时，我们将这个标志设置为True；而玩家松开时，我们将这个标志重新设置为False。
>
>   ​		飞船的属性都由Ship类控制，因此我们将给这个类添加一个名为moving_right的属性和一个名为update()的方法。
>
>   ​		方法update()检查标志moving_right的状态，如果这个标志为True，就调整飞船的位置。

示例1：

```python
# ship.py
import pygame


class Ship():

    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
```

输出语句：

```python
```

示例2：

```python
# game_functions.py
import sys

import pygame

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            
def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()
```

输出语句：

```python
```

示例3：

```python
# alien_invasion.py
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一艘飞船
    ship = Ship(screen)
    
    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
```

输出语句：

```python
```

### 12.6.3 左右移动

>   ​		对Ship类的方法\__init__()和update()所做的相关修改：
>
>   ​		在方法\__init__()中，我们添加了标志self.moving_left；
>
>   ​		在方法update()中，我们添加一个if代码块而不是elif代码块，这样如果玩家同时按下了左右键，将先增大飞船的rect.centrex值，再降低这个值，即飞船的位置保持不变。
>
>   ​		如果使用一个elif代码块来处理向左移动的情况，右箭头键将始终处于优先地位。
>
>   ​		对check_events()所做的相关修改：
>
>   ​		我们可以使用elif代码块，是因为每个事件都只与一个键相关联；如果玩家同时按下了左右箭头键，将检测到两个不同的事件。

示例1：

```python
# ship.py
import pygame


class Ship():

    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
```

输出语句：

```python
```

示例2：

```python
# game_functions.py
import sys

import pygame

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            
def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()
```

输出语句：

```python
```

### 12.6.4 调整飞船的速度

>   ​		我们可以在Settings类中添加属性ship_speed_factor，用于控制飞船的速度。我们将根据这个属性决定飞船在每次循环时最多移动多少距离。
>
>   ​		通过将速度设置指定为小数值，可在后面加快游戏的节奏时更细致地控制飞船的速度。
>
>   ​		然而，rect的centerx等属性只能存储整数值，因此我们需要对Ship类做些修改。

示例1：

```python
# settings.py
class Settings():
    """存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # 飞船的设置
        self.ship_speed_factor = 1.5
```

输出语句：
```python
```

示例2：

```python
# ship.py
import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
```

输出语句：

```python
```

示例3：

```python
# alien_invasion.py
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    
    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
```

输出语句：
```python
```

### 12.6.5 限制飞船的活动范围

>   ​		我们将修改Ship类的方法update()，让飞船到达屏幕边缘后停止移动。
>
>   ​		self.rect.right返回飞船外接矩形的右边缘的x坐标，如果这个值小于self.screen_rect.right的值，就说明飞船未触及屏幕右边缘。
>
>   ​		self.rect.left返回飞船外接矩形的左边缘的x坐标，如果这个值大于0，就说明飞船未触及屏幕左边缘。
>
>   ​		这就确保仅当飞船在屏幕内时，才调整self.center的值。

示例1：

```python
# ship.py
import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
```

输出语句：

```python
```

### 12.6.6 重构 check_events()

>   ​		随着游戏开发的进行，函数check_events()将越来越长，我们将其部分代码放在两个函数中：一个处理KEYDOWN事件，另一个处理KEYUP事件。

示例：
```python
# game_functions.py
import sys

import pygame


def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)   
        elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
```

输出语句：

```python
```

## 12.7 简单回顾

>   ​		当前，我们有四个文件，其中包含很多类、函数和方法。
>
>   ​		添加其他功能之前，为让你清楚这个项目的组织结构，先来回顾一下这些文件。

### 12.7.1 alien_invasion.py

>   ​		主文件alien_invasion.py创建一系列整个游戏都要用到的对象：
>
>   ​		存储在ai_settings中的设置、存储在screen中的主显示surface以及一个飞船实例。
>
>   ​		文件alien_invasion.py还包含游戏的主循环，这是一个调用check_events()、ship.update()和update_screen()的while循环。
>
>   ​		
>
>   ​		要玩游戏《外星人入侵》，只需运行文件alien_invasion.py。其他文件（settings.py、game_functions.py、ship.py）包含的代码被直接或间接地导入到这个文件中。

### 12.7.2 settings.py

>   ​		文件settings.py包含Settings类，这个类只包含方法\__init__()，它初始化控制游戏外观和飞船速度的属性。

### 12.7.3 game_functions.py

>   ​		文件game_functions.py包含一系列函数，游戏的大部分工作都是由它们完成的。
>
>   ​		函数check_events()检测相关的事件，如按键和松开，并使用辅助函数check_keydown_events()和check_keyup_events()来处理这些事件。
>
>   ​		就目前而言，这些函数管理飞船的移动。
>
>   ​		模块game_functions还包含函数update_screen()，它用于在每次执行主循环时都重绘屏幕。

### 12.7.4 ship.py

>   ​		文件ship.py包含Ship类，这个类包含方法\__init__()、管理飞船位置的方法update()以及在屏幕上绘制飞船的方法blitme()。
>
>   ​		表示飞船的图像存储在文件夹images下的文件ship.bmp中。

## 12.8 射击

>   ​		我们将编写玩家按空格键时发射子弹（小矩形）的代码。子弹将在屏幕中向上穿行，抵达屏幕上边缘后消失。

### 12.8.1 添加子弹设置

>   ​		更新settings.py，在其方法\__init__()末尾存储新类Bullet所需的值。

示例：

```python
# settings.py
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
```

输出语句：

```python
```

### 12.8.2 创建 Bullet 类

>   ​		创建存储Bullet类的文件bullet.py。
>
>   ​		Bullet类继承了我们从模块pygame.sprite中导入的Sprite类。通过使用精灵，可将游戏中相关的元素编组，进而同时操作编组中的所有元素。
>
>   ​		为创建子弹实例，需要向\__init__()传递ai_setting、screen和ship实例，还调用了super()来继承Sprite。
>
>   ​		注意：代码super(Bullet, self).\__init__()使用了Python2.7语法。
>
>   ​				这种语法也适用于Python3，但你也可以将这行代码简写为super().\__init__()。
>
>   ​		我们创建子弹的属性rect。子弹并非基于图像的，因此我们必须使用pygame.Rect()类从空白开始创建一个矩形。
>
>   ​		函数draw.rect()使用存储在self.color中的颜色填充表示子弹的rect占据的屏幕部分。

示例：

```python
# bullet.py
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""


    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y


    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
```

输出语句：

```python

```

### 12.8.3 将子弹存储到编组中

>   ​		我们将在alien_invasion.py中创建一个编组（group），用于存储所有有效的子弹，以便能够管理发射出去的所有子弹。
>
>   ​		这个编组将是pygame.sprite.Group类的一个实例。
>
>   ​		pygame.sprite.Group类类似于列表，但提供了有助于开发游戏的额外功能。
>
>   ​		在主循环中，我们将使用这个编组在屏幕上绘制子弹，以及更新每颗子弹的位置。
>
>   ​		当你对编组调用update()时，编组将自动对其中的每个精灵调用update()。

示例：

```python
# alien_invasion.py
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
```

输出语句：

```python
```

### 12.8.4 开火

>   ​		在game_functions.py中，我们需要修改check_keydown_events()，以便在玩家按空格键时发射一颗子弹。
>
>   ​		我们无需修改check_keyup_events()，因为玩家松开空格键时什么都不会发生。
>
>   ​		我们还需要修改update_screen()，确保在调用flip()前再屏幕上重绘每颗子弹。
>
>   ​		方法bullets.sprites()返回一个列表，其中包含编组bullets中的所有精灵。

示例：

```python
# game_functions.py
import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
   	
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
```

输出语句：
```python
```

### 12.8.5 删除已消失的子弹

>   ​		当前，子弹抵达屏幕顶端后消失，这仅仅是因为Pygame无法在屏幕外面绘制它们。这些子弹实际上依然存在，它们的y坐标为负数，且越来越小。这是个问题，因为它们将继续消耗内存和处理能力。
>
>   ​		我们需要将这些已消失的子弹删除，否则游戏所做的无谓工作将越来越多，进而变得越来越慢。
>
>   ​		为此，我们需要检测这样的条件，即表示子弹的rect的bottom属性为0，它表明子弹已穿过屏幕顶端。
>
>   ​		运行这个游戏并确认子弹已被删除后，将这条print语句删除。如果你留下了这条语句，游戏的速度将大大降低，因为将输出写入到终端而花费的时间比将图形绘制到游戏窗口花费的时间还多。

示例：

```python
# alien_invasion.py
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        
        # 删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
        print(len(bullets))
        
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
```

输出语句：
```python
```

### 12.8.6 限制子弹数量

>   ​		很多射击游戏都对可同时出现在屏幕上的子弹数量进行限制，以鼓励玩家有目标地射击。

示例1：

```python
# settings.py
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
```

输出语句：

```python
```

示例2：

```python
# game_functions.py
import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
```

输出语句：

```python
```

### 12.8.7 创建函数 update_bullets()

>   ​		编写并检查子弹管理代码后，可将其移到模块game_functions中，以让主程序文件alien_invasion.py尽可能简单。
>
>   ​		我们创建一个名为update_bullets()的新函数，并将其添加到game_functions.py的末尾。
>
>   
>
>   ​		我们让主循环包含尽可能少的代码，这样只要看函数名就能迅速知道游戏中发生的情况。
>
>   ​		主循环检查玩家的输入，然后更新飞船的位置和所有未消失的子弹的位置。接下来，我们使用更新后的位置来绘制新屏幕。

示例1：

```python
# game_functions.py
import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
    

def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
```

输出语句：

```python
```

示例2：

```python
# alien_invasion.py
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
```

输出语句：

```python
```

### 12.8.8 创建函数 fire_bullet()

>   ​		函数fire_bullet()只包含玩家按空格键时用于发射子弹的代码。
>
>   ​		在check_keydown_events()中，我们在玩家按空格键时调用fire_bullet()。

示例：

```python
# game_functions.py
import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到限制，就发射一颗子弹"""
	# 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

        
def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
```

输出语句：

```python

```

## 12.9 小结

>   ​		在本章中，你学习了：
>
>   ​				游戏开发计划的制定；
>
>   ​				使用Pygame编写的游戏的基本结构；
>
>   ​				如何设置背景色，以及如何将设置存储在可供游戏的各个部分访问的独立类中；
>
>   ​				如何在屏幕上绘制图像，以及如何让玩家控制游戏元素的移动；
>
>   ​				如何创建自动移动的元素，如在屏幕中向上飞驰的子弹，以及如何删除不再需要的对象；
>
>   ​				如何定期重构项目的代码，为后续开发提供便利。		
