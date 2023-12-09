# Arithmetic Subarrays
# O(n log n * len(l)), O(n)
def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    
    def isArithmetic(arr: List[int]) -> bool:
        arr.sort()
        d = arr[0]-arr[1]
        n = len(arr)
        
        for i in range(1,n):
            if arr[i-1]-arr[i] != d: return False
        return True
    
    q = len(l)
    res = []
    for i in range(q):
        arr = nums[l[i]:r[i]+1]
        res.append(isArithmetic(arr))
    return res