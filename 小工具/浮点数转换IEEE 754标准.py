import struct

def float_to_ieee754(num):
    return bin(int.from_bytes(struct.pack('f', num), 'big'))[2:].zfill(32)

num = float(input("请输入一个浮点数: "))
ieee754 = float_to_ieee754(num)
print(f"IEEE 754表示: {ieee754[::-1]}")

def float_to_binary(num):
    whole, dec = str(num).split(".")
    whole = int(whole)
    dec = int(dec)
    res = bin(whole).lstrip("0b") + "."

    while dec:
        whole, dec = str((decimal_converter(dec)) * 2).split(".")
        dec = int(dec)
        res += whole
    return res

def decimal_converter(num): 
    while num > 1:
        num /= 10
    return num
binary_num = float_to_binary(num)
print(f"二进制小数: {binary_num}")