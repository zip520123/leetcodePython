# Count the Number of Good Subarrays
# O(n), O(n)
def countGood(self, nums: List[int], k: int) -> int:
    l, r = 0, 0
    pair_count = 0
    memo = defaultdict(int)
    n = len(nums)
    res = 0
    while r < n:
        curr = nums[r]
        
        exiting_pairs = (memo[curr] * (memo[curr] - 1)) // 2           
        pair_count -= exiting_pairs
        memo[curr] += 1
        new_pairs = (memo[curr] * (memo[curr] - 1)) // 2  
        pair_count += new_pairs

        while pair_count >= k:
            res += n-r
            left_num = nums[l]
            left_exiting_pairs = (memo[left_num] * (memo[left_num] - 1)) // 2
            pair_count -= left_exiting_pairs
            memo[left_num] -= 1
            left_new_pairs = (memo[left_num] * (memo[left_num] - 1)) // 2
            pair_count += left_new_pairs
            l += 1
        r += 1
    return res