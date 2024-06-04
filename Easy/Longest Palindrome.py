# Longest Palindrome
# O(n), O(n)
def longestPalindrome(self, s: str) -> int:
    res = 0
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    oddFlag = False
    for _, val in memo.items():
        if val % 2 == 1:
            if oddFlag == False:
                res += val
                oddFlag = True
            else:
                res += val - 1
        else:
            res += val
    return res