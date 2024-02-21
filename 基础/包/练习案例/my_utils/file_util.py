def print_file_info(file_name):
    try:
        f = open(file_name, 'r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError as e:
        print("")
    else:
        f.close()
def append_to_file(file_name, data):
    try:
        f = open(file_name, 'a',encoding='utf-8')
        f.write(data)
    except FileNotFoundError as e:
        print("错误信息:",e)
    else:
        f.close()