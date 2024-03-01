# Maximum Odd Binary Number
# O(n), O(n)
def maximumOddBinaryNumber(self, s: str) -> str:
    l, r = 0, len(s)-1
    s = list(s)
    while l<r:
        if s[l] == "1":
            s[l], s[r] = s[r], s[l]
            break
        l += 1
    l = 0
    r = 0
    while r<len(s)-1:
        if s[r] == "1":
            s[l], s[r] = s[r], s[l]
            l += 1
        r += 1
    return "".join(s)