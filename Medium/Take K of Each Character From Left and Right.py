# Take K of Each Character From Left and Right
# O(2^n), O(n), TLE
def takeCharacters(self, s: str, k: int) -> int:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    for char in "abc":
        if memo[char] < k:
            return -1
    @cache
    def dfs(path, l, r) -> int:
        memo = defaultdict(int)
        for char in path:
            memo[char] += 1
        if l>r or (memo["a"] >= k and memo["b"] >= k and memo["c"] >= k):
            return 0
        curr = math.inf
        curr = min(curr, dfs(path + s[l], l+1, r) + 1)
        curr = min(curr, dfs(path + s[r], l, r-1) + 1)
        return curr
    return dfs("", 0, len(s)-1)

# O(n), O(1)
def takeCharacters(self, s: str, k: int) -> int:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    for char in "abc":
        if memo[char] < k:
            return -1
    max_window = 0
    l, r = 0, 0
    while r < len(s):
        memo[s[r]] -= 1
        while memo[s[r]] < k:
            memo[s[l]] += 1
            l += 1
        max_window = max(max_window, r-l+1)
        r += 1
    return len(s) - max_window