# Height Checker
# O(n log n), O(n)
def heightChecker(self, heights: List[int]) -> int:
    arr = sorted(heights)
    res = 0
    for i in range(len(arr)):
        if arr[i] != heights[i]:
            res += 1

    return res

# O(n), O(n)
def heightChecker(self, heights: List[int]) -> int:
    memo = defaultdict(int)
    minN, maxN = math.inf, -math.inf
    for n in heights:
        memo[n] += 1
        minN = min(minN, n)
        maxN = max(maxN, n)
    arr = []
    for n in range(minN, maxN+1):
        for _ in range(memo[n]):
            arr.append(n)
    res = 0
    for i in range(len(arr)):
        if heights[i] != arr[i]:
            res += 1
    return res