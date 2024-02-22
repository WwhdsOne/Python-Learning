"""
在Python中，成员方法是定义在类中的函数，它们是类的一部分，可以访问和修改类的属性。
成员方法的第一个参数通常是self，它是一个对类实例自身的引用。
以下是一个简单的例子：
"""
class MyClass:
    def __init__(self):
        self.my_attribute = 0

    def increment(self):
        self.my_attribute += 1
        
        
obj = MyClass()
print(obj.my_attribute)  # 输出：0
obj.increment()
print(obj.my_attribute)  # 输出：1

# 注意，成员方法只能通过类的实例来调用，不能直接通过类来调用。也就是说，你不能这样做：
MyClass.increment()  # 这会引发TypeError