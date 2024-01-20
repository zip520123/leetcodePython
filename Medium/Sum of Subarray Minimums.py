# Sum of Subarray Minimums
# O(n), O(n)
def sumSubarrayMins(self, arr: List[int]) -> int:
    res = 0
    arr = [-math.inf] + arr + [-math.inf]
    stack = []
    n = len(arr)
    for i in range(n):
        curr = arr[i]
        while stack and arr[stack[-1]] > curr:
            last = stack.pop(-1)
            res += (i-last) * (last-stack[-1]) * arr[last]
        stack.append(i)
    return res % (10 ** 9 + 7)