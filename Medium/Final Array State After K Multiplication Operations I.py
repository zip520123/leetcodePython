# Final Array State After K Multiplication Operations I
# O(n), O(1)
def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
    for _ in range(k):
        min_i = 0
        min_n = math.inf
        for i in range(len(nums)):
            if nums[i] < min_n:
                min_n = nums[i]
                min_i = i
        nums[min_i] *= multiplier
    return nums