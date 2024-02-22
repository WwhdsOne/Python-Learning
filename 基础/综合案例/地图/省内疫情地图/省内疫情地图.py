import json

with open("./地图数据/疫情.txt", "r", encoding="UTF-8") as f:
    data = json.loads(f.read())

# 获取各省数据
data = data["areaTree"][0]["children"]
for i in data:
    if "河北" == i["name"]:
        data = i["children"]
data_list = []

# 循环data元素，将省和数据封装到data_list中
for city_data in data:
    city_name = city_data["name"]
    city_confirm = city_data["total"]["confirm"]
    # 添加数据
    data_list.append((city_name + "市", city_confirm))

print(data_list)

from pyecharts.charts import Map
from pyecharts.options import *

virus_map = Map()
virus_map.add("河北各市确诊人数", data_list, "河北")
virus_map.set_global_opts(
    title_opts=TitleOpts(title="河北疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "99-499人", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "499-999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
            {"min": 10000, "label": "10000以上", "color": "#990033"},
        ],
    )
)

virus_map.render("河北疫情地图.html")
