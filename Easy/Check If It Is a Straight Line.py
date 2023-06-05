# Check If It Is a Straight Line
# O(n), O(1)
def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    n = len(coordinates)
    x1,y1 = coordinates[0]
    x2,y2 = coordinates[1]
    dx1 = x1-x2
    dy1 = y1-y2
    for i in range(n-1):
        x1,y1 = coordinates[i]
        x2,y2 = coordinates[i+1]
        dx2 = x1-x2
        dy2 = y1-y2
        if dx1*dy2 != dx2*dy1: return False
    return True
