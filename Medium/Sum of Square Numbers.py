# Sum of Square Numbers
# O(log n), O(n)
def judgeSquareSum(self, c: int) -> bool:
    memo = {}
    i = 0
    while i*i <= c:
        memo[i*i] = True
        i += 1
    i -= 1
    while i >= 0:
        if c-i*i in memo:
            return True
        i -= 1
    return False