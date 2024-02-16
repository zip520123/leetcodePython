# Least Number of Unique Integers after K Removals
# O(n log n), O(n)
def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    memo = defaultdict(int)
    for n in arr:
        memo[n] += 1
    arr = []
    for key, val in memo.items():
        arr.append((val, key))
    arr.sort()
    i = 0
    while i < len(arr) and arr[i][0] <= k:
        k -= arr[i][0]
        i += 1
    return len(arr)-i