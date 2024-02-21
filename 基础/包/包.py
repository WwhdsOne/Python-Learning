"""
在Python中,包是一种组织模块的方式,它使用"点模块名称"。例如,一个模块的名称是 A.B, 那么他表示一个包 A中的子模块 B 。
创建包
创建包很简单。首先,创建一个目录,用于存放相关的模块,这个目录就是包的名字。
然后,在这个目录下创建一个__init__.py文件,这个文件的存在,告诉Python这个目录应该被视为一个包。__init__.py可以是空文件,也可以有Python代码,因为__init__.py会被当作一个模块,你可以定义任何你想定义的变量,函数,类等等。
例如,你有以下的目录结构：
mypackage/
    __init__.py
    module1.py
    module2.py
"""
# 你可以使用和导入模块类似的语法来导入包。例如：import mypackage.module1
import mypackage.module1
print(mypackage.module1.add(1, 1))  # 输出：1

# 你也可以使用from...import语句来导入包中的模块：
from mypackage import module2
print(module2.mul(2, 5))  # 输出：10

# 你还可以导入包中模块的指定部分：
from mypackage.module1 import sub
print(sub(10, 3))  # 输出：7
