# Special Array With X Elements Greater Than or Equal X
# O(n^2), O(1)
def specialArray(self, nums: List[int]) -> int:
    for curr in range(len(nums)+1):
        count = 0
        for n in nums:
            if n >= curr:
                count += 1
        if count == curr:
            return curr
    return -1