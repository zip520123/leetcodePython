# Isomorphic Strings
# O(n), O(n)
def isIsomorphic(self, s: str, t: str) -> bool:
    memo1 = {}
    memo2 = {}
    for i in range(len(s)):
        char1, char2 = s[i], t[i]
        if char1 in memo1 and memo1[char1] != char2:
            return False
        if char2 in memo2 and memo2[char2] != char1:
            return False
        memo1[char1] = char2
        memo2[char2] = char1
    return True