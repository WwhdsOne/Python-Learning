import json


class sales_data:
    def __init__(self, date, order_id, sales, province):
        self.date = date
        self.order_id = order_id
        self.sales = sales
        self.province = province


sales_data_january_dict = {}
sales_data_february_dict = {}
with open("./数据/2011年1月销售数据.txt", "r", encoding="UTF-8") as f:
    data = f.readlines()
    for i in data:
        tmp = i.split(",")
        if tmp[0] not in sales_data_january_dict:
            sales_data_january_dict[tmp[0]] = int(tmp[2])
        else:
            sales_data_january_dict[tmp[0]] += int(tmp[2])
with open("./数据/2011年2月销售数据JSON.txt", "r", encoding="UTF-8") as f:
    data = f.readlines()
    for i in data:
        tmp = json.loads(i)
        if tmp["date"] not in sales_data_february_dict:
            sales_data_february_dict[tmp["date"]] = int(tmp["money"])
        else:
            sales_data_february_dict[tmp["date"]] += int(tmp["money"])
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar_january = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT,width="1300px"))
bar_january.add_xaxis(list(sales_data_january_dict.keys()))
bar_january.add_yaxis(
    "1月销售额",
    list(sales_data_january_dict.values()),
    label_opts=opts.LabelOpts(position="top",font_size=10),
    
)
# 设置标题
bar_january.set_global_opts(
    title_opts=opts.TitleOpts(title="2011年1月销售额"),
    
)
bar_january.render("2011年1月销售额.html")

bar_february = Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION,width="1300px"))
bar_february.add_xaxis(list(sales_data_february_dict.keys()))
bar_february.add_yaxis(
    "2月销售额",
    list(sales_data_february_dict.values()),
    label_opts=opts.LabelOpts(position="top",font_size=10),
    
)
# 设置标题
bar_february.set_global_opts(
    title_opts=opts.TitleOpts(title="2011年2月销售额"),
    
)
bar_february.render("2011年2月销售额.html")
