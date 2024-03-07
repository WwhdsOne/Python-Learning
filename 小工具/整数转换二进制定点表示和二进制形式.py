def fixed_point_representation(num, bit_count):
    # 计算阶码
    exponent = 0
    while num >= 2:
        num /= 2
        exponent += 1

    # 转换为二进制
    binary = bin(int(num * (2 ** (bit_count - 1))))[2:]

    # 补齐位数
    while len(binary) < bit_count:
        binary = '0' + binary

    return binary, exponent

num = int(input("请输入一个整数: "))
bit_count = int(input("请输入数值位数: "))
binary, exponent = fixed_point_representation(num, bit_count)
print(f"二进制形式定点表示: {binary}")
print(f"阶码: {exponent}")