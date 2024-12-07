# Minimum Limit of Balls in a Bag
# O(n log n), O(n)
def minimumSize(self, nums: List[int], maxOperations: int) -> int:
    l, r = 1, max(nums)
    while l<r:
        mid = l+((r-l)>>1)

        curr_op = 0
        for n in nums:
            if n > mid:
                curr_op += math.ceil(n/mid) - 1
                if curr_op > maxOperations:
                    break
        if curr_op > maxOperations:
            l = mid + 1
        else:
            r = mid
    return l