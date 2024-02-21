import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 打开文件
f_us = open("./折线图数据/美国.txt", "r", encoding="UTF-8")
f_jp = open("./折线图数据/日本.txt", "r", encoding="UTF-8")
f_in = open("./折线图数据/印度.txt", "r", encoding="UTF-8")
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()

# json转为python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend key
us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]
# 获取日期数据
us_x_data = us_trend_data["updateDate"][:314]
# 获取确诊数量数据
us_y_data = us_trend_data["list"][0]["data"]
jp_y_data = jp_trend_data["list"][0]["data"]
in_y_data = in_trend_data["list"][0]["data"]
# 生成图表
line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度", in_y_data, label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
)

line.render()

f_us.close()
f_jp.close()
f_in.close()
