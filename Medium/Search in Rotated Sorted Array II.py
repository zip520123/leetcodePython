# Search in Rotated Sorted Array II
# O(n)~Θ(log n)~Ω(1), O(1)
def search(self, nums: List[int], target: int) -> bool:
    l,r = 0, len(nums)-1
    while l<=r:
        while l<r and nums[l] == nums[l+1]: l+=1
        while l<r and nums[r] == nums[r-1]: r-=1
        
        mid = l+((r-l)>>1)
        if nums[mid] == target: return True

        if nums[mid] >= nums[l]:
            if target < nums[l] or target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        else:
            if target > nums[r] or target < nums[mid]:
                r = mid-1
            else:
                l = mid+1
    
    return False
        