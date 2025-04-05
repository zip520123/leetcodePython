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

# O(n), O(n)
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    visit_list = [0] * numCourses
    # 0 non visited, 1 visiting, 2 visited
    graph = defaultdict(list)
    for coures, pre in prerequisites:
        graph[pre].append(coures)

    def dfs(node) -> bool:
        if visit_list[node] == 1: 
            return False
        if visit_list[node] == 2:
            return True
        visit_list[node] = 1 # visiting
        for next_coures in graph[node]:
            if dfs(next_coures) == False:
                return False
        visit_list[node] = 2 # visited
        return True
    
    for node in range(numCourses):
        if dfs(node) == False:
            return False
    return True