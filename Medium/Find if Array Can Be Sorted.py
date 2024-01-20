# Find if Array Can Be Sorted
# O(n log n), O(n)
def canSortArray(self, nums: List[int]) -> bool:
    curr = -1
    groups = []
    for n in nums:
        bits = 0
        currN = n
        while currN:
            bits += currN & 1
            currN >>= 1
        if curr != bits:
            curr = bits
            groups.append([])
        groups[-1].append(n)
    sortArr = []
    for arr in groups:
        sortArr += sorted(arr)
    
    return sortArr == sorted(nums)