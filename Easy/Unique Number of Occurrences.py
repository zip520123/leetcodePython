# Unique Number of Occurrences
# O(n), O(n)
def uniqueOccurrences(self, arr: List[int]) -> bool:
    memo = defaultdict(int)
    for n in arr:
        memo[n] += 1
    counts = set()
    for _, val in memo.items():
        if val in counts: return False
        counts.add(val)
    return True