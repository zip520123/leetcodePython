# Type of Triangle
# O(n), O(n)
def triangleType(self, nums: List[int]) -> str:
    if nums[0] == nums[1] == nums[2]:
        return "equilateral"

    nums.sort()
    if nums[0] + nums[1] <= nums[2]:
        return "none"
    
    memo = defaultdict(int)
    for n in nums:
        memo[n] += 1
        if memo[n] == 2:
            return "isosceles"
    
    return "scalene"