# Find Longest Special Substring That Occurs Thrice I
# O(n^3), O(n^2)
def maximumLength(self, s: str) -> int:
    memo = defaultdict(int)
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                memo[s[i:j+1]] += 1
            else:
                break
    res = -1
    
    for key, val in memo.items():
        if val >= 3:
            res = max(res, len(key))
    
    return res

# O(n^2), O(n)
def maximumLength(self, s: str) -> int:
    memo = defaultdict(int)
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                memo[(s[i],j-i+1)] += 1
            else:
                break
    res = -1
    for key, val in memo.items():
        if val >= 3:
            res = max(res, key[1])
    
    return res