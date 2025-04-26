# Random Pick with Weight

class Solution:
    def __init__(self, w: List[int]): #O(n)
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total = prefix_sum

    def pickIndex(self) -> int: #O(logn)
        target = random.randrange(self.total)
        
        for i in range(len(self.prefix_sums)):
            if target < self.prefix_sums[i]:
                return i



class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total = prefix_sum

    def pickIndex(self) -> int:
        # target = random.randrange(self.total) Wrong answer
        target = self.total * random.random()
        l, r = 0, len(self.prefix_sums)
        while l<r:
            mid = l+((r-l)>>1)
            if self.prefix_sums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l