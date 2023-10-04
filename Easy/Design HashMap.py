# Design HashMap
# O(1), O(1)
class MyHashMap:

    def __init__(self):
        self.arr = [-1 for _ in range(int(1E6+1))]

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    def get(self, key: int) -> int:
        return self.arr[key]

    def remove(self, key: int) -> None:
        self.arr[key] = -1
