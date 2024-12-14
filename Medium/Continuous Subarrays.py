# Continuous Subarrays
# O(n), O(n)
def continuousSubarrays(self, nums: List[int]) -> int:
    res = 0
    l = 0
    max_q = []
    min_q = []
    for i in range(len(nums)):
        while max_q and nums[max_q[-1]] <= nums[i]:
            max_q.pop(-1)
        max_q.append(i)
        while min_q and nums[min_q[-1]] >= nums[i]:
            min_q.pop(-1)
        min_q.append(i)

        while max_q and min_q and (abs(nums[i] - nums[max_q[0]]) > 2 or abs(nums[i] - nums[min_q[0]]) > 2):
            if max_q[0] == l:
                max_q.pop(0)
            if min_q[0] == l:
                min_q.pop(0)
            l += 1
            
        res += i-l+1
    return res