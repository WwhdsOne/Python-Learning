import json

with open("./地图数据/疫情.txt", "r", encoding="UTF-8") as f:
    data = json.loads(f.read())

# 获取各省数据
data = data["areaTree"][0]["children"]

data_list = []

# 循环data元素，将省和数据封装到data_list中
for province_data in data:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    # 添加数据
    if "广西" in province_name:
        data_list.append((province_name + "壮族自治区", province_confirm))
    elif "内蒙古" in province_name:
        data_list.append((province_name + "自治区", province_confirm))
    elif "新疆" in province_name:
        data_list.append((province_name + "维吾尔自治区", province_confirm))
    elif "宁夏" in province_name:
        data_list.append((province_name + "回族自治区", province_confirm))
    elif "西藏" in province_name:
        data_list.append((province_name + "自治区", province_confirm))
    elif "香港" in province_name:
        data_list.append((province_name[:-1:] + "特别行政区", province_confirm))
    elif "澳门" in province_name:
        data_list.append((province_name[:-1:] + "特别行政区", province_confirm))
    elif "北京" in province_name:
        data_list.append((province_name + "市", province_confirm))
    elif "天津" in province_name:
        data_list.append((province_name + "市", province_confirm))
    elif "上海" in province_name:
        data_list.append((province_name + "市", province_confirm))
    elif "重庆" in province_name:
        data_list.append((province_name + "市", province_confirm))
    else:
        data_list.append((province_name + "省", province_confirm))

print(data_list)

from pyecharts.charts import Map
from pyecharts.options import *

virus_map = Map()
virus_map.add("各省份确诊人数", data_list, "china")
virus_map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
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

virus_map.render("国内疫情地图.html")
