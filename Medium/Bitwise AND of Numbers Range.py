# Bitwise AND of Numbers Range
# O(1), O(1)
def rangeBitwiseAnd(self, left: int, right: int) -> int:
    res = 0
    for i in range(32):
        if right - left < 2 ** i and (left & 2 ** i) and (right & 2 ** i):
            res += 2 ** i
    return res

# O(1), O(1)
def rangeBitwiseAnd(self, left: int, right: int) -> int:
    count = 0
    while left != right:
        left >>= 1
        right >>= 1
        count += 1
    return left << count