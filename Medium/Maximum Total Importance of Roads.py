# Maximum Total Importance of Roads
# O(n log n), O(n)
def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
    memo = defaultdict(int)
    for node1, node2 in roads:
        memo[node1] += 1
        memo[node2] += 1
    
    arr = sorted(memo.values(), reverse = True)
    res = 0
    curr = 0
    for importance in range(n, -1, -1):
        if curr < len(arr):
            res += arr[curr] * importance
        curr += 1
    return res