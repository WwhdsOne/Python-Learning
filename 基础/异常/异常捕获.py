"""
在Python中,异常是在程序运行时发生的错误。当Python解释器遇到一个错误时,它会创建一个异常对象。
如果你的代码没有正确处理这个异常,那么程序就会停止,并显示一个错误消息。
Python有许多内置的异常类型,例如ValueError、TypeError、IndexError、FileNotFoundError等等。
你也可以定义自己的异常类型。
你可以使用try/except语句来捕获并处理异常。以下是一个例子:
"""
# 基本语法：
try:
    x = 1 / 0  # 这会引发一个ZeroDivisionError,可能发生错误的代码
except ZeroDivisionError:
    print("You can't divide by zero!") # 如果出现异常执行的代码

# 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。
# 一般try下方只放一行尝试执行的代码。

# 1.捕获指定异常，基本语法：
try:
    print(name)
except NameError as e:
    print('name变量名称未定义错误')
    
# 2.捕获多个异常，基本语法：
# 当捕获多个异常时，可以把要捕获的异常类型的名字，放到except 后，并使用元组的方式进行书写。
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('ZeroDivision错误...')

# 3.捕获异常并输出描述信息，基本语法：
try:
    print(num)
except (NameError, ZeroDivisionError) as e:
    print(e)

# 4.捕获所有异常，基本语法：
try:
    print(name)
except Exception as e:
    print(e)

# 5.异常else
# else表示的是如果没有异常要执行的代码。
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('我是else，是没有异常的时候执行的代码')

# 6.异常的finally
# finally表示的是无论是否有异常都要执行的代码。
try:
    f = open('test.txt', 'r')
except Exception as e:
    f = open('test.txt', 'w')
else:
    print('没有异常，真开心')
finally:
    f.close()



