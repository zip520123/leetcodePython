# Shortest Subarray With OR at Least K II
# O(n), O(1)
def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
    bits = [0] * 32        
    l, r = 0, 0
    res = math.inf
    while r<len(nums):
        curr = nums[r]
        mask = 0
        while curr:
            bits[mask] += curr & 1
            curr >>= 1
            mask += 1
        
        total = 0
        for i in range(32):
            if bits[i] > 0:
                total += (2 ** i)
        
        while total >= k and l <= r:
            res = min(res, r-l+1)
            left = nums[l]
            mask = 0
            while left:
                bits[mask] -= left & 1
                left >>= 1
                mask += 1
            total = 0
            for i in range(32):
                if bits[i] > 0:
                    total += 2 ** i
            
            l += 1
        r += 1
    return res if res < math.inf else -1