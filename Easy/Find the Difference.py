# Find the Difference
# O(s+t), O(s)
def findTheDifference(self, s: str, t: str) -> str:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    for char in t:
        memo[char] -= 1
        if memo[char] < 0:
            return char
    return ""
