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

# O(n), O(n)
def countPalindromicSubsequence(self, s: str) -> int:
    right_chars = defaultdict(int)
    for char in s:
        right_chars[char] += 1
    seen = set()
    left_chars = defaultdict(int)
    for i in range(len(s)):
        curr = s[i]
        right_chars[curr] -= 1
        if i > 0:
            for assci in range(ord("a"), ord("z")+1):
                char = chr(assci)
                if left_chars[char] > 0 and right_chars[char] > 0:
                    seen.add((char, curr, char))
        left_chars[curr] += 1
    return len(seen)

# O(n), O(1)
def countPalindromicSubsequence(self, s: str) -> int:
    left_chars, right_chars = {}, {}
    for i in range(len(s)):
        char = s[i]
        if char not in left_chars:
            left_chars[char] = i
        right_chars[char] = i
    
    res = 0
    for left_char, left_index in left_chars.items():
        right_index = right_chars[left_char]
        middle_chars = set()
        for i in range(left_index+1, right_index):
            middle_chars.add(s[i])
        res += len(middle_chars)
    return res