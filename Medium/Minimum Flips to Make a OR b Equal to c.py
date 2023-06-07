# Minimum Flips to Make a OR b Equal to c
# O(n), O(n)
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0 

        while a > 0 or b > 0 or c > 0:
            res += check(a&1,b&1,c&1)
            a = a>>1
            b = b>>1
            c = c>>1
        return res

def check(a,b,c) -> int:
    if c == 0:
        return a+b
    if c == 1:
        if a==0 and b==0:
            return 1
    return 0 