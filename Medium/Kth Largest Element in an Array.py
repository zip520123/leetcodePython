# Kth Largest Element in an Array
# O(n^2)~O(n), O(n)
def findKthLargest(self, nums: List[int], k: int) -> int:
    n = len(nums)
    def dfs(left: int, right: int) -> int:
        l, r, p = left, left, right
        while r<p:
            if nums[r] >= nums[p]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        nums[l], nums[p] = nums[p], nums[l]
        if l == k-1:
            return nums[l]
        elif l > k-1:
            return dfs(0,l-1)
        else :
            return dfs(l+1, r)
    
    return dfs(0,n-1)