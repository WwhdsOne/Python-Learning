def binary_to_codes(binary):
    # 分割二进制字符串为整数部分和小数部分
    integer_part = binary
    # 整数部分转换为原码、反码和补码
    if integer_part[0] == '0':  # 正数
        integer_original = integer_inverse = integer_complement = integer_part
    else:  # 负数
        integer_original = integer_part
        integer_inverse = '1' + ''.join('0' if bit == '1' else '1' for bit in integer_part[1:])
        inverse_real = bin(int(integer_inverse[1:], 2)+1)[2:]
        integer_complement = bin(int(integer_inverse[1:], 2) + 1)[-len(inverse_real):]
    original = integer_original 
    inverse = integer_inverse
    complement = integer_complement
    return original, inverse, complement,complement
binary = input("请输入一个二进制数: ")
original, inverse, complement, offset_code = binary_to_codes(binary)
print(f"无符号十进制: {int(binary, 2)}")
print(f"原码: {original}十进制: {"-" if binary[0] == "1" else "+"}{int(original[1:],2)} ")
print(f"反码: {inverse}十进制: {"-" if binary[0] == "1" else "+"}{int(inverse[1:],2)}")
print(f"补码: {complement}十进制: {"-" if binary[0] == "1" else "+"}{int(complement,2)}")
print(f"移码: {offset_code}十进制: {"+" if binary[0] == "1" else "-"}{int(offset_code,2)}")
