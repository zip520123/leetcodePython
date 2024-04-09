# Number of Students Unable to Eat Lunch
# O(n^2), O(1)
def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    valid = True
    while valid:
        n = len(students)
        valid = False
        for _ in range(n):
            student = students.pop(0)
            if sandwiches[0] == student:
                sandwiches.pop(0)
                valid = True
                break
            else:
                students.append(student)
        
    return len(students)