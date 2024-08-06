# Kth Distinct String in an Array
# O(n), O(n)
def kthDistinct(self, arr: List[str], k: int) -> str:
    memo = defaultdict(int)
    for n in arr:
        memo[n] += 1
    d = 0
    for n in arr:
        if memo[n] == 1:
            d += 1
            if d == k:
                return n
    return ""