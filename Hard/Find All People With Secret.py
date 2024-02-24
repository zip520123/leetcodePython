# Find All People With Secret
# O(n log n), O(n), union find
def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    sortedMeetings = sorted(meetings, key= lambda meeting: meeting[2])
    l, r = 0, 0
    arr = [False]*n
    arr[0], arr[firstPerson] = True, True
    while r < len(sortedMeetings):
        while r < len(sortedMeetings) and sortedMeetings[l][2] == sortedMeetings[r][2]:
            r += 1
        memo = {}
        def find(node: int) -> int:
            if node not in memo:
                memo[node] = node
                return memo[node]
            if memo[node] != node:
                root = find(memo[node])
                memo[node] = root
            return memo[node]

        def union(node1: int, node2: int):
            root1, root2 = find(node1), find(node2)
            if arr[root1]:
                memo[root2] = root1
            else:
                memo[root1] = root2
        
        for i in range(l,r):
            p1, p2, t = sortedMeetings[i]
            union(p1,p2)
        for node in memo.keys():
            root = find(node)
            if arr[root]:
                arr[node] = True
        l = r
    res = []
    for i in range(n):
        if arr[i]:
            res.append(i)
    return res

# O(n log n), O(n)
def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    graph = defaultdict(list)
    for p1, p2, t in meetings:
        graph[p1].append((t, p2))
        graph[p2].append((t, p1))

    visited = set()
    heap = [] 
    heapq.heappush(heap, (0, 0)) # time, person
    heapq.heappush(heap, (0, firstPerson))

    while heap:
        t, p = heapq.heappop(heap)
        if p in visited: continue
        visited.add(p)
        for nextTime, nextPerson in graph[p]:
            if nextTime >= t:
                heapq.heappush(heap, (nextTime, nextPerson))
    return visited