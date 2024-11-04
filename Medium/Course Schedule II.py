# Course Schedule II
# O(n), O(n)
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    course_to_prerequisites = defaultdict(int)
    prerequisites_to_course = defaultdict(list)
    for course, pre in prerequisites:
        prerequisites_to_course[pre].append(course)
        course_to_prerequisites[course] += 1
    
    
    queue = []
    for c in range(numCourses):
        if course_to_prerequisites[c] == 0:
            queue.append(c)
    
    res = []

    while queue:
        temp = queue
        queue = []
        for course in temp:
            res.append(course)
            for next_course in prerequisites_to_course[course]:
                course_to_prerequisites[next_course] -= 1
                if course_to_prerequisites[next_course] == 0:
                    queue.append(next_course)
    
    for c in range(numCourses):
        if course_to_prerequisites[c] != 0:
            return []
    
    return res