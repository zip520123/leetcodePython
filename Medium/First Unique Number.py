# First Unique Number
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.memo = defaultdict(int)
        self.arr = []
        for n in nums:
            self.arr.append(n)
            self.memo[n] += 1

    def showFirstUnique(self) -> int: # O(n)
        while self.arr and self.memo[self.arr[0]] > 1:
            self.arr.pop(0)
        if self.arr:
            return self.arr[0]
        return -1

    def add(self, value: int) -> None: #O(1)
        self.memo[value] += 1
        self.arr.append(value)

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.memo = defaultdict(int)
        self.arr = []
        self.i = 0
        for n in nums:
            self.arr.append(n)
            self.memo[n] += 1
        

    def showFirstUnique(self) -> int:
        while self.i < len(self.arr) and self.memo[self.arr[self.i]] > 1:
            self.i += 1
        if self.i < len(self.arr):
            return self.arr[self.i]
        return -1

    def add(self, value: int) -> None:
        self.memo[value] += 1
        self.arr.append(value)