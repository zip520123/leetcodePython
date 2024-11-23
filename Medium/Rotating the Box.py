# Rotating the Box
# O(n), O(1)
def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
    rows, cols = len(box), len(box[0])
    for row in range(rows):
        last_obstacle_index = -1
        for col in range(cols):
            
            if box[row][col] == "*":
                l = last_obstacle_index + 1
                r = col-1
                last_obstacle_index = col
                while r > l and box[row][r] != ".":
                    r -= 1
                while l<r:
                    if box[row][l] == "#":
                        box[row][r], box[row][l] = box[row][l], box[row][r]
                        while r > l and box[row][r] != ".":
                            r -= 1
                    l += 1

        l = last_obstacle_index + 1
        r = cols-1
        while r > l and box[row][r] != ".":
            r -= 1
        while l<r:
            if box[row][l] == "#":
                box[row][r], box[row][l] = box[row][l], box[row][r]
                while r > l and box[row][r] != ".":
                    r -= 1
            l += 1

    res = [ [""] * rows for _ in range(cols) ]
    for row in range(rows):
        for col in range(cols):
            res[col][rows-row-1] = box[row][col]
    return res