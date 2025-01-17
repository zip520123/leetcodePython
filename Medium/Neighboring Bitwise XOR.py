# Neighboring Bitwise XOR
def doesValidArrayExist(self, derived: List[int]) -> bool:
    curr = 0
    for i in derived:
        curr ^= i
    return curr == 0