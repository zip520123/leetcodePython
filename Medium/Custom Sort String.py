# Custom Sort String
# O(n log n), O(n)
def customSortString(self, order: str, s: str) -> str:
    memo = defaultdict(lambda: 27)
    for i in range(len(order)):
        char = order[i]
        memo[char] = i
    heap = []
    for char in s:
        heapq.heappush(heap, (memo[char], char))
    res = ""
    while heap:
        val, char = heapq.heappop(heap)
        res += char
    return res

# O(n), O(n)
def customSortString(self, order: str, s: str) -> str:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1
    res = ""
    for char in order:
        for _ in range(memo[char]):
            res += char
            memo[char] = 0
    for char, val in memo.items():
        for _ in range(val):
            res += char
    return res