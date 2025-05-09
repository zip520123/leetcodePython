# Minimum Array End
# O(log n), O(1)
def minEnd(self, n: int, x: int) -> int:
    res = x
    n -= 1
    mask = 1
    
    while n > 0:
        if (mask & x) == 0:
            res = res + (n & 1) * mask
            n >>= 1
        mask <<= 1
    return res