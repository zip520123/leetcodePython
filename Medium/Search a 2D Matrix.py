# Search a 2D Matrix
# O(log(rows*cols)), O(1)
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix); cols = len(matrix[0])
    l, r = 0, rows*cols-1
    while l<r:
        mid = l+((r-l)>>1)
        row = mid // cols
        col = mid % cols
        if matrix[row][col] < target:
            l = mid+1
        else :
            r = mid
    row = l // cols
    col = l % cols
    return matrix[row][col] == target