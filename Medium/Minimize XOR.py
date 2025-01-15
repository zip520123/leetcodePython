# Minimize XOR
# O(1), O(1)
def minimizeXor(self, num1: int, num2: int) -> int:
    bits_count = 0
    while num2:
        bits_count += num2 % 2
        num2 >>= 1

    res = 0
    
    for i in range(32, -1, -1):
        if (num1 & (2 ** i)) and bits_count:
            bits_count -= 1
            res += 2 ** i
    for i in range(32):
        if num1 & 2 ** i == 0 and bits_count:
            res += 2 ** i
            bits_count -= 1
    return res