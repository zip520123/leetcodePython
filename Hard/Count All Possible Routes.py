# Count All Possible Routes
# O(n^2*fuel), O(n^2*fuel)
def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
    memo = {}
    mod = 1E9+7
    n = len(locations)
    def dfs(start: int, fuel: int) -> int:
        if (start,fuel) in memo:
            return memo[(start, fuel)]
        
        res = 0
        if start == finish: 
            res += 1
        for nextCity in range(n):
            if nextCity != start:
                restFuel = fuel - abs(locations[start]-locations[nextCity])
                if restFuel >= 0:
                    res = (res + dfs(nextCity, restFuel)) % mod

        memo[(start, fuel)] = res
        return int(res)

    return dfs(start, fuel)
