# Product of the Last K Numbers
# TLE
class ProductOfNumbers:

    def __init__(self):
        self.arr = []

    def add(self, num: int) -> None:
        self.arr.append(num)

    def getProduct(self, k: int) -> int: # O(k)
        curr = 1
        for n in self.arr[-k:]:
            curr *= n
        return curr