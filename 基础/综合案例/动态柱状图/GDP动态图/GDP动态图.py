from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 读取数据
f = open("../动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
lines = f.readlines()
f.close()
# 去除第一条数据
lines.pop(0)
# 将数据添加到字典中
data_dict = {}
for data in lines:
    year_data = data.split(",")
    year = int(year_data[0])
    country = year_data[1]
    gdp = float(year_data[2])
    try:
        data_dict[year].append((country, gdp))
    except KeyError:
        data_dict[year] = []
        data_dict[year].append((country, gdp))
sorted_year_list = sorted(data_dict.keys())
# 时间线生成,并添加主题
timeline = Timeline({"theme": ThemeType.LIGHT})
# 每年gdp数据处理
for year in sorted_year_list:

    data_dict[year].sort(key=lambda x: x[1], reverse=True)
    year_data = data_dict[year][:10]
    countrys = []
    gdps = []
    for country_gdp in year_data:
        countrys.append(country_gdp[0])
        gdps.append(country_gdp[1] / 100000000)
    bar = Bar()
    countrys.reverse()
    gdps.reverse()
    # 添加x轴
    bar.add_xaxis(countrys)
    # 添加y轴
    bar.add_yaxis("GDP(亿)", gdps, label_opts=opts.LabelOpts(position="right"))
    # 反转x轴和y轴
    bar.reversal_axis()
    # 设置标题
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="{}年全球GDP前十国家".format(year))
    )
    # 添加柱状图到时间线
    timeline.add(bar, str(year))
# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000, is_timeline_show=True, is_auto_play=True, is_loop_play=False
)
# 绘图
timeline.render("1960-2019全球GDP前8国家.html")
