# Count Complete Subarrays in an Array
# O(n), O(n)
def countCompleteSubarrays(self, nums: List[int]) -> int:
    
    elements = 0
    memo = defaultdict(int)
    n = len(nums)
    res = 0
    l, r = 0, 0
    distinct_set = set()
    for num in nums:
        distinct_set.add(num)
    distinct = len(distinct_set)

    while r < n:
        num = nums[r]
        memo[num] += 1
        if memo[num] == 1:
            elements += 1
            while elements == distinct:
                res += n-r
                left_num = nums[l]
                memo[left_num] -= 1
                if memo[left_num] == 0:
                    elements -= 1
                l += 1
        r += 1
    return res