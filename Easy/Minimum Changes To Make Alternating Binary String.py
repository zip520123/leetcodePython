# Minimum Changes To Make Alternating Binary String
# O(n), O(n)
def minOperations(self, s: str) -> int:
    n = len(s)
    mask1 = []
    for i in range(n):
        if i % 2 == 0:
            mask1.append("0")
        else:
            mask1.append("1")

    mask2 = []
    for i in range(n):
        if i % 2 == 0:
            mask2.append("1")
        else:
            mask2.append("0")
    
    res1, res2 = 0, 0
    for i in range(n):
        if mask1[i] != s[i]: res1 += 1
        if mask2[i] != s[i]: res2 += 1
    return min(res1, res2)