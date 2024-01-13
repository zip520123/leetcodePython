# Minimum Moves to Capture The Queen
# O(1), O(1)
def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
    
    if a == e: # rock on same row
        if c == a and (d - b) * (d - f) < 0: # check bishop between them
            return 2
        return 1
    if b == f: # rock on same col
        if b == d and (c - a) * (c - e) < 0:
            return 2
        return 1
    if c - e == d - f: # bishop on the same \ diagonal
        if a - e == b - f and (a - c) * (a - e) < 0: # if rock between them
            return 2
        return 1
    if c - e == f - d:
        if a - e == f - b and (a - c) * (a - e) < 0:
            return 2
        return 1
    return 2