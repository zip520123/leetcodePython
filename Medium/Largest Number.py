# Largest Number
# O(n log n), O(n)
class LargerNum(str):
    def __lt__(x,y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(num) for num in nums]
        arr.sort(key=LargerNum)
        return "0" if arr[0] == "0" else "".join(arr)