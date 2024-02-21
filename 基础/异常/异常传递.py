"""
在Python中,当一个异常被抛出时,它会被传递给上层的代码块来处理。这个过程被称为异常的传递。
如果一个函数内部发生了异常,但该函数没有处理这个异常（即没有捕获这个异常）,那么这个异常就会被传递给调用这个函数的代码块。
如果调用这个函数的代码块也没有处理这个异常,那么异常会继续被传递,直到被某个代码块捕获,或者传递到最顶层（主程序）而导致程序终止。
以下是一个例子：
"""

def divide(x, y):
    return x / y  # 如果y是0，这里会抛出ZeroDivisionError

try:
    result = divide(1, 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
