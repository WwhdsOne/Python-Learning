"""
正则表达式,又称规则表达式(Regular Expression),
是使用单个字符串来描述、匹配某个句法规则的字符串,常被用来检索、替换那些符合某个模式（规则）的文本。
简单来说,正则表达式就是使用：字符串定义规则,并通过规则去验证字符串是否匹配。
比如,验证一个字符串是否是符合条件的电子邮箱地址,只需要配置好正则规则,即可匹配任意邮箱。
比如通过正则规则： (^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$)  即可匹配一个字符串是否是标准邮箱格式
但如果不使用正则,使用if else来对字符串做判断就非常困难了。

Python正则表达式,使用re模块,并基于re模块中三个基础方法来做正则匹配。
分别是:match、search、findall 三个基础方法


"""

# re.match(匹配规则, 被匹配字符串)
# 从被匹配字符串开头进行匹配, 匹配成功返回匹配对象（包含匹配的信息）,匹配不成功返回空。
import re
s = "hello world 123 hello world 123 hello world 123 hello world 456"
result = re.match("hello",s) 
print(result) # 输出 <re.Match object; span=(0, 5), match='hello'>
print(result.span()) # 输出 (0, 5)
print(result.group()) # 输出 hello
s = "1hello world 123 hello world 123 hello world 123 hello world 456"
result = re.match("hello",s)
print(result) # 输出 None
# re.search(匹配规则, 被匹配字符串)
# 整个字符串都找不到，返回None
s = "1hello world 123 hello world 123 hello world 123 hello world 456"
result = re.search("hello",s)
print(result) # 输出 <re.Match object; span=(1, 6), match='hello'>
result = re.search("olleh",s)
print(result) # 输出 None

# re.findall(匹配规则, 被匹配字符串)
s = "hello world 123 hello world 123 hello world 123 hello world 456"
result = re.findall("hello",s)
print(result) # 输出 ['hello', 'hello', 'hello', 'hello']