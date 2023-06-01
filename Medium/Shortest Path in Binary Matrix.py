# Shortest Path in Binary Matrix
# O(n), O(n)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid); cols = len(grid[0])
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        seen = set()
        queue = [(0,0)]
        step = 1
        while len(queue) > 0:
            temp = queue
            queue = []
            for x,y in temp:
                if x==rows-1 and y==cols-1:
                    return step
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        nextX = x+dx; nextY = y+dy
                        if nextX >= 0 and nextY >= 0 and nextX < rows and nextY < cols and grid[nextX][nextY] == 0 and (nextX,nextY) not in seen:
                            seen.add((nextX,nextY))
                            queue.append((nextX,nextY))
            step += 1
        return -1