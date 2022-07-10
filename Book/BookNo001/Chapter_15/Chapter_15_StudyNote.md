# 第15章：生成数据

>   ​		数据可视化指的是通过可视化表示来探索数据，它与数据挖掘紧密相关，而数据挖掘指的是使用代码来探索数据集的规律和关联。数据集可以是用一行代码就能表示的小型数字列表，也可以是数以吉字节的数据。
>
>   ​		漂亮地呈现数据关乎的并非仅仅是漂亮的图片。以引人注目的简洁方式呈现数据，让观看者能够明白其含义，发现数据集中原本未意识到的规律和意义。
>
>   ​		在基因研究、天气研究、政治经济分析等众多领域，大家都使用Python来完成数据密集型工作。数据科学家使用Python编写了一系列令人印象深刻的可视化和分析工具。最流行的工具之一是matplotlib，它是一个数学绘图库，我们将使用它来制作简单的图表，如折线图和散点图。然后，我们将基于随机漫步概念生成一个更有趣的数据集—根据一系列随机决策生成的图表。
>
>   ​		我们还将使用Pygal包，它专注于生成适合在数字设备上显示的图表。通过使用Pygal，可在用户与图表交互突出元素以及调整其大小，还可轻松地调整整个图表的尺寸，使其适合在微型智能手表或巨型显示器上显示。我们将使用Pygal以各种方式探索掷骰子的结果。

## 15.1 安装 matplotlib

### 15.1.1 在 Linux 系统中安装 matplotlib

>   ​		使用系统自带的Python版本，请执行如下命令：
>
>   ​				`sudo apt-get install python3-matplotlib`
>
>   ​		使用Python 2.7，请执行如下命令：
>
>   ​				`sudo ap-get install python-matplotlib`
>
>   ​		使用Python 3.5，请执行如下命令：
>
>   ​				安装matplotlib依赖库：
>
>   ​						`sudo apt-get install python3.5-dev python3.5-tk tk-dev`
>
>   ​						`sudo apt-get install libfreetype6-dev g++`
>
>   ​				使用pip安装matplotlib
>
>   ​						`pip install --user matplotlib`

### 15.1.2 在 OS X 系统中安装 matplotlib

>   ​		Apple的标准Python安装自带了matplotlib。
>
>   ​		要检查系统是否安装了matplotlib，可打开一个终端会话并尝试导入matplotlib。
>
>   ​		如果系统没有自带matplotlib，且Python是使用Homebrew安装的，请执行如下命令：
>
>   ​				`pip install --user matplotlib`
>
>   ​		注意：安装包时可能需要使用pip3，而不是pip。另外，如果这个命令不管用，你可能需要删除标志--user。

### 15.1.3 在 Windows 系统中安装 matplotlib

>   ​		在Windows系统中，首先需要安装Visual Studio。为此，请访问https://dev.windows.com/，单击Downloads，再查找Visual Studio Community —一组免费的Windows开发工具。请下载并运行该安装程序。
>
>   ​		接下来，需要下载matplotlib安装程序。为此，请访问https://pypi.python.org/pypi/matplotlib/，并查找与你使用的Python版本匹配的wheel文件（扩展名为.whl的文件）。
>
>   ​		注意：如果找不到与你安装的Python版本匹配的文件，请去http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib看看，这个网站发布安装程序的时间通常比matplotlib官网早些。
>
>   ​		将下载好的.whl文件复制到项目文件夹下，打开命令行窗口，并切换到该项目文件夹，使用pip来安装matplotlib。
>
>   ​		请执行如下命令：
>
>   ​				`cd python_work`
>
>   ​				`python -m pip install --user matplotlib-1.4.3-cp35-none-win32.whl`

### 15.1.4 测试 matplotlib

>   ​		安装必要的包后，对安装进行测试。
>
>   ​		使用命令python或python3启动一个终端会话，再尝试导入matplotlib。如果没有出现任何错误消息，就说明你的系统安装了matplotlib。
>
>   ​		请执行如下命令：
>
>   ​				`python3`
>
>   ​				`import matplotlib`

### 15.1.5 matplotlib 画廊

>   ​		要查看使用matplotlib可制作的各种图表，请访问http://matplotlib.org/的示例画廊。单击画廊中的图表，就可查看用于生成图表的代码。

## 15.2 绘制简单的折线图

>   ​		使用matplotlib绘制一个简单的折线图，再对其进行定制，以实现信息更丰富的数据可视化。
>
>   ​		我们将使用平方数序列1、4、9、16和25来绘制这个图表。

示例：

```python
# mpl_squares.py
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
# 将这个列表传递给函数plot(),这个函数尝试根据这些数字绘制出有意义的图形。
plt.plot(squares)
# plt.show()打开matplotlib查看器,并显示绘制的图形。
plt.show()
```

输出：

```python
```

### 15.2.1 修改标签文字和线条粗细

>   ​		参数linewidth决定了plot()绘制的线条粗细。
>
>   ​		函数title()给图表指定标题。
>
>   ​		函数xlabel()和ylabel()让你能够为每条轴设置标题。
>
>   ​		函数tick_params()设置刻度的样式，其中指定的实参将影响x轴和y轴上的刻度(axis='both'),并将刻度标记的字号设置为14(labelsize=14)。

示例：

```python
# mpl_squares.py
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# 设置图表标题,并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
```

输出：

```python
```

### 15.2.2 校正图形

>   ​		当你向plot()提供一系列数字时，它假设第一个数据点对应的x坐标值为0。
>
>   ​		为改变这种默认行为，我们可以给plot()同时提供输入值和输出值。

示例：

```python
# mpl_squares.py
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题,并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
```

输出：

```python
```

### 15.2.3 使用 scatter() 绘制散点图并设置其样式

>   ​		要绘制单个点，可使用函数scatter()，并向它传递一对x和y坐标，它将在指定位置绘制一个点。
>
>   ​		调用scatter()，使用实参s设置了绘制图形时使用点的尺寸。

示例1：

```python
# scatter_squares.py
import matplotlib.pyplot as plt

plt.scatter(2, 4)
plt.show()
```

输出：

```python

```

示例2：

```python
# scatter_squares.py
import matplotlib.pyplot as plt

# 实参s设置点的尺寸
plt.scatter(2, 4, s=200)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
```

输出：

```python
```

### 15.2.4 使用 scatter() 绘制一系列点

示例：

```python
# scatter_squares.py
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
```

输出：

```python
```

### 15.2.5 自动计算数据

>   ​		函数axis()指定了每个坐标轴的取值范围。
>
>   ​		函数axis()要求提供四个值：x和y坐标轴的最小值和最大值。

示例：

```python
# scatter_squares.py
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
```

输出：

```python
```

### 15.2.6 删除数据点的轮廓

>   ​		matplotlib允许你给散点图中的各个点指定颜色。默认为蓝色点和黑色轮廓。
>
>   ​		要删除数据点的轮廓，可调用scatter()时传递实参edgecolor='none'。
>
>   ​				`plt.scatter(x_values, y_values, edgecolor='none', s=40)`
>
>   ​		在2.0.0版本的matplotlib中，scatter()函数的实参edgecolor默认为'none'。

示例：

```python
# scatter_squares.py
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
```

输出：

```python
```

### 15.2.7 自定义颜色

>   ​		要指定自定义颜色，可传递参数c。
>
>   ​		方式1：使用颜色的名称；
>
>   ​				`plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)`
>
>   ​		方式2：使用RGB颜色模式，将其设置为一个元组，其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量。值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅。
>
>   ​				`plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)`

示例1：

```python
# scatter_squares.py
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
```

输出：

```python

```

示例2：

```python
# scatter_squares.py
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
```

输出：

```python
```

### 15.2.8 使用颜色映射

>   ​		颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。
>
>   ​		在可视化中，颜色映射用于突出数据的规律。例如，用较浅颜色来显示较小的值，较深颜色来显示较大的值。
>
>   ​		模块pyplot内置了一组颜色映射，使用参数cmap设置使用哪个颜色映射。
>
>   ​		注意：要了解pyplot中所有的颜色映射，请访问http://matplotlib.org/，单击Examples，向下滚动到Color Examples，再单击colormaps_reference。

示例：

```python
# scatter_squares.py
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
```

输出：

```python
```

### 15.2.9 自动保存图表

>   ​		要让程序自动将图表保存到文件中，可调用plt.savefig()。
>
>   ​		实参fname：是一个包含文件名路径的字符串，或者是一个类似于python文件的对象；
>
>   ​		实参bbox_inches：将图表多余的空白区域裁剪掉。
>
>   ​				`plt.savefig(r'./images/squares_plot.png', bbox_inches='tight')`

示例：

```python
# scatter_squares.py
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
            edgecolor='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.savefig(r'./images/squares_plot.png', bbox_inches='tight')
```

输出：

```python

```

## 15.3 随机漫步