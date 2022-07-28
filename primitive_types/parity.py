# compute parity of a word



def parity(x : int) -> int:
    res = 0
    while x:
        res ^= x & 1
        x >>= 1
    return res

def parity_lowbitclear(x : int) -> int:
    res = 0
    while x:
        res ^= 1
        x &= x-1
    return res


x = int(1)
print(parity_lowbitclear(x))