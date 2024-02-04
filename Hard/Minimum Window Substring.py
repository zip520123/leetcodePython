# Minimum Window Substring
# O(n), O(n)
def minWindow(self, s: str, t: str) -> str:
    memo = defaultdict(int)
    count = len(t)
    for char in t:
        memo[char] += 1
    l, r = 0, 0
    index, length = 0, math.inf
    while r < len(s):
        char = s[r]
        memo[char] -= 1
        if memo[char] >= 0:
            count -= 1
            while count == 0:
                if r-l+1 < length:
                    length = r-l+1
                    index = l
                leftChar = s[l]
                memo[leftChar] += 1
                l += 1
                if memo[leftChar] > 0:
                    count += 1
        r += 1
    if length == math.inf:
        return ""
    return s[index: index+length] 