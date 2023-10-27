# Longest Palindromic Substring
# O(n^2), O(1)
def longestPalindrome(self, s: str) -> str:
    index, length = 0, 0
    n = len(s)
    for i in range(n):
        l = r = i
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        if r-l+1 > length:
            length = r-l+1
            index = l
        l, r = i, i+1
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        if r-l+1 > length:
            length = r-l+1
            index = l
    return s[index: index+length]