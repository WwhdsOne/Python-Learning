# 在Python中,模块是一个包含Python定义和语句的文件。模块可以定义函数、类和变量,也可以包含可执行的代码。

# 1.创建模块
# 当前文件夹下有一个名为mymodule.py的文件,其中包含以下内容:
# def hello():
#   print("Hello, world!")
# 这个文件就是一个模块，你可以在其他Python脚本中导入并使用它。

# 2.导入模块 
# 你可以使用import语句来导入模块，然后使用模块名.函数名的方式来调用模块中的函数：
import mymodule
mymodule.hello()  # 输出：Hello, world!

# 3.from...import语句
# 你也可以使用from...import语句来导入模块中的特定部分：
from mymodule import hello
hello()  # 输出：Hello, world!

# as关键字
# 你可以使用as关键字给导入的模块起一个别名：
import mymodule as mm

mm.hello()  # 输出：Hello, world!


