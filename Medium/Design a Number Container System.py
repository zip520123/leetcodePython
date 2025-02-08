# Design a Number Container System
# TLE
class NumberContainers:

    def __init__(self):
        self.index_to_number = {}
        self.number_to_indeies = defaultdict(set)

    def change(self, index: int, number: int) -> None:  # O(1)
        if index in self.index_to_number:
            prev_number = self.index_to_number[index]
            self.number_to_indeies[prev_number].remove(index)
        self.index_to_number[index] = number
        self.number_to_indeies[number].add(index)

    def find(self, number: int) -> int: # O(n)
        if self.number_to_indeies[number]:
            return min(self.number_to_indeies[number])
        return -1
    

class NumberContainers:
    def __init__(self):
        self.number_to_indices = defaultdict(list)
        self.index_to_numbers = {}

    def change(self, index: int, number: int) -> None:
        self.index_to_numbers[index] = number
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        if not self.number_to_indices[number]:
            return -1

        while self.number_to_indices[number]:
            index = self.number_to_indices[number][0]

            if self.index_to_numbers.get(index) == number:
                return index

            heapq.heappop(self.number_to_indices[number])
        return -1