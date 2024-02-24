"""
在Python中,我们可以通过在属性名前加上两个下划线__来创建私有属性。
这样的属性只能在类的内部访问,不能在类的外部直接访问。
类中提供了私有成员的形式来支持。
· 私有成员变量
· 私有成员方法

定义私有成员的方式非常简单,只需要:
· 私有成员变量:变量名以__开头（2个下划线）
· 私有成员方法:方法名以__开头（2个下划线）
即可完成私有成员的设置

"""
class PhoneTest:
    ID = None # 编号
    producer = None # 生产商
    __current_voltage = None # 电压
    
    def call_back_5g(self):
        print("5G通话")
    def __keep_sign_coure(self):
        print("保持单核运行")

phonetest = PhoneTest()
phonetest.call_back_5g()
# phonetest.__keep_sign_coure() # 报错
# phonetest.__current_voltage = 5 # 报错

"""
练习案例:
设计带有私有成员的手机
设计一个手机类,内部包含:
私有成员变量:__is_5g_enable,类型bool,True表示开启5g,False表示关闭5g
私有成员方法:__check_5g(),会判断私有成员__is_5g_enable的值
若为True,打印输出:5g开启
若为False,打印输出:5g关闭,使用4g网络
公开成员方法:call_by_5g(),调用它会执行
调用私有成员方法:__check_5g(),判断5g网络状态
打印输出:正在通话中
运行结果:

通过完成这个类的设计和使用,体会封装中私有成员的作用
对用户公开的,call_by_5g()方法
对用户隐藏的,__is_5g_enable私有变量和__check_5g私有成员
"""
class Phone:
    __is_5g_enable = False
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭,使用4g网络")
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")
phone = Phone()
phone.call_by_5g()

