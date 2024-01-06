# Maximum Profit in Job Scheduling
# O(n log n), O(n)
def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    n = len(startTime)
    jobs = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
    jobs.sort()
    arr = []
    for i in range(n):
        l, r = i+1, n
        (start, end, p) = jobs[i]
        while l<r:
            mid = l+((r-l)>>1)
            if jobs[mid][0] < end:
                l = mid+1
            else:
                r = mid
        arr.append(l)
    dp = [0 for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        (_, _, p) = jobs[i]
        dp[i] = max(p + dp[arr[i]], dp[i+1])
    return dp[0]

# O(n log n), O(n)
def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    n = len(startTime)
    jobs = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
    jobs.sort()
    arr = []
    for i in range(n):
        l, r = i+1, n
        (start, end, p) = jobs[i]
        while l<r:
            mid = l+((r-l)>>1)
            if jobs[mid][0] < end:
                l = mid+1
            else:
                r = mid
        arr.append(l)
    
    @cache
    def dfs(i: int)-> int:
        if i == n: return 0
        return max(jobs[i][2]+dfs(arr[i]), dfs(i+1))
    return dfs(0)

# O(n log n), O(n)
def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    n = len(startTime)
    jobs = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
    jobs.sort()
    arr = []
    for i in range(n):
        l, r = i+1, n
        (start, end, p) = jobs[i]
        while l<r:
            mid = l+((r-l)>>1)
            if jobs[mid][0] < end:
                l = mid+1
            else:
                r = mid
        arr.append(l)
    
    memo = {}
    def dfs(i: int)-> int:
        if i == n: return 0
        if i in memo: return memo[i]
        memo[i] = max(jobs[i][2]+dfs(arr[i]), dfs(i+1))
        return memo[i]
    return dfs(0)