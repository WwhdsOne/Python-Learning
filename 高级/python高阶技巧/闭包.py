account_amount = 0
def atm(amount,deposit=True):
    global account_amount
    if deposit:
        print(f"{amount}元存入账户,账户余额为{account_amount+amount}元")
    else:
        print(f"{amount}元取出账户,账户余额为{account_amount-amount}元")
atm(1000)
atm(500,False)
"""
尽管功能实现是ok的,但是仍有问题:
- 代码在命名空间上（变量定义）不够干净、整洁
- 全局变量有被修改的风险
如何解决？
将变量定义在函数内部是行不通的
我们需要使用闭包
"""
# 在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包。
# 在Python中，nonlocal关键字用于在一个嵌套的函数中声明一个变量不是局部变量也不是全局变量，而是在上一级函数中定义的变量。
# 如果我们需要在嵌套函数中修改上一级函数的变量，我们需要使用nonlocal关键字。
# 如果不使用nonlocal关键字，Python会在嵌套函数中创建一个新的局部变量，而不是修改上一级函数的变量。
def account_create(inital_amount=0):
    def atm(amount,deposit=True):
        nonlocal inital_amount
        if deposit:
            print(f"{amount}元存入账户,账户余额为{inital_amount+amount}元")
        else:
            print(f"{amount}元取出账户,账户余额为{inital_amount-amount}元")
    return atm
fn = account_create(1000)
fn(500)
fn(200)
fn(300,False)
"""
优点，使用闭包可以让我们得到：
- 无需定义全局变量即可实现通过函数，持续的访问、修改某个值
- 闭包使用的变量的所用于在函数内，难以被错误的调用修改
缺点：
- 由于内部函数持续引用外部函数的值，所以会导致这一部分内存空间不被释放，一直占用内存
"""