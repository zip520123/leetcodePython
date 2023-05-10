# Spiral Matrix II
# O(n) time, O(1) space
from enum import Enum
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        left=0; right=n-1; top=0; bottom=n-1
        d = Direction.right
        curr = 1
        while left<=right and top<=bottom:
            if d == Direction.right:
                for i in range(left,right+1):
                    res[top][i] = curr
                    curr += 1
                top += 1
                d = Direction.down
            elif d == Direction.down:
                for i in range(top,bottom+1):
                    res[i][right] = curr
                    curr += 1
                right -= 1
                d = Direction.left
            elif d == Direction.left:
                for i in range(right,left-1,-1):
                    res[bottom][i] = curr
                    curr += 1
                bottom -= 1
                d = Direction.up
            elif d == Direction.up:
                for i in range(bottom, top-1,-1):
                    res[i][left] = curr
                    curr += 1
                left += 1
                d = Direction.right
        return res

Direction = Enum('Direction', ['left','right','up','down'])
