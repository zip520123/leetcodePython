# Is Subsequence
# O(n), O(1)
def isSubsequence(self, s: str, t: str) -> bool:
    if s == "": return True
    l = 0
    for char in t:
        if s[l] == char:
            l += 1
        if l == len(s):
            return True
    return False