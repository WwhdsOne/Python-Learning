# Python的元组（Tuple）是一种有序的、不可变的集合，一旦创建就不能修改。

# 1.创建元组：使用圆括号()创建元组，元素之间用逗号,分隔。
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# 2.访问元素：通过索引来访问元组中的元素，索引从0开始。
print(my_tuple[0])  # 输出：1

# 3.元组长度：使用len()函数获取元组的长度。
print(len(my_tuple))  # 输出：6

# 4.元组一旦创建，就不能修改其元素或大小。
my_tuple[0] = 'one'  # 报错：TypeError: 'tuple' object does not support item assignment

# 5.单元素元组：创建只有一个元素的元组时，需要在元素后面添加逗号,，否则Python会将其解释为一个普通的括号表达式。
single_element_tuple = (1,)  # 正确
not_a_tuple = (1)  # 错误，这是一个整数，不是元组

# 以上就是Python元组的基础用法，包括如何创建元组、访问元素、获取元组长度，以及元组的不可变性和创建单元素元组的特殊语法。


'''
练习案例:元组的基本操作
定义一个元组，内容是：（'周杰轮', 11, ['football', 'music']），记录的是一个学生的信息（姓名、年龄、爱好）

请通过元组的功能（方法），对其进行
1.查询其年龄所在的下标位置
2.查询学生的姓名
3.删除学生爱好中的football
4.增加爱好:coding到爱好list内
'''