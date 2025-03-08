# Minimum Recolors to Get K Consecutive Black Blocks
# O(n), O(1)
def minimumRecolors(self, blocks: str, k: int) -> int:
    res = math.inf
    whites = 0
    for i in range(len(blocks)):
        char = blocks[i]
        if char == "W":
            whites += 1
        if i >= k - 1:
            res = min(res, whites)
            if blocks[i - (k - 1)] == "W":
                whites -= 1
            
    return res
