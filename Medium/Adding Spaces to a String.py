# Adding Spaces to a String
# O(n), O(1)
def addSpaces(self, s: str, spaces: List[int]) -> str:
    res = ""
    space_index = 0
    for i in range(len(s)):
        if space_index < len(spaces) and spaces[space_index] == i:
            res += " "
            space_index += 1
        res += s[i]
    return res