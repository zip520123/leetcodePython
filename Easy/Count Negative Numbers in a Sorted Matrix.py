# Count Negative Numbers in a Sorted Matrix
# O(rows*cols), O(1)
def countNegatives(self, grid: List[List[int]]) -> int:
    res = 0
    for row in grid:
        for col in row:
            if col < 0:
                res += 1 
    return res

# O(rows* log cols), O(1)
def countNegatives(self, grid: List[List[int]]) -> int:
    res = 0
    for row in grid:
        l=0;r=len(row)
        while l<r:
            mid = l+((r-l)>>1)
            if row[mid] >= 0:
                l = mid+1
            else:
                r = mid
        res += len(row)-l
    return res