# 1. 打开文件,通过a模式打开即可
f = open('file.txt', 'a',encoding="UTF-8")

# 2.文件写入
f.write('hello world')

# 3. 内容刷新
f.flush()

"""
a模式,文件不存在会创建文件
a模式,文件存在会在最后,追加写入文件
"""
