# Number Complement
# O(n), O(1)
def findComplement(self, num: int) -> int:
    res = 0
    p = 0
    while num:
        if num & 1 == 0:
            res += 2 ** p
        p += 1
        num >>= 1
    return res