from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar()
# 添加x轴数据
bar.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据,并且数值标签在右侧
bar.add_yaxis("GDP",[20,25,5],label_opts=opts.LabelOpts(position="right"));
# 反转x轴y轴
bar.reversal_axis()

bar.render("bar.html")