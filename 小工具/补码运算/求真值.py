def twos_complement(value, bits):
    if value < 0:
        value = (1 << bits) + value
    return format(value, '0' + str(bits) + 'b')

def multiply(a, b):
    a_bin = twos_complement(a, 8)
    b_bin = twos_complement(b, 8)
    result = 0
    for i in range(8):
        if a_bin[-(i+1)] == '1':
            result += int(b_bin, 2) << i
    return result if result < (1 << 7) else result - (1 << 8)

print(multiply(114, 7))  # 输出：-42