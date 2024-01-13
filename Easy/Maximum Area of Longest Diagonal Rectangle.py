# Maximum Area of Longest Diagonal Rectangle
# O(n), O(n)
def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
    maxS = 0
    max_area = 0
    n = len(dimensions)
    for i in range(n):
        curr = sqrt(dimensions[i][0] * dimensions[i][0] + dimensions[i][1] * dimensions[i][1])
        curr_area = dimensions[i][0] * dimensions[i][1]
        
        if curr > maxS:
            maxS = curr
            max_area = curr_area
            
        if curr == maxS and curr_area > max_area:
            max_area = curr_area
    return max_area