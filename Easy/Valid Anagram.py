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

# O(n), O(n)
def isAnagram(self, s: str, t: str) -> bool:
    arr1 = [0] * 26
    arr2 = [0] * 26
    for char in s:
        arr1[ord(char)-ord("a")] += 1
    for char in t:
        arr2[ord(char)-ord("a")] += 1
    for i in range(26):
        if arr1 != arr2:
            return False
    return True