# Find Missing and Repeated Values
# O(n), O(n)
def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    n_set = set()
    n = len(grid[0]) ** 2
    res = []
    for row in range(len(grid)):
        for num in grid[row]:
            if num in n_set:
                res.append(num)
            n_set.add(num)
    for i in range(1, n+1):
        if i not in n_set:
            res.append(i)
    
    return res