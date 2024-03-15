# Product of Array Except Self
# O(n), O(n)
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    arr1, arr2 = [0]*n, [0]*n
    arr1[0] = nums[0]
    for i in range(1,n):
        arr1[i] = nums[i] * arr1[i-1]
    arr2[n-1] = nums[n-1]
    for i in range(n-2,0,-1):
        arr2[i] = nums[i] * arr2[i+1]
    res = [0]*n
    for i in range(1,n-1):
        res[i] = arr1[i-1] * arr2[i+1]
    res[0] = arr2[1]
    res[n-1] = arr1[n-2]
    return res

# O(n), O(1)
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [ nums[i] for i in range(n)]
    for i in range(1,n):
        res[i] *= res[i-1]
    d = 1
    for i in range(n-1, 0, -1):
        res[i] = d * res[i-1]
        d *= nums[i]
    res[0] = d
    return res