def display_number_info(num):
    binary = bin(num)[2:]  # 转换为二进制字符串
    unsigned_decimal = num  # 无符号十进制整数
    hexadecimal = hex(num)[2:]  # 转换为十六进制字符串
    signed_decimal = num if num < 2**31 else num - 2**32  # 转换为有符号十进制整数
    return binary, unsigned_decimal, hexadecimal, signed_decimal

num = int(input("请输入一个无符号整数: "))
binary, unsigned_decimal, hexadecimal, signed_decimal = display_number_info(num)
print(f"二进制表示: {binary}")
print(f"无符号十进制: {unsigned_decimal}")
print(f"十六进制: {hexadecimal}")
print(f"有符号十进制: {signed_decimal}")