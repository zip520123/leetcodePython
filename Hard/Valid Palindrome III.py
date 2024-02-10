# Valid Palindrome III
# O(n^2), O(n^2) distence between its reversed str divied by 2
def isValidPalindrome(self, s: str, k: int) -> bool:
    n = len(s)
    dp = [[0]*(n+1) for _ in range(n+1) ]
    for i in range(1,n+1):
        dp[0][i] = dp[0][i-1] + 1
        dp[i][0] = dp[i-1][0] + 1
    s2 = ""
    for i in range(n-1, -1, -1):
        s2 += s[i]
    for i in range(1,n+1):
        for j in range(1, n+1):
            if s[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

    return dp[n][n] // 2 <= k

# O(n^2), O(n^2) Longest Palindromic Subsequence
def isValidPalindrome(self, s: str, k: int) -> bool:
    n = len(s)
    dp = [[0]*(n+1) for _ in range(n+1) ]
    s2 = ""
    for i in range(n-1, -1, -1):
        s2 += s[i]
    for i in range(1,n+1):
        for j in range(1, n+1):
            if s[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return n - dp[n][n] <= k