# Solving Questions With Brainpower
# O(n) time, O(n) space
def mostPoints(self, questions: List[List[int]]) -> int:
    n = len(questions)
    dp = [0 for _ in range(n)]
    dp[n-1] = questions[n-1][0]
    for i in range(n-2,-1,-1):
        point = questions[i][0]; brainPower = questions[i][1]
        dp[i] = point
        if i+brainPower+1 < n:
            dp[i] += dp[i+brainPower+1]
        dp[i] = max(dp[i], dp[i+1])
    return dp[0]