# Maximum Subarray With Equal Products
# O(n^2), O(1)
def maxLength(self, nums: List[int]) -> int:
    res = 0
    for i in range(len(nums)-1):
        prod = nums[i]
        gcd_n = nums[i]
        lcm_n = nums[i]
        for j in range(i+1, len(nums)):
            prod *= nums[j]
            gcd_n = gcd(gcd_n, nums[j])
            lcm_n = lcm(lcm_n, nums[j])
            if prod == gcd_n * lcm_n:
                res = max(res, j-i+1)
    return res