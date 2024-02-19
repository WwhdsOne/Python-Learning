print(
    "对于单个字符的编码,Python提供了ord()函数获取字符的整数表示,chr()函数把编码转换为对应的字符"
)
print(ord("中"))
print(chr(20013))


print("Python对 bytes类型的数据用带b前缀的单引号或双引号表示")
print(b"abc")
print("ABC".encode("ascii"))

print("在bytes中,无法显示为ASCII字符的字节,用\\x##显示。")
print("中文".encode("utf-8"))

print("要把bytes变为str,就需要用decode()方法")
print(b"ABC".decode("ascii"))

print("如果bytes中只有一小部分无效的字节,可以传入errors='ignore'忽略错误的字节")
print(b"\xe4\xb8\xad\xff".decode("utf-8", errors="ignore"))

print("要计算str包含多少个字符,可以用len()函数")
print(len("ABC"))


print("在Python中,采用的格式化方式和C语言是一致的,用%实现")
print("Hello,%s" % "world")
print("Hi,%s,you have ￥%d" % ("Wwhds", 10086))

print("如果你不太确定应该用什么,%s永远起作用,它会把任何数据类型转换为字符串")
print("Age:%s" % 25)

print(
    "另一种格式化字符串的方法是使用字符串的format()方法,"
    "它会用传入的参数依次替换字符串内的占位符{0}、{1}……"
    "不过这种方式写起来比%要麻烦得多"
)
print("Hello, {0}, 成绩提升了 {1:.1f}%".format("小明", 17.125))

print(
    "最后一种格式化字符串的方法是使用以f开头的字符串,"
    "称之为f-string,它和普通字符串不同之处在于,"
    "字符串如果包含{xxx},就会以对应的变量替换"
)
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
