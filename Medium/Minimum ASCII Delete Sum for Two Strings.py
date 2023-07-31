# Minimum ASCII Delete Sum for Two Strings
# O(s1.len*s2.len), O(s1.len*s2.len)
def minimumDeleteSum(self, s1: str, s2: str) -> int:
    n1 = len(s1); n2 = len(s2)
    dp = [[0 for _ in range(n1+1)] for _ in range(n2+1)]
    def ascii(char) -> int:
        return ord(char)
    for i in range(1,n1+1):
        dp[0][i] = dp[0][i-1] + ascii(s1[i-1])
    for i in range(1,n2+1):
        dp[i][0] = dp[i-1][0] + ascii(s2[i-1])

    for i in range(1,n2+1):
        for j in range(1,n1+1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1] + ascii(s1[j-1]) + ascii(s2[i-1]), \
                                dp[i-1][j] + ascii(s2[i-1]), \
                                dp[i][j-1] + ascii(s1[j-1])
                    )
    return dp[n2][n1]