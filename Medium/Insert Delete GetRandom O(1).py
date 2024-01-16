# Insert Delete GetRandom O(1)

class RandomizedSet:

    def __init__(self):
        self.memo = set()

    def insert(self, val: int) -> bool: #O(1)
        if val in self.memo:
            return False
        self.memo.add(val)
        return True

    def remove(self, val: int) -> bool: #O(1)
        if val in self.memo: 
            self.memo.remove(val)
            return True
        return False

    def getRandom(self) -> int: #O(n)
        arr = list(self.memo)

        return arr[random.randrange(0, len(arr))]

# Insert Delete GetRandom O(1)
class RandomizedSet:
    def __init__(self):
        self.index_map = {}
        self.arr = []

    def insert(self, val: int) -> bool: #O(1)
        if val in self.index_map:
            return False
        index = len(self.arr)
        self.arr.append(val)
        self.index_map[val] = index
        return True

    def remove(self, val: int) -> bool: #O(1)
        if val not in self.index_map:
            return False
        lastIndex = len(self.arr)-1
        lastVal = self.arr[lastIndex]
        valIndex = self.index_map[val]
        self.arr[valIndex] = lastVal
        self.arr.pop(-1)
        self.index_map[lastVal] = valIndex
        del self.index_map[val]
        return True

    def getRandom(self) -> int: #O(1)
        return random.choice(self.arr)