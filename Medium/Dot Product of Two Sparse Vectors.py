# Dot Product of Two Sparse Vectors
# O(n), O(n)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.memo = defaultdict(int)
        for i in range(len(nums)):
            self.memo[i] = nums[i]

    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for key,val in vec.memo.items():
            res += self.memo[key] * val
        return res