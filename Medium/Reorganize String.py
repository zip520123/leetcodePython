# Reorganize String
# O(n log n), O(n)
def reorganizeString(self, s: str) -> str:
    res = ""
    pq = [(-count, char) for char, count in Counter(s).items()]
    heapify(pq)
    while pq:
        firstCount, firstChar = heappop(pq)
        if res == "" or res[-1] != firstChar:
            res += firstChar
            if firstCount + 1 < 0:
                heappush(pq, (firstCount + 1, firstChar))
        else:
            if len(pq) == 0: return ""
            secondCount, secondChar = heappop(pq)
            res += secondChar
            if secondCount + 1 < 0:
                heappush(pq,(secondCount+1, secondChar))
            heappush(pq, (firstCount, firstChar))
    return res