# Design Hit Counter
class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None: #O(1)
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int: #O(n)
        while self.hits and self.hits[0] <= timestamp-300:
            self.hits.pop(0)
        return len(self.hits)
    
# follow up
class HitCounter:
    def __init__(self):
        self.hits = []
        self.total = 0

    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][1] == timestamp:
            count, _ = self.hits.pop(-1)
            self.hits.append((count + 1, timestamp))
        else:
            self.hits.append((1, timestamp))
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0][-1] <= timestamp-300:
            count, t = self.hits.pop(0)
            self.total -= count
 
        return self.total