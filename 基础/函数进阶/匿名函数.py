"""
在Python中,函数是一等公民,这意味着函数可以作为参数传递给其他函数,也可以作为其他函数的返回值。
这是一种非常强大的特性,使得我们可以编写更加灵活和可重用的代码。
以下是一个例子,演示了如何将函数作为参数传递:
"""


def apply_func(func, x):
    return func(x)

def square(x):
    return x ** 2

print(apply_func(square, 5))  # 输出: 25

"""
在这个例子中,我们定义了一个名为apply_func的函数,它接受两个参数:一个函数func和一个值x。
apply_func函数将x作为参数传递给func,并返回结果。
然后我们定义了一个名为square的函数,它接受一个参数x,并返回x的平方。
"""

"""
在Python中,lambda函数也被称为匿名函数,即没有具体名称的函数。
它允许你快速定义单行的微小函数,这些函数通常在你希望在程序中需要一个短小的,临时使用的函数。
lambda函数的语法结构如下:
"""

lambda arguments: Expression

"""
这里,arguments是一个参数列表,expression是一个关于参数的表达式。
lambda函数可以有任意数量的参数,但表达式只能有一个。
也就是说只能有一行代码, 但是可以有多个参数
以下是一个lambda函数的例子:
"""
double = lambda x: x * 2
print(double(5))  # 输出: 10
# 也可以这么写
print((lambda x: x * 2)(5))  # 输出: 10

# 虽然只有只能有一行代码,但是你可以使用函数使得其能处理多个参数
    
def compose(a,b):
    return a**b
print(lambda a,b:compose(2,3))
