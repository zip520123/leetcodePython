# First Unique Character in a String
# O(n), O(1)
def firstUniqChar(self, s: str) -> int:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    for i in range(len(s)):
        if memo[s[i]] == 1:
            return i
    return -1