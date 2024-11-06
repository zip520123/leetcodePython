# Find if Array Can Be Sorted
# O(n log n), O(n)
def canSortArray(self, nums: List[int]) -> bool:
    curr = -1
    groups = []
    for n in nums:
        bits = 0
        currN = n
        while currN:
            bits += currN & 1
            currN >>= 1
        if curr != bits:
            curr = bits
            groups.append([])
        groups[-1].append(n)
    sortArr = []
    for arr in groups:
        sortArr += sorted(arr)
    
    return sortArr == sorted(nums)

# O(n), O(n)
def canSortArray(self, nums: List[int]) -> bool:
    first_ones = 0
    first = nums[0]
    while first:
        first_ones += first % 2
        first >>= 1
    
    segments = [[]]

    for n in nums:
        ones = 0
        curr = n
        while curr:
            ones += curr % 2
            curr >>= 1
        if ones == first_ones:
            segments[-1].append(n)
        else:
            segments.append([n])
            first_ones = ones
    
    for i in range(1, len(segments)):
        curr_segment = segments[i]
        prev_segment = segments[i-1]
        if max(prev_segment) > min(curr_segment):
            return False
    return True