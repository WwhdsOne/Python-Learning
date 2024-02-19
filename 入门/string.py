# Python的字符串（str）是一种有序的字符集合，可以使用单引号'或双引号"来创建字符串。

# 1.创建字符串
s1 = 'hello'
s2 = "world"

# 2.访问字符串:通过索引来访问字符串中的字符，索引从0开始。
print(s1[0])  # 输出：h

# 3.字符串长度:使用len()函数获取字符串的长度。
print(len(s1))  # 输出：5

# 4.字符串拼接:使用+操作符来拼接字符串。
s3 = s1 + ' ' + s2
print(s3)  # 输出：hello world

# 5.字符串不可变：字符串一旦创建，就不能修改其内容。
s1[0] = 'H'  # 报错：TypeError: 'str' object does not support item assignment

# 6.字符串方法：字符串有许多内置的方法，如lower()、upper()、split()等。
print(s1.upper())  # 输出：HELLO
print(s3.split())  # 输出：['hello', 'world']
#
# 以上就是Python字符串（str）的基础用法
# 包括如何创建字符串、访问字符、获取字符串长度、拼接字符串，以及字符串的不可变性和一些常用的字符串方法。

'''
练习案例：分割字符串
· 给定一个字符串："Wwhds_one Wwhds sdhwW"
· 统计字符串内有多少个"Ww"字符
· 将字符串内的空格，全部替换为字符："|"
· 并按照"|"进行字符串分割，得到列表

提示：
· count、replace、split
'''