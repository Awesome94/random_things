def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1 
    return result

print(parity(1011))