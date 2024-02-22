# Timeline()-时间线
# 柱状图描述的是分类数据，回答的是每一个分类中『有多少？』这个问题.
# 这是柱状图的主要特点,同时柱状图很难动态的描述一个趋势性的数据. 这里pyecharts为我们提供了一种解决方案-时间线
from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar1 = Bar()
# 添加x轴数据
bar1.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据,并且数值标签在右侧
bar1.add_yaxis("GDP", [20, 25, 5], label_opts=opts.LabelOpts(position="right"))
# 反转x轴y轴
bar1.reversal_axis()
# 生成折线图

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [25, 30, 4], label_opts=opts.LabelOpts(position="right"))
bar2.reversal_axis()

# 创建时间线,并添加主题
timeline = Timeline(
    {"theme": "infographic"}
)
# timeline对象添加bar柱状图
timeline.add(bar1, "2019年")
timeline.add(bar2, "2020年")
# 设置自动播放
timeline.add_schema(
    play_interval=1000, is_timeline_show=True, is_auto_play=True, is_loop_play=True
)
# 渲染
timeline.render("timeline.html")
