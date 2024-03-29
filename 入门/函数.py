# 在Python中,函数是一种组织和复用代码的方式。以下是Python函数的基础知识:

# 1.定义函数:使用def关键字定义函数
# 后面跟函数名和圆括号()。圆括号中可以放置函数的参数。函数的主体从下一行开始,并且必须缩进。
def greet():
    print("Hello, World!")

# 2.调用函数:通过函数名后面跟圆括号()来调用函数
greet()  # 输出:Hello, World!


'''
练习案例:打印欢迎语
定义一个函数,函数名任意,要求调用函数后可以输出如下欢迎语:
欢迎来到Wwhds的教程
我会好好学python的
'''

# 3.函数可以接受参数,参数在函数定义时放在圆括号中。在函数调用时,我们将值传递给参数。
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # 输出:Hello, Alice!

# 4.返回值:函数可以返回一个值,这个值可以被赋值给一个变量或在表达式中使用。使用return关键字来返回值。
def add(a, b):
    return a + b


result = add(1, 2)  # result现在是3
print(result)  # 输出:3

# 5.默认参数:函数参数可以有默认值。当函数调用时没有提供这个参数的值时,将使用默认值。
def greet(name="World"):
    print(f"Hello, {name}!")

greet()  # 输出:Hello, World!
greet("Alice")  # 输出:Hello, Alice!

# 以上就是Python函数的基础知识,包括如何定义函数、调用函数、使用参数和返回值,以及如何设置默认参数。

'''
综合案例:ATM
· 定义一个全局变量:money,用来记录银行卡余额(默认5000000)
· 定义一个全局变量:name,用来记录客户姓名（启动程序时输入）
· 定义如下的函数:
    · 查询余额函数
    · 存款函数
    · 取款函数
    · 主菜单函数
· 要求:
· 程序启动后要求输入客户姓名
· 查询余额、存款、取款后都会返回主菜单
· 存款、取款后,都应显示一下当前余额
· 客户选择退出或输入错误,程序会退出,否则一直运行
'''