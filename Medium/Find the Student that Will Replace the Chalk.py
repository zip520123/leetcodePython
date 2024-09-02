# Find the Student that Will Replace the Chalk
# O(n), O(1)
def chalkReplacer(self, chalk: List[int], k: int) -> int:
    sumN = sum(chalk) 
    curr = k % sumN 
    for i in range(len(chalk)):
        curr -= chalk[i]
        if curr < 0:
            return i
    return 0