# Path Crossing
# O(n), O(n)
def isPathCrossing(self, path: str) -> bool:
    pointsSet = set()
    pointsSet.add((0,0))
    curr = (0,0)
    for char in path:
        if char == "N":
            curr = (curr[0], curr[1]+1)
        if char == "S":
            curr = (curr[0], curr[1]-1)
        if char == "E":
            curr = (curr[0]+1, curr[1])
        if char == "W":
            curr = (curr[0]-1, curr[1])
        if curr in pointsSet: return True
        pointsSet.add(curr)

    return False