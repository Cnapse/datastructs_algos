#Program to count numbers of 1 bits in a given int

def count_bits(x : int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1

    return num_bits

# 0110
# 0110 & 1 = 0
# 011 & 1 = 1
# 01 & 1 = 1
# 0 & 1 = 0
# num_bits = 2

x = 8
print(count_bits(x))