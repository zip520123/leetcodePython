# Smallest Rectangle Enclosing Black Pixels
# O(mn), O(1)
def minArea(self, image: List[List[str]], x: int, y: int) -> int:
    top, bottom = x, x
    left, right = y, y
    rows, cols = len(image), len(image[0])
    for row in range(rows):
        for col in range(cols):
            if image[row][col] == "1":
                top = min(top, row)
                bottom = max(bottom, row)
                left = min(left, col)
                right = max(right, col)
    return (right - left + 1) * (bottom - top + 1)