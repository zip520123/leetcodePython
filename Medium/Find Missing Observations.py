# Find Missing Observations
# O(n), O(1)
def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
    total_rolls = len(rolls) + n
    x = mean * total_rolls - sum(rolls)
    maxN = n * 6
    minN = n * 1
    if not minN <= x <= maxN: 
        return []
    res = [1] * n
    curr = x - n
    for i in range(n):
        if curr >= 5:
            res[i] += 5
            curr -= 5
        else:
            res[i] += curr
            break
        
    return res

# O(n), O(1)
def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
    total_rolls = len(rolls) + n
    x = mean * total_rolls - sum(rolls)
    maxN = n * 6
    minN = n * 1
    if not minN <= x <= maxN: 
        return []
    distribute_mean = x // n
    mod = x % n
    res = [distribute_mean] * n
    for i in range(mod):
        res[i] += 1
        
    return res