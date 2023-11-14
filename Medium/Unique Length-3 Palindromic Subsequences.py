# Unique Length-3 Palindromic Subsequences
# O(n), O(1)
def countPalindromicSubsequence(self, s: str) -> int:
    charL, charR = {}, {}
    res = 0
    for i, char in enumerate(s):
        if char not in charL:
            charL[char] = i
        charR[char] = i
    
    for key, l in charL.items():
        r = charR[key]
        middleChars = set()
        for i in range(l+1,r):
            middleChars.add(s[i])
        res += len(middleChars)
    return res