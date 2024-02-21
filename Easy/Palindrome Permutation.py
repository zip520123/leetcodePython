# Palindrome Permutation
# O(n), O(n)
def canPermutePalindrome(self, s: str) -> bool:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    odd = 0
    for val in memo.values():
        if val % 2 != 0:
            odd += 1
            if odd > 1:
                return False
    return True