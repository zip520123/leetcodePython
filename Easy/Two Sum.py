# Two Sum
# O(n), O()
def twoSum(self, nums: List[int], target: int) -> List[int]:
    memo = {}
    for i in range(len(nums)):
        curr = nums[i]
        if target - curr in memo:
            return [memo[target-curr], i]
        memo[curr] = i
    return []
