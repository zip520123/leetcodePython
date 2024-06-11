# Relative Sort Array
# O(n log n), O(n)
def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    memo = {}
    for i in range(len(arr2)):
        n = arr2[i]
        memo[n] = i

    res1 = []
    res2 = []
    for n in arr1:
        if n in memo:
            res1.append(n)
        else:
            res2.append(n)
    res = sorted(res1, key = lambda x: memo[x]) + sorted(res2)

    return res