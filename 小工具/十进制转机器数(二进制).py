import struct

hex_num = "C6400000"
bytes_num = bytes.fromhex(hex_num)
float_num = struct.unpack('!f', bytes_num)[0]

print(float_num)