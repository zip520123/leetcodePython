# Moving Average from Data Stream
# O(1), O(n)
class MovingAverage:

    def __init__(self, size: int):
        self.arr = []
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        self.arr.append(val)
        self.sum += val
        if len(self.arr) > self.size:
            self.sum -= self.arr[0]
            self.arr.pop(0)
        return self.sum / len(self.arr)