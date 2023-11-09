# Count Number of Homogenous Substrings
# O(n), O(1)
def countHomogenous(self, s: str) -> int:
    res = 0
    count = 0
    for i in range(len(s)):
        if i==0 or s[i] == s[i-1]:
            count += 1
        else:
            count = 1
        res = (res + count) % (10 ** 9 + 7)
    return res