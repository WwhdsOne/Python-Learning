# 在Python中,我们使用if,elif和else关键字来创建条件判断语句。以下是一些示例:
# 基本的if语句
x = 10
if x > 0:
    print("x is positive")
    
'''
练习案例:成年人判断
1. 通过input语句,获取键盘输入,为变量age赋值。(注意转换成数字类型)
2. 通过if判断是否是成年人,满足条件则输出提示信息,如下:
提示:您已成年,需要补票的信息输出,来自if判断
'''





# if-else语句
y = -5
if y > 0:
    print("y is positive")
else:
    print("y is not positive")
    
'''
练习案例：我要买票吗
通过input语句获取键盘输入的身高
判断身高是否超过120cm,并通过print给出不同提示信息。
'''





# if-elif-else语句
z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")
'''
练习案例：猜猜心里数字
1. 定义一个变量,数字类型,内容随意。
2. 基于input语句输入猜想的数字,通过if和多次elif的组合,判断猜想数字是否和心里数字一致。
'''

# 嵌套的if语句
a = 10
b = 20
if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("a is less than b")
else:
    print("a is equal to b")
    
# 在这些示例中,if后面的表达式被称为条件。如果条件为真（即结果为True）,则执行该条件后面的代码块。
# elif和else关键字允许我们在原始条件不满足的情况下检查更多的条件。


'''
案例需求:
    定义一个数字(1~10,随机产生),通过3次判断来猜出来数字
案例要求:
    1.数字随机产生,范围1-10
    2.有3次机会猜测数字,通过3层嵌套判断实现
    3.每次猜不中,会提示大了或小了
提示,通过如下代码,可以定义一个变量num,变量内存储随机数字。
import random
num = random.randint(1, 10)
'''

