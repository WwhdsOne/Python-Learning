class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} miao miao miao")
class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} wang wang wang")
def speak(animal: Animal):
    animal.speak()
cat = Cat("kitty")
dog = Dog("doggy")
speak(cat) # kitty miao miao miao
speak(dog) # doggy wang wang wang

"""
在Python中,抽象类是一种特殊的类,它不能被实例化,只能被其他类继承。
抽象类可以定义抽象方法,这些方法在抽象类中没有实现,必须在子类中实现。
Python的abc模块提供了ABC(Abstract Base Class)类和abstractmethod装饰器,可以用来定义抽象类和抽象方法。
以下是一个Python抽象类的例子:
"""

from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    def speak(self):
        pass

class Dog(AbstractAnimal):
    def speak(self):
        return "Woof!"

class Cat(AbstractAnimal):
    def speak(self):
        return "Meow!"


