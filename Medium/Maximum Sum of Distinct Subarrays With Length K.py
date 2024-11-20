# Maximum Sum of Distinct Subarrays With Length K
# O(n), O(n)
def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    curr_num_set = set()
    num_count = defaultdict(int)
    res = 0
    curr = 0
    l, r = 0,0
    while r < len(nums):
        curr += nums[r]
        num_count[nums[r]] += 1
        if num_count[nums[r]] == 1:
            curr_num_set.add(nums[r])
        elif num_count[nums[r]] == 2:
            curr_num_set.remove(nums[r])
            
        if r >= k-1:
            if len(curr_num_set) == k:
                res = max(res, curr)
            curr -= nums[l]
            num_count[nums[l]] -= 1
            if num_count[nums[l]] == 1:
                curr_num_set.add(nums[l])
            elif num_count[nums[l]] == 0:
                curr_num_set.remove(nums[l])
                
            l += 1
        r += 1
    return res