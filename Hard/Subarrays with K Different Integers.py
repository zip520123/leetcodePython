# Subarrays with K Different Integers
# O(n), O(n)
def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    def subarrayWithK(nums: List[int], k: int)-> int:
        memo = defaultdict(int)
        num_set = set()
        res = 0
        l, r = 0, 0
        n = len(nums)
        while r<n:
            memo[nums[r]] += 1
            num_set.add(nums[r])
            while len(num_set) > k:
                memo[nums[l]] -= 1
                if memo[nums[l]] == 0:
                    num_set.remove(nums[l])
                l += 1
            
            res += r-l+1
            r += 1
        return res
    return subarrayWithK(nums, k) - subarrayWithK(nums,k-1)