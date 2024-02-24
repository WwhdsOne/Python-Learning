"""
上文学习的__init__ 构造方法,是Python类内置的方法之一。
这些内置的类方法,各自有各自特殊的功能,这些内置方法我们称之为：魔术方法
Python的魔术方法是一种特殊的方法,它们的名称以双下划线开始和结束,例如__init__。魔术方法定义了类的特殊行为,例如运算符重载、属性访问等。以下是一些常用的魔术方法：

__init__(self, ...): 构造方法,当一个对象被创建并初始化时调用。

__del__(self): 析构方法,当一个对象被销毁（即,它的引用计数达到零并被垃圾收集器收回）时调用。

__str__(self): 当使用str()函数或print函数打印一个对象时调用,应返回一个描述该对象的字符串。

__repr__(self): 当使用repr()函数获取对象的字符串表示时调用,应返回一个表达创建同一个对象的Python表达式的字符串。

__eq__(self, other): 定义等于（==）运算符的行为。

__ne__(self, other): 定义不等于（!=）运算符的行为。

__lt__(self, other): 定义小于（<）运算符的行为。

__gt__(self, other): 定义大于（>）运算符的行为。

__le__(self, other): 定义小于等于（<=）运算符的行为。

__ge__(self, other): 定义大于等于（>=）运算符的行为。

__add__(self, other): 定义加法（+）运算符的行为。

__sub__(self, other): 定义减法（-）运算符的行为。

__mul__(self, other): 定义乘法（*）运算符的行为。

__truediv__(self, other): 定义真除法（/）运算符的行为。

__floordiv__(self, other): 定义整除法（//）运算符的行为。

__mod__(self, other): 定义取模（%）运算符的行为。

__pow__(self, other): 定义乘方（**）运算符的行为。

以下是一个使用了一些常用魔术方法的Python类的例子:
"""
class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}j"

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        else:
            return ComplexNumber(self.real + other, self.imag)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        else:
            return ComplexNumber(self.real - other, self.imag)

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imag == other.imag
        else:
            return False
c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(2, 3)

print(c1)  # 输出：1 + 2j
print(c1 + c2)  # 输出：3 + 5j
print(c1 - c2)  # 输出：-1 - 1j
print(c1 == c2)  # 输出：False