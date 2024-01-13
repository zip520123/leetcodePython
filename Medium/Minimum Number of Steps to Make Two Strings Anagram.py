# Minimum Number of Steps to Make Two Strings Anagram
# O(n), O(n)
def minSteps(self, s: str, t: str) -> int:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    for char in t:
        memo[char] -= 1
    res = 0
    for _, val in memo.items():
        res += abs(val)
    return res // 2