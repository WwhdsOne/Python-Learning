"""
进程和线程:
现代操作系统比如Mac OS X,UNIX,Linux,Windows等,都是支持“多任务”的操作系统。
进程:就是一个程序,运行在系统之上,那么便称之这个程序为一个运行进程,并分配进程ID方便系统管理。
线程:线程是归属于进程的,一个进程可以开启多个线程,执行不同的工作,是进程的实际工作最小单位。

进程就好比一家公司,是操作系统对程序进行运行管理的单位
线程就好比公司的员工,进程可以有多个线程（员工）,是进程实际的工作者

操作系统中可以运行多个进程,即多任务运行
一个进程内可以运行多个线程,即多线程运行
注意点:

进程之间是内存隔离的, 即不同的进程拥有各自的内存空间。 这就类似于不同的公司拥有不同的办公场所。

线程之间是内存共享的,线程是属于进程的,一个进程内的多个线程之间是共享这个进程所拥有的内存空间的。
这就好比,公司员工之间是共享公司的办公场所。

并行执行:
并行执行的意思指的是同一时间做不同的工作。
进程之间就是并行执行的,操作系统可以同时运行好多程序,这些程序都是在并行执行。

除了进程外,线程其实也是可以并行执行的。
也就是比如一个Python程序,其实是完全可以做到:
一个线程在输出:你好
一个线程在输出:Hello
像这样一个程序在同一时间做两件乃至多件不同的事情, 我们就称之为:多线程并行执行
绝大多数编程语言,都允许多线程编程,Pyhton也不例外。
Python的多线程可以通过threading模块来实现。
"""
import threading
# thread_obj = threading.Thread([group [, target [, name [, args [, kwargs]]]]])
# - group: 线程组,目前还没有实现,库引用默认为None
# - target: 要执行的方法
# - name: 线程名
# - args: 要传入方法的参数
# - kwargs: 字典类型的参数
def sing():
    for i in range(10):
        print("正在唱歌...%d" % i)
def dance():
    for i in range(10):
        print("正在跳舞...%d" % i)
def action(msg):
    for i in range(10):
        print(f"正在{msg}...{i}")
# 创建线程
sing_thread = threading.Thread(target=sing)
dance_thread = threading.Thread(target=dance)
action_thread1 = threading.Thread(target=action,args=("玩LOL",))
sing_thread.start()
dance_thread.start()
action_thread1.start()
"""
threading模块的使用
thread_obj = threading.Thread(target=func)  创建线程对象
thread_obj.start() 启动线程执行
"""


    