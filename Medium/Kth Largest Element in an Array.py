# Kth Largest Element in an Array
# O(n), O(1)
def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        t = n-k
        left, right = 0, n-1
        while True:
            i, l, r = left, left, right
            p = nums[randint(l,r)]
            while i<=r:
                if nums[i] < p:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
                    i += 1
                elif nums[i] > p:
                    nums[r], nums[i] = nums[i], nums[r]
                    r -= 1
                else:
                    i += 1
            if t < l:
                right = l - 1
            elif t > r:
                left = r + 1
            else:
                return p