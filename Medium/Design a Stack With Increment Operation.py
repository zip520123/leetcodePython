# Design a Stack With Increment Operation
# O(n), O(n)
class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.arr = []

    def push(self, x: int) -> None:
        if len(self.arr) < self.size:
            self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) == 0:
            return -1
        return self.arr.pop(-1)

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.arr))):
            self.arr[i] += val