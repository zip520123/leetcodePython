# Image Smoother
# O(n), O(1)
def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
    rows, cols = len(img), len(img[0])
    res = [[0]*cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            curr = 0
            count = 0
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if 0 <= row+y < rows and 0 <= col+x < cols:
                        count += 1
                        curr += img[row+y][col+x]
            res[row][col] = curr // count
    return res 