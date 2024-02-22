"""
学生信息录入
开学了有一批学生信息需要录入系统，请设计一个类，记录学生的：
姓名、年龄、地址，这3类信息
请实现：
通过for循环，配合input输入语句，并使用构造方法，完成学生信息的键盘录入
输入完成后，使用print语句，完成信息的输出
"""

class stu:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def print_info(self):
        print(f"姓名：{self.name}，年龄：{self.age}，地址：{self.address}")
student1 = stu(input("请输入学生姓名："), input("请输入学生年龄："), input("请输入学生地址："))
student1.print_info()