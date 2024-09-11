# Minimum Bit Flips to Convert Number
# O(n), O(1)
def minBitFlips(self, start: int, goal: int) -> int:
    res = 0
    while start or goal:
        l = start & 1
        r = goal & 1
        if l ^ r:
            res += 1
        start >>= 1
        goal >>= 1
    return res