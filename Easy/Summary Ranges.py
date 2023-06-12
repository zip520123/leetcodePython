# Summary Ranges
# O(n), O(1)
def summaryRanges(self, nums: List[int]) -> List[str]:
    n = len(nums)
    if n == 0: return []
    start = nums[0]; end = nums[0]
    res = []
    for i in range(1,n):
        if nums[i] == end+1:
            end = nums[i]
        else:
            if start == end:
                res.append(str(start))
            else :
                res.append(str(start)+"->"+str(end))
            start = nums[i]
            end = nums[i]
    if start == end:
        res.append(str(start))
    else :
        res.append(str(start)+"->"+str(end))
    return res