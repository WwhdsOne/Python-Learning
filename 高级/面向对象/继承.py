"""
在Python中,我们可以使用继承来创建一个新的类,这个新的类会继承父类的所有属性和方法。
我们可以使用class关键字和父类的名称来创建一个子类。
以下是一个Python继承的例子:
"""
# 父类
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# 子类
class Dog(Animal):
    def speak(self):
        return "Woof!"

# 子类
class Cat(Animal):
    def speak(self):
        return "Meow!"
"""
在Python中,pass是一个空操作语句,它什么都不做。
它常常用在需要语法上需要有语句,但程序逻辑上什么都不需要做的地方。
"""


"""
在Python中，复写（Override）是面向对象编程中的一个重要概念。
当子类继承了父类的方法后，如果子类需要改变父类方法的行为，就需要在子类中重新定义这个方法，这就是方法的复写。
以下是一个Python方法复写的例子：
"""

# 父类
class Animal:
    def speak(self):
        return "This animal makes a sound"

# 子类
class Dog(Animal):
    def speak(self):
        return "Woof!"
    def father_speak(self):
        return super().speak()

# 子类
class Cat(Animal):
    def speak(self):
        return "Meow!"