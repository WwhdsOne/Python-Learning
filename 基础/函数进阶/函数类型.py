# 在Python中，函数可以有多个返回值。这是通过返回一个元组来实现的。以下是一个示例：
def func():
    return 1, 2, "Wwhds"

x, y, z = func()
"""
按照返回值的顺序，写对应顺序的多个变量接收即可
变量之间用逗号隔开
支持不同类型的数据return
"""
print(x)  # 输出: 1
print(y)  # 输出: 2
print(z)  # 输出: Wwhds

# Python函数的参数有以下几种类型：

# 1.位置参数（Positional arguments）：这是最常见的参数类型，按照函数定义的位置来传递参数。
def func(a, b):
    return a + b

print(func(1, 2))  # 输出: 3

# 2.关键字参数（Keyword arguments）：在调用函数时，通过"键=值"的形式指定参数的值。
def user_info(name, age, gender):
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender}")
# 位置参数 - 默认使用形式
user_info('小明', 20, '男')

# 关键字参数
user_info(name='小王', age=11, gender='女')
user_info(age=10, gender='女', name='潇潇')    # 可以不按照参数的定义顺序传参
user_info('甜甜', gender='女', age=9)


# 3.默认参数（Default arguments）：在定义函数时，可以为参数指定默认值。
def func(a, b=2):
    return a + b
# 函数调用时，如果为缺省参数传值则修改默认参数值, 否则使用这个默认值


# 4.可变位置参数（Variable positional arguments）：如果在参数名前面加上*，那么这个参数可以接受任意数量的位置参数。
def func(*args):
    return sum(args)

print(func(1, 2, 3, 4, 5))  # 输出: 15



# 5.可变关键字参数（Variable keyword arguments）：如果在参数名前面加上**，那么这个参数可以接受任意数量的关键字参数。
def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

func(a=1, b=2, c=3)

# 以上就是Python函数的参数类型，每种参数类型都有其特定的使用场景，可以根据需要选择使用。

