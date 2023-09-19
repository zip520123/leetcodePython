# Find the Duplicate Number
# O(n), O(n)
def findDuplicate(self, nums: List[int]) -> int:
    memo = set()
    for n in nums:
        if n in memo: return n
        memo.add(n)
    return 0

# O(n), O(1)
def findDuplicate(self, nums: List[int]) -> int:
    slow, fast = nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow