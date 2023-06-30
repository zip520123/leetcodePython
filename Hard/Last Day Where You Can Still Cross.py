# Last Day Where You Can Still Cross
# O(n log n), O(n)
def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

    def canCross(day: int) -> bool:
        grid = [[0] * col for _ in range(row)]

        for r, c in cells[:day]:
            grid[r-1][c-1] = 1

        queue = [] 

        for i in range(col):
            if grid[0][i] == 0:
                queue.append((0,i))
                grid[0][i] = -1
        
        while queue:
            r,c = queue.pop(0)
            if r == row-1:
                return True
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                newRow, newCol = r+dr, c+dc
                if 0 <= newRow < row and 0 <= newCol < col and grid[newRow][newCol] == 0:
                    grid[newRow][newCol] = -1
                    queue.append((newRow, newCol))
                    
        return False
    
    l, r = 1, row*col
    while l<r:
        mid = l+((r-l)>>1)
        if canCross(mid):
            l = mid+1
        else:
            r = mid
    return l-1