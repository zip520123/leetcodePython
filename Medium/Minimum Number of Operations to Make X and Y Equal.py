# Minimum Number of Operations to Make X and Y Equal
# O((y-x)^4), O((y-x)^4) MLE
def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
    if y >= x: return y-x
    dp = {y:0}
    heap = [(0,y)]
    heapq.heapify(heap)
    while heap:
        currStep, currNum = heapq.heappop(heap)
        if currNum == x: return currStep
        for nextN in [currNum + 1, currNum - 1, currNum * 5, currNum * 11]:
            if (nextN in dp and dp[nextN] > currStep+1) or (nextN not in dp):
                dp[nextN] = currStep+1
                heapq.heappush(heap, (currStep+1, nextN))
    return 0

# O(n), O(n) 
def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
    seen = set()
    queue = [x]
    count = 0
    while queue:
        temp = queue
        queue = []
        for node in temp:
            if node == y: return count
            if node in seen: continue
            seen.add(node)
            queue.append(node+1)
            if node-1 >= 1:
                queue.append(node-1)
            if node%5 == 0:
                queue.append(node//5)
            if node%11 == 0:
                queue.append(node//11)
        count += 1
    return -1