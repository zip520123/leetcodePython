# Number of Laser Beams in a Bank
# O(n), O(n)
def numberOfBeams(self, bank: List[str]) -> int:
    res = 0
    rows = []
    for row in bank:
        ones = 0
        for char in row:
            if char == "1": ones += 1
        if ones > 0:
            rows.append(row)
        
    n = len(rows)
    for i in range(n-1):
        l = 0
        for char in rows[i]:
            if char == "1": l += 1
        r = 0
        for char in rows[i+1]:
            if char == "1": r += 1
        res += l*r
    return res
