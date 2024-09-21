# Largest Number
# O(n log n), O(n)
class LargerNum(str):
    def __lt__(self,other):
        return self+other > other+self

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(num) for num in nums]
        arr.sort(key=LargerNum)
        return "0" if arr[0] == "0" else "".join(arr)

# O(n log n), O(n)
def largestNumber(self, nums: List[int]) -> str:
    arr = sorted(nums, key=lambda x: str(x) * 10, reverse=True)
    res = "".join(map(str,arr))
    return "0" if res[0] == "0" else res