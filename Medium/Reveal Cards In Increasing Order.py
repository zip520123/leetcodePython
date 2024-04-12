# Reveal Cards In Increasing Order
# O(n log n), O(n)
def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    n = len(deck)
    deck.sort()
    res = [0 for _ in range(n)]
    queue = [i for i in range(n)]

    for num in deck:
        curr_index = queue.pop(0)
        res[curr_index] = num
        if queue:
            next_index = queue.pop(0)
            queue.append(next_index)
    return res