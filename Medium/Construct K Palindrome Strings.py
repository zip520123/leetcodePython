# Construct K Palindrome Strings
# O(n), O(n)
def canConstruct(self, s: str, k: int) -> bool:
    if len(s) < k:
        return False
    odd = 0
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    for key, val in memo.items():
        if val % 2 == 1:
            odd += 1
    if odd > k:
        return False
    return True