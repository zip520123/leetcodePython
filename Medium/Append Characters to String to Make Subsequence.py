# Append Characters to String to Make Subsequence
# O(s+t), O(1)
def appendCharacters(self, s: str, t: str) -> int:
    l, r = 0,0
    while l<len(s) and r < len(t):
        if s[l] == t[r]:
            r += 1
        l += 1
    return len(t)-r
