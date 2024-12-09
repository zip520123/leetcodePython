# Special Array II
# O(n), O(n)
def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    memo = {}
    l = 0
    interval_index = 0
    for i in range(1, len(nums)):
        curr = nums[i]
        prev = nums[i-1]
        if curr % 2 != prev % 2:
            pass
        else:
            for j in range(l,i):
                memo[j] = interval_index
            interval_index += 1
            l = i
    
    for j in range(l, len(nums)):
        memo[j] = interval_index
        
    return [ memo[s] == memo[e] for s, e in queries ]