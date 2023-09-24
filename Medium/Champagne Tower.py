# Champagne Tower
# O(row^2), O(row^2)
def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    memo = [([0] * (query_row + 1)) for _ in range(query_row+1)]
    memo[0][0] = poured
    for row in range(query_row):
        for col in range(row+1):
            p = (memo[row][col]-1) / 2
            if p > 0:
                memo[row+1][col] += p
                memo[row+1][col+1] += p
    
    return 1 if memo[query_row][query_glass] > 1 else memo[query_row][query_glass]