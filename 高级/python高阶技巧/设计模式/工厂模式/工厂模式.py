"""
当需要大量创建一个类的实例的时候， 可以使用工厂模式。
即，从原生的使用类的构造去创建对象的形式
迁移到，基于工厂提供的方法去创建对象的形式。
"""
class Person:
    pass

class Worker(Person):
    pass
class Student(Person):
    pass
class TourGuide(Person):
    pass

worker = Worker()
student = Student()
tour_guide = TourGuide()
# 接下来我们使用工厂模式来建立实体
class PersonFactory:
    def create_person(self, person_type):
        if person_type == "worker":
            return Worker()
        elif person_type == "student":
            return Student()
        elif person_type == "tour_guide":
            return TourGuide()
        else:
            return None
factory = PersonFactory()
worker = factory.create_person("worker")
student = factory.create_person("student")
tour_guide = factory.create_person("tour_guide")
"""
使用工厂类的get_person()方法去创建具体的类对象
优点：
- 大批量创建对象的时候有统一的入口，易于代码维护
- 当发生修改，仅修改工厂类的创建方法即可
- 符合现实世界的模式，即由工厂来制作产品（对象）
"""
