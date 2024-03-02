# Count Binary Substrings
# O(n), O(1)
def countBinarySubstrings(self, s: str) -> int:
    res = 0
    n = len(s)
    for i in range(n-1):
        if s[i] == "0" and s[i+1] == "1":
            l, r = i, i+1
            while l>=0 and r<n and s[l] == "0" and s[r] == "1":
                res += 1
                l -= 1
                r += 1
        if s[i] == "1" and s[i+1] == "0":
            l, r = i, i+1
            while l>=0 and r<n and s[l] == "1" and s[r] == "0":
                res += 1
                l -= 1
                r += 1
    return res

# O(n), O(n)
def countBinarySubstrings(self, s: str) -> int:
    res = 0
    n = len(s)
    arr = []
    curr = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            arr.append(curr)
            curr = 1
        else:
            curr += 1
    arr.append(curr)
    for i in range(len(arr) - 1):
        res += min(arr[i], arr[i+1])
    return res

# O(n), O(1)
def countBinarySubstrings(self, s: str) -> int:
    res = 0
    n = len(s)
    prev, curr = 0, 1
    for i in range(1,n):
        if s[i-1] != s[i]:
            res += min(prev, curr)
            prev, curr = curr, 1
        else:
            curr += 1

    return res + min(prev, curr)
