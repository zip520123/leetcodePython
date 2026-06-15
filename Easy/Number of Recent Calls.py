# Number of Recent Calls
# O(n) time | O(n) space
class RecentCounter:

    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        self.arr.append(t)
        while self.arr and t-3000 > self.arr[0]:
            self.arr.pop(0)
        return len(self.arr)