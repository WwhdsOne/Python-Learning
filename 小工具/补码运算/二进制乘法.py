def binary_multiplication(num1, num2):
    # 检查数字是否为负数
    negative = num1.startswith('-') ^ num2.startswith('-')

    # 如果存在，删除负号
    num1 = num1[1:] if num1.startswith('-') else num1
    num2 = num2[1:] if num2.startswith('-') else num2

    # 将数字分为整数部分和小数部分
    int_part1, frac_part1 = num1.split('.')
    int_part2, frac_part2 = num2.split('.')

    # 将二进制小数转换为整数
    int_num1 = int(int_part1, 2) + int(frac_part1, 2) / (2**len(frac_part1))
    int_num2 = int(int_part2, 2) + int(frac_part2, 2) / (2**len(frac_part2))

    # 乘以整数
    result = int_num1 * int_num2

    # 将结果转换回二进制小数
    binary_result = bin(int(result))[2:] + '.' + bin(int((result % 1) * 2**len(frac_part1 + frac_part2)))[2:]

    # 如果结果为负数，添加负号
    binary_result = '-' + binary_result if negative else binary_result

    return binary_result

# 示例使用
num1 = "-0.1101"
num2 = "0.1011"
result = binary_multiplication(num1, num2)
print(result) 