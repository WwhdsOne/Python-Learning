# 导包
from pyecharts.charts import Line 
# 创建对象
line = Line()
# 添加x轴数据
line.add_xaxis(['周一', '周二', '周三', '周四', '周五', '周六', '周日'])
# 添加y轴数据
line.add_yaxis('生命力', [0, 0, -1, -2, 10, 15, 233])
# 生成图表
line.render()
