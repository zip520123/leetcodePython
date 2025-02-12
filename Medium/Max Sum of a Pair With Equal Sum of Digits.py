# Max Sum of a Pair With Equal Sum of Digits
# O(n), O(n)
def maximumSum(self, nums: List[int]) -> int:
    res = -1
    memo = {}
    for n in nums:
        temp = n
        digit = 0
        while temp:
            digit += temp % 10
            temp //= 10
        if digit in memo:
            res = max(res, n + memo[digit])
            memo[digit] = max(memo[digit], n)
        else:
            memo[digit] = n
    return res