# Detonate the Maximum Bombs
# O(n^2), O(n^2)
def maximumDetonation(self, bombs: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    n = len(bombs)
    for i in range(0,n-1):
        for j in range(i+1,n):
            x1,y1,r1 = bombs[i]
            x2,y2,r2 = bombs[j]
            d = sqrt((x1-x2)**2 + (y1-y2)**2)
            if d <= r1:
                graph[i].append(j)
            if d <= r2:
                graph[j].append(i)
    res = 0
    for i in range(n):
        curr = 0
        queue = [i]
        seen = set()
        seen.add(i)
        while queue:
            temp = queue
            queue = []
            for node in temp:
                curr += 1
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
        res = max(res, curr)
    return res