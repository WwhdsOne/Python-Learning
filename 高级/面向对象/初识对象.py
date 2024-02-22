"""
在Python中，几乎所有的东西都是对象，包括数字、字符串、函数、类、模块等等。
对象是数据（属性）和一组访问和操作这些数据的方法的封装。
创建对象
在Python中，你可以通过定义类来创建自己的对象。类是对象的蓝图，它定义了对象的属性和方法。例如：
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
        
# 实例化对象
# 你可以通过调用类来创建类的实例，也就是对象。例如：
bob = Person("Bob", 30)
# 访问属性和方法
# 你可以使用点符号（.）来访问对象的属性和方法。例如：
print(bob.name)  # 输出：Bob
bob.say_hello()  # 输出：Hello, my name is Bob and I'm 30 years old.