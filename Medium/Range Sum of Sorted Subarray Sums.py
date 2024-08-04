# Range Sum of Sorted Subarray Sums
# O(n^2), O(n)
def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    arr = []
    
    for i in range(n):
        curr = 0
        for j in range(i,n):
            curr += nums[j]
            arr.append(curr)
        
    arr.sort()

    res = 0
    for i in range(left-1, right):
        res += arr[i]
    return res % (10 ** 9 + 7)