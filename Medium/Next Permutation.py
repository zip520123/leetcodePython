# Next Permutation
'''
    1. find i < i+1
    2. find j > i from right 
    3. swap i,j
    4. reverse i+1...n
'''
# O(n), O(1)
def nextPermutation(self, nums: List[int]) -> None:
    p = -1
    n = len(nums)
    for i in range(n-1):
        if nums[i] < nums[i+1]:
            p = i
    if p == -1:
        l, r = 0, n - 1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return
    next_p = p
    for i in range(n-1, p, -1):
        if nums[i] > nums[p]:
            next_p = i
            break
    nums[p], nums[next_p] = nums[next_p], nums[p]
    
    l, r = p + 1, n - 1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1