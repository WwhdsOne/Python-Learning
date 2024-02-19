# Python的字典（Dictionary）是一种无序的键值对集合，键必须是唯一的。

# 1.创建字典：使用花括号{}创建字典，键值对之间用逗号,分隔，键和值之间用冒号:分隔。
my_dict = {"name": "Alice", "age": 20, "gender": "female"}

# 2.访问元素：通过键来访问字典中的值
print(my_dict["name"])  # 输出：Alice

# 3.修改元素：通过键来修改字典中的值。
my_dict["age"] = 21
print(my_dict)  # 输出：{'name': 'Alice', 'age': 21, 'gender': 'female'}

# 4.添加元素：通过新的键来添加元素。
my_dict["city"] = "Beijing"
print(
    my_dict
)  # 输出：{'name': 'Alice', 'age': 21, 'gender': 'female', 'city': 'Beijing'}

# 5.删除元素：使用del语句或pop()方法删除元素。
del my_dict["city"]
print(my_dict)  # 输出：{'name': 'Alice', 'age': 21, 'gender': 'female'}

age = my_dict.pop("age")
print(age)  # 输出：21
print(my_dict)  # 输出：{'name': 'Alice', 'gender': 'female'}

# 6.字典长度：使用len()函数获取字典的长度。
print(len(my_dict))  # 输出：2

# 7.在Python中，可以使用多种方法来遍历字典。

# 7.1 遍历所有的键
for key in my_dict:
    print(key)  # 输出：name
#   或者
for key in my_dict.keys():
    print(key)
# 7.2 遍历所有的值
for value in my_dict.values():
    print(value)
# 7.3 遍历所有的键值对
for key, value in my_dict.items():
    print(key, value)


# 以上就是Python字典的基础操作，包括如何创建字典、访问元素、修改元素、添加元素、删除元素和获取字典长度。

"""
练习案例：升职加薪
有如下员工信息,请使用字典完成数据的记录。
并通过for循环,对所有级别为1级的员工,级别上升1级,薪水增加1000元
"""
staff = {
    "王力红": {"部门:": "销售部", "级别:": 1, "薪水:": 5000},
    "周杰伦": {"部门:": "技术部", "级别:": 2, "薪水:": 6000},
    "李小龙": {"部门:": "人事部", "级别:": 1, "薪水:": 4000},
    "张靓颖": {"部门:": "销售部", "级别:": 3, "薪水:": 7000},
    "刘德华": {"部门:": "技术部", "级别:": 1, "薪水:": 5500},
}

