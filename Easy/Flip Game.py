# Flip Game
# O(n), O(n)
def generatePossibleNextMoves(self, currentState: str) -> List[str]:
    n = len(currentState)
    if n == 1: return []
    res = []
    for i in range(1,n):
        if currentState[i] == "+" and currentState[i-1] == "+":
            curr = currentState[:i-1] + "--" + currentState[i+1:]
            res.append(curr)
    return res