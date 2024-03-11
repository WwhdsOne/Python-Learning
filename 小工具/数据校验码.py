import math
def generate_parity_code(data, parity='even'):
    # 计算数据中1的个数
    count = data.count('1')

    # 如果选择的是偶校验，并且1的个数是奇数，或者选择的是奇校验，并且1的个数是偶数，那么校验位为1
    if (parity == 'even' and count % 2 != 0) or (parity == 'odd' and count % 2 == 0):
        data += '1'
    else:
        data += '0'
    return data
# 汉明码
def generate_hamming_code(k):
    for i in range(1, 64):
        if 2 ** (i - 1) >= k + i:
            binary = i
            break
        i += 1
    result = [] # list[str]
    # 校验位
    P = []
    # 校验位位置
    P_index = []
    # 数据位
    D = []
    # 数据位位置
    D_index = []
    # 校验位的生成部分
    D_cnt = {}
    # 定义海明码类,内容包括数据位,二进制形式,校验位计算,校验位组
    class hamming_code:
        def __init__(self, data,binary_format,bit_verification_calculation,check_bit_group):
            self.data = data
            self.binary_format = binary_format
            self.bit_verification_calculation = bit_verification_calculation
            self.check_bit_group = check_bit_group
        def __str__(self) -> str:
            return f"数据位:{self.data} 二进制形式:{self.binary_format} 校验位计算:{self.bit_verification_calculation} 校验位组:{self.check_bit_group}"
    for i in range(binary):
        P.append("P" + str(i + 1))
    for i in range(k):
        D.append("D" + str(i + 1))
    j = 0
    o = 0
    # 生成海明码
    for i in range(1, k + binary):
        tmp = ""
        if i == 2 ** j:
            result.append(P[j])
            P_index.append(i)
            j += 1
        else:
            result.append(D[o])
            D_index.append(i)
            o += 1
    if j < len(P):
        result.append(P[j])
        P_index.append(len(result))
    result.reverse()
    f = open("汉明码.md", "a",encoding="UTF-8")
    # 清除原有内容
    f.truncate(0)
    f.write("**汉明码:**")
    for i in range(len(result)):
        if result[i][0] == "P":
            if i == len(result) - 2:
                f.write("`P2P1`")
                break
            else:
                f.write("`" + result[i] + "`")
        else:
            f.write(result[i])
    print("汉明码：", result)
    print("数据位位置：", D_index)
    print("校验位位置：", P_index)
    result.reverse()
    hamming_code_result = []
    # 校验码生成结果字典
    P_result = {}
    # 生成海明码内容类的相关数据
    for i in D_index:
        data_binary = bin(i)[:1:-1]
        tmp_calculate = []
        check_bit_group = []
        tmp_calculate.append(str(i) + " = ")
        for t in range(len(data_binary)):
            if data_binary[t] == '1':
                if len(tmp_calculate) == 1:
                    tmp_calculate.append(str(2 ** t))
                else:
                    tmp_calculate.append(" + "+str(2 ** t))
                check_bit_group.append(result[2 ** t - 1])
        tmp_hamming_code = hamming_code(result[i-1],data_binary[::-1],tmp_calculate,check_bit_group)
        hamming_code_result.append(tmp_hamming_code)
    # 输出汉明码结果类的相关信息
    # 有数据位,二进制形式,校验位计算,校验位组
    f.write("\n| 数据位 | 二进制形式 | 校验位计算 | 校验位组 |\n| :----: | :--------: | :--------: | :------: |")
    for i in hamming_code_result:
        print(i)
        if(i.binary_format.count('1') < binary):
            i.binary_format = "0" * (binary - len(i.binary_format) -1) + i.binary_format
        f.write(f"\n| {i.data} | {i.binary_format} | {''.join(i.bit_verification_calculation)} | {','.join(i.check_bit_group)} |")
    # 数值最大值,保证码距相等
    D_max = 0
    # 获取最大码距并且将其添加到校验码的生成部分
    for i in P_index:
        tmp_list = []
        for t in hamming_code_result:
            for y in t.check_bit_group:
                if y == result[i - 1]:
                    tmp_list.append(t.data)
                    if(D_cnt.get(t.data) == None):
                        D_cnt[t.data] = 1
                    else:
                        D_cnt[t.data] += 1
                    D_max = max(D_max,D_cnt[t.data])
        P_result[result[i - 1]] = tmp_list
    # 输出校验位的生成部分,确认是否正确
    for i in P_result:
        print(i, ":", P_result[i])
    if P_result[result[-1]] == []:
        for i in D_cnt.keys():
            if D_cnt[i] != D_max:
                P_result[result[-1]].append(i)
        P_result[result[-1]].sort()
    # 输出latex的校验码
    f.write("\n\n$$\n")
    # 校验位的形成部分打印
    for i in P_result:
        f.write("\\\\")
        print(i, ":", P_result[i])
        P_result[i].sort(key = lambda x: int(x[1:]))
        for l in range(len(P_result[i])):
            if l == 0:
                f.write(f"{i} = {P_result[i][l]}")
            else:
                f.write(f"\oplus {P_result[i][l]}")
    f.write("\n$$\n")
    f.write("# 校验\n")
    f.write("\n$$\n")
    for i in P_result:
        f.write("\\\\")
        print("S" + i[1:], ":", P_result[i])
        for l in range(len(P_result[i])):
            if l == 0:
                f.write(f"S{i[1:]} = {i} \\oplus {P_result[i][l]}")
            else:
                f.write(f"\\oplus {P_result[i][l]}")
    f.write("\n$$\n")
    f.close()
def calculate_crc(data, divisor):
    # 获取移位位数
    shift_bits = len(divisor) - divisor.find('1') -1
    # 将数据和除数转换为列表，以便进行操作
    data = list(map(int, data))
    data = data + [0] * (len(divisor) - 1)
    # 保存原始数据，以便最后生成CRC码
    original_data = data.copy()
    divisor = list(map(int, divisor))

    # 执行除法操作
    for i in range(len(data) - len(divisor) + 1):
        if data[i] == 1:
            for j in range(len(divisor)):
                data[i+j] ^= divisor[j]
    # 生成CRC码
    crc_code = ''.join(map(str, data[-(len(divisor)-1):]))
    for i in range(len(crc_code)):
        j = int(crc_code[i])
        if j == 1:
            original_data[len(data) - (len(crc_code) - i)] = 1
    print(*original_data)
    print("CRC码:", crc_code)
    return original_data
generate_hamming_code(8)
print(calculate_crc('1100', '1011'))
        
        
    
        

    
