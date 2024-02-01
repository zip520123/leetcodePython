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

# O(n), O(n)
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    prere = defaultdict(int)
    coursesLink = defaultdict(list)
    for course, prereque in prerequisites:
        prere[course] += 1
        coursesLink[prereque].append(course)
    queue = []
    for i in range(numCourses):
        if prere[i] == 0:
            queue.append(i)
    while queue:
        course = queue.pop()
        for nextCourse in coursesLink[course]:
            prere[nextCourse] -= 1
            if prere[nextCourse] == 0:
                queue.append(nextCourse)
    for i in range(numCourses):
        if prere[i] > 0: return False
    return True