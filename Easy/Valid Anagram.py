# Valid Anagram
# O(s+t), O(s)
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t): return False
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    for char in t:
        memo[char] -= 1
        if memo[char] < 0: return False
    return True