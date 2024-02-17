"""
Python的集合(Set)是一个无序的、不含重复元素的集合,
主要用于测试元素是否存在于集合中,以及进行集合运算,如并集、交集、差集等。
"""

# 1.创建集合：使用花括号{}或set()函数创建集合。
my_set = {1, 2, 3, 'a', 'b', 'c'}
empty_set = set()

# 2.添加元素：使用add()方法添加单个元素，使用update()方法添加多个元素。
my_set.add('d')
my_set.update([4, 5, 6])
print(my_set)  # 输出：{1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd'}

# 3.删除元素：使用remove()方法删除指定元素
# 使用discard()方法删除指定元素但如果元素不存在不会引发错误，使用pop()方法删除并返回任意一个元素。
my_set.remove('d')
my_set.discard('e')  # 不会引发错误
print(my_set.pop())  # 删除并返回一个元素

# 4.测试元素是否存在：使用in关键字测试元素是否存在于集合中。
print(1 in my_set)  # 输出：True

# 5.集合长度：使用len()函数获取集合的长度。
print(len(my_set))  # 输出：集合的长度

# 6.集合运算：使用&、|、-、^等运算符进行集合的交集、并集、差集、对称差集等运算。
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 | set2)  # 输出：{1, 2, 3, 4}
print(set1 & set2)  # 输出：{2, 3}
print(set1 - set2)  # 输出：{1}
print(set1 ^ set2)  # 输出：{1, 4}

'''
以上就是Python集合的基础操作
包括如何创建集合、添加元素、删除元素、测试元素是否存在、获取集合长度，以及进行集合运算。
'''

'''
练习案例：信息去重
有如下列表对象：
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
请：
· 定义一个空集合
· 通过for循环遍历列表
· 在for循环中将列表的元素添加至集合
· 最终得到元素去重后的集合对象，并打印输出
'''
