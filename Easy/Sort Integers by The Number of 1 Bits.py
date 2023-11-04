# Sort Integers by The Number of 1 Bits
# O(n log n), O(1)
def sortByBits(self, arr: List[int]) -> List[int]:
    def count1(n: int) -> int:
        res = 0
        while n > 0:
            res += n & 1
            n >>= 1
        return res

    sortedArr = sorted(arr, key = lambda x: (count1(x), x))
    return sortedArr