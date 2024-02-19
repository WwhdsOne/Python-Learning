"""
在Python,使用open函数,可以打开一个已经存在的文件,或者创建一个新文件,语法如下:
open(name, mode, encoding)
name:是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。
mode:设置打开文件的模式(访问模式):只读、写入、追加等。
encoding:编码格式(推荐使用UTF-8)
"""
f = open('file.txt', 'r', encoding="UTF-8")
f.close()
# encoding的顺序不是第三位,所以不能用位置参数,用关键字参数直接指定
"""
Python的open函数默认的编码方式取决于你的系统环境。
在大多数系统中,包括Windows和Linux,open函数默认的编码方式通常是UTF-8。
所以你有时可以不必写编码格式
你可以通过以下代码来查看默认的编码方式：
"""
import locale
print(locale.getpreferredencoding())

"""
mode常用的三种基础访问模式
r:只读模式,默认模式,如果文件不存在,则会报错 r的全称是read
w:只写模式,如果文件不存在,则会创建一个新文件,如果文件已经存在,则会清空文件中的内容 w的全称是write
a:追加模式,如果文件不存在,则会创建一个新文件,如果文件已经存在,则会在文件末尾追加内容 a的全称是append
"""

# 以下是一些基本的示例：
# read()方法
# num表示要从文件中读取的数据的长度（单位是字节）,如果没有传入num,那么就表示读取文件中所有的数据。
# 1.读取整个文件：
f = open('file.txt', 'r',encoding="UTF-8")
content = f.read()
print(content)
f.close()
# 2.按行读取文件：
f = open('file.txt', 'r',encoding="UTF-8")
for line in f:
    print(line, end='')
f.close()
print()
# 3.读取文件的前n个字符：
f = open('file.txt', 'r',encoding="UTF-8")
content = f.read(5)
print(content)
f.close()

# readline()方法
# readlines可以按照行的方式把整个文件中的内容进行一次性读取,并且返回的是一个列表,其中每一行的数据为一个元素。
f = open('file.txt',encoding="UTF-8")
content = f.readlines()

# 输出列表中的每一行
print(content)

# 关闭文件
f.close()

# for循环读取文件行
for line in open("file.txt", "r",encoding="UTF-8"):
    print(line)

# 每一个line临时变量,就记录了文件的一行数据

# close() 关闭文件对象

f = open("file.txt", "r",encoding="UTF-8")

f.close()

# 最后通过close,关闭文件对象,也就是关闭对文件的占用
# 如果不调用close,同时程序没有停止运行,那么这个文件将一直被Python程序占用。

# with open 语法
with open("file.txt", "r",encoding="UTF-8") as f:
    f.readlines()

# 通过在with open的语句块中对文件进行操作
# 可以在操作完成后自动关闭close文件,避免遗忘掉close方法

"""
课后练习：单词计数

通过Windows的文本编辑器软件,将如下内容,复制并保存到:task.txt,文件可以存储在任意位置
wwhds itcast python
wwhds python itcast
beijing shanghai wwhds
shenzhen guangzhou wwhds
wuhan hangzhou wwhds
zhengzhou bigdata wwhds
通过文件读取操作,读取此文件,统计wwhds单词出现的次数
"""
f = open("单词计数.txt", "r",encoding="UTF-8")
content = f.read()
result = content.split()
print(result.count("wwhds"))






