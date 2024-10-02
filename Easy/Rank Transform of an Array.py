# Rank Transform of an Array
# O(n log n), O(n)
def arrayRankTransform(self, arr: List[int]) -> List[int]:
    memo = {}
    rank = 1
    sortedArr = sorted(arr)
    for i in range(len(sortedArr)):
        n = sortedArr[i]
        if i > 0 and n > sortedArr[i-1]:
            rank += 1
        memo[n] = rank
    res = []
    for n in arr:
        res.append(memo[n])
    
    return res
