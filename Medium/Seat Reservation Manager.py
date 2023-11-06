# Seat Reservation Manager

class SeatManager:

    def __init__(self, n: int):
        self.heap = [i for i in range(1,n+1)] #O(n)
        # heapq.heapify(self.heap)

    def reserve(self) -> int:
        return heapq.heappop(self.heap) #O(log n)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber) #O(log n)