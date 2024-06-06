# Hand of Straights
# O(n log n), O(n)
def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    heap = []
    memo = defaultdict(int)
    for card in hand:
        memo[card] += 1
        heapq.heappush(heap, card)

    while heap:
        curr = heapq.heappop(heap)
        if memo[curr] > 0:
            memo[curr] -= 1
            for i in range(1, groupSize):
                next = curr+i
                if memo[next] == 0:
                    return False
                memo[next] -= 1
    return True