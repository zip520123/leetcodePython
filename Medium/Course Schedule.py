# Course Schedule
# O(n), O(n)
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(int)
    preCourses = defaultdict(list)
    for a,b in prerequisites:
        graph[b] += 1
        preCourses[a].append(b)
    queue = []
    for i in range(numCourses):
        if graph[i] == 0:
            queue.append(i)
    while queue:
        node = queue.pop()
        for preCourse in preCourses[node]:
            graph[preCourse] -= 1
            if graph[preCourse] == 0:
                queue.append(preCourse)
    for i in range(numCourses):
        if graph[i] > 0: return False

    return True