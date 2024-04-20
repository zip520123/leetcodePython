# Find All Groups of Farmland
# O(n), O(n)
def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
    rows, cols = len(land), len(land[0])
    res = []
    def dfs(row,col) -> List[int]:
        nonlocal land
        land[row][col] = 0
        end_x = row
        end_y = col
        for dx, dy in [(0,1), (1,0)]:
            if 0 <= row+dx < rows and 0 <= col+dy < cols and land[row+dx][col+dy] == 1:
                next = dfs(row+dx, col+dy)
                end_x, end_y = max(end_x, next[0]), max(end_y, next[1])
                    
        return [end_x, end_y]
            
    for row in range(rows):
        for col in range(cols):
            if land[row][col] == 1:
                start = [row, col]
                end = dfs(row, col)
                res.append(start+end)
    return res