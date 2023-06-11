# Snapshot Array
# O(len * snaps), O(len * snaps) MLE
class SnapshotArray:

    def __init__(self, length: int):
        self.dictArr = {}
        self.snaps = {}
        self.id = 0

    def set(self, index: int, val: int) -> None:
        self.dictArr[index] = val

    def snap(self) -> int:
        self.snaps[self.id] = dict(self.dictArr)
        self.id += 1
        return self.id-1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id not in self.snaps or index not in self.snaps[snap_id]:
            return 0
        return self.snaps[snap_id][index]
        
# O(len * log snaps), O(len + snaps), ChatGPT
class SnapshotArray:
    def __init__(self, length: int):
        self.records = []
        for _ in range(length):
            self.records.append([[0, 0]])
        self.id = 0

    def set(self, index: int, val: int) -> None:
        self.records[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snaps = self.records[index]
        left, right = 0, len(snaps) - 1

        while left < right:
            mid = (left + right + 1) // 2 #left + (right-left+1) // 2
            if snaps[mid][0] <= snap_id:
                left = mid
            else:
                right = mid - 1

        return snaps[left][1]
