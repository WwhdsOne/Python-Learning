"""
Python的第三方包是由Python社区的开发者创建并分享的代码库,你可以使用这些代码库来扩展Python的功能。
Python的第三方包通常会被发布到Python包索引(PyPI)上,你可以使用pip(Python的包管理器)来安装这些包。
安装第三方包
你可以使用pip的install命令来安装第三方包。例如,如果你想安装名为requests的包,你可以在命令行(cmd)中输入以下命令:
pip install requests
"""

# 使用第三方包
# 安装完第三方包后,你可以在你的Python脚本中导入并使用这个包。例如,你可以使用requests包来发送HTTP请求:
import requests

response = requests.get('https://www.python.org')
print(response.status_code)

# 更新第三方包
# pip install --upgrade requests

# 卸载第三方包
# pip uninstall requests

"""
在Python程序的生态中,有许多非常多的第三方包(非Python官方),可以极大的帮助我们提高开发效率,如:
科学计算中常用的:numpy包
数据分析中常用的:pandas包
大数据计算中常用的:pyspark、apache-flink包
图形可视化常用的:matplotlib、pyecharts
人工智能常用的:tensorflow
等

由于pip是连接的国外的网站进行包的下载,所以有的时候会速度很慢。

我们可以通过如下命令，让其连接国内的网站进行包的安装：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称
"""