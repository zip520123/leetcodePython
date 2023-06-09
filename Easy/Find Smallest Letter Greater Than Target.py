# Find Smallest Letter Greater Than Target
# O(n), O(1)
def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    res = None
    for char in letters:
        if char > target:
            if res == None:
                res = char
            else:
                if res > char:
                    res = char

    if res == None:
        return letters[0]
    return res 