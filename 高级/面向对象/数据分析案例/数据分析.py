import json
class sales_data:
    def __init__(self, date,order_id,sales,province):
        self.date = date
        self.order_id = order_id
        self.sales = sales
        self.province = province
sales_data_january_dict = {}
sales_data_february_dict = {}
with open("./数据/2011年1月销售数据.txt","r",encoding="UTF-8") as f:
    data = f.readlines()
    for i in data:
        tmp = i.split(",")
        if tmp[0] not in sales_data_january_dict:
            sales_data_january_dict[tmp[0]] = int(tmp[2])
        else:
            sales_data_january_dict[tmp[0]] += int(tmp[2])
with open("./数据/2011年2月销售数据JSON.txt","r",encoding="UTF-8") as f:       
    data = f.readlines()
    for i in data:
        tmp = json.loads(i)
        if tmp["date"] not in sales_data_february_dict:
            sales_data_february_dict[tmp["date"]] = int(tmp["money"])
        else:
            sales_data_february_dict[tmp["date"]] += int(tmp["money"])
print(sales_data_january_dict)
    

    