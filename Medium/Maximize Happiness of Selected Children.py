# Maximize Happiness of Selected Children
# O(n log n), O(n)
def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
    happiness.sort(reverse=True)
    res = 0
    count = 0
    for i in range(k):
        curr = happiness[i] - count
        if curr > 0:
            res += curr
        count += 1
    return res