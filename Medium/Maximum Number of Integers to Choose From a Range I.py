# Maximum Number of Integers to Choose From a Range I
# O(n), O(n)
def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
    banned_set = set(banned)
    curr = 0
    res = 0
    
    for i in range(1, n+1):
        if curr + i > maxSum:
            break
        if i not in banned_set:
            curr += i
            res += 1
    return res