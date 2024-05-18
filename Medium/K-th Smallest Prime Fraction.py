# K-th Smallest Prime Fraction
# O(n^2), O(n)
def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
    res = []
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            res.append((arr[i]/arr[j], [arr[i], arr[j]]))
    res.sort()
    return res[k-1][1]