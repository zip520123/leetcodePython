# Minimum Deletions to Make String Balanced
# O(n), O(n)
def minimumDeletions(self, s: str) -> int:
    n = len(s)
    count_a = [0] * n
    count_b = [0] * n
    b_count = 0
    for i in range(n):
        count_b[i] = b_count
        if s[i] == "b": 
            b_count += 1
    a_count = 0
    for i in range(n-1, -1, -1):
        count_a[i] = a_count
        if s[i] == "a":
            a_count += 1
    res = n
    for i in range(n):
        res = min(res, count_a[i]+count_b[i])
    return res

# O(n), O(n), stack
def minimumDeletions(self, s: str) -> int:
    n = len(s)
    stack = []
    res = 0
    for char in s:
        if stack and stack[-1] == "b" and char == "a":
            stack.pop()
            res += 1
        else:
            stack.append(char)
    return res

# O(n), O(n), dp
def minimumDeletions(self, s: str) -> int:
    n = len(s)
    dp = [0] * (n+1)
    b_count = 0
    for i in range(n):
        if s[i] == "b":
            dp[i+1] = dp[i]
            b_count += 1
        else:
            dp[i+1] = min(dp[i]+1, b_count)
    return dp[n]

# O(n), O(1), dp
def minimumDeletions(self, s: str) -> int:
    n = len(s)
    dp = 0
    b_count = 0
    for i in range(n):
        if s[i] == "b":
            b_count += 1
        else:
            dp = min(dp+1, b_count)
    return dp