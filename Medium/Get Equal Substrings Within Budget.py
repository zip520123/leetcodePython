# Get Equal Substrings Within Budget
# O(n), O(n)
def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    res = 0
    curr = maxCost
    l, r = 0, 0
    while r<len(s):
        cost = abs(ord(s[r]) - ord(t[r]))
        while cost > curr:
            curr += abs(ord(s[l]) - ord(t[l]))
            l += 1
        curr -= cost
        res = max(res, r-l+1)
        r += 1
    return res