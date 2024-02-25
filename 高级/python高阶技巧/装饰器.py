# 装饰器其实也是一种闭包, 其功能就是在不破坏目标函数原有的代码和功能的前提下,为目标函数增加新功能。

# (这不就是java的AOP吗？)

def sleep():
    import random
    import time
    print("开始睡觉了")
    time.sleep(random.random())
sleep()
"""
希望给sleep函数,增加一个功能:
在调用sleep前输出:我要睡觉了
在调用sleep后输出:我起床了
装饰器的一般写法（闭包写法）
"""
def outer(fun):
    def inner():
        print("我要睡觉了")
        fun()
        print("我起床了")
    return inner
fn = outer(sleep)
fn()
# 装饰器的语法糖写法

# 使用@outer
# 定义在目标函数sleep之上
@outer
def sleep():
    import random
    import time
    print("开始睡觉了")
    time.sleep(random.random())
sleep()

