# Design Circular Deque
# O(n), O(n)
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.arr = []

    def insertFront(self, value: int) -> bool:
        if len(self.arr) == self.k:
            return False
        self.arr.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.arr) == self.k:
            return False
        self.arr.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.arr) == 0:
            return False
        self.arr.pop(0)
        return True

    def deleteLast(self) -> bool:
        if len(self.arr) == 0:
            return False
        self.arr.pop(-1)
        return True

    def getFront(self) -> int:
        if self.arr:
            return self.arr[0]
        return -1

    def getRear(self) -> int:
        if self.arr:
            return self.arr[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.arr) == 0

    def isFull(self) -> bool:
        return len(self.arr) == self.k