# Number of Lines To Write String
# O(n), O(1)
def numberOfLines(self, widths: List[int], s: str) -> List[int]:
    currWidths = 0
    currCount = 0
    lines = 1
    for char in s:
        width = widths[ord(char) - ord("a")]
        if currWidths + width > 100:
            currWidths = 0
            currCount = 0
            lines += 1
        currWidths += width
        currCount += 1
    return [lines, currWidths]