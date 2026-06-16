# Valid Palindrome
# O(n), O(1)
def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s)-1
    s = s.lower()
    
    while  l<r:
        while l<len(s) and s[l] not in "abcdefghijklmnopqrstuvwxyz0123456789":
            l += 1
        while r>=0 and s[r] not in "abcdefghijklmnopqrstuvwxyz0123456789":
            r -= 1
        if l<len(s) and r>=0 and s[l] == s[r]:
            l += 1
            r -= 1
        else:
            break
    return l>=r