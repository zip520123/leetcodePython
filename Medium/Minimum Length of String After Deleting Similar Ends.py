# Minimum Length of String After Deleting Similar Ends
# O(n), O(1)
def minimumLength(self, s: str) -> int:
    l, r = 0, len(s)-1
    while l<r and s[l] == s[r]:
        while l+1<r and s[l+1] == s[r]:
            l += 1
        while l<r-1 and s[l] == s[r-1]:
            r -= 1
        l += 1
        r -= 1
    return r-l+1