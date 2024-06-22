# Count Number of Nice Subarrays
# O(n), O(n)
def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    curr_sum = 0
    subarrays = 0
    prefix_sum = {0: 1}

    for i in range(len(nums)):
        curr_sum += nums[i] % 2
        if curr_sum - k in prefix_sum:
            subarrays = subarrays + prefix_sum[curr_sum - k]

        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
    return subarrays

def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    curr_sum = 0
    subarrays = 0
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    for i in range(len(nums)):
        curr_sum += nums[i] % 2
        subarrays += prefix_sum[curr_sum-k]
        prefix_sum[curr_sum] += 1
    return subarrays