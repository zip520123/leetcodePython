# Spiral Matrix
# O(n) time, O(1) space
from enum import Enum
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows = len(matrix); cols = len(matrix[0])
        top = 0; right = cols-1; bottom = rows-1; left = 0
        d = Direction.r
        while top <= bottom and left <= right:
            if d is Direction.r:
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top += 1
                d = Direction.below
            elif d is Direction.below:
                for i in range(top,bottom+1):
                    res.append(matrix[i][right])
                right -= 1
                d = Direction.l
            elif d is Direction.l:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                d = Direction.up
            elif d is Direction.up:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left += 1
                d = Direction.r
        return res

class Direction(Enum):
    r = 1
    l = 2
    up = 3
    below = 4
