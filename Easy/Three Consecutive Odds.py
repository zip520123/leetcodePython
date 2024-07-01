# Three Consecutive Odds
# O(n), O(1)
def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    count = 0
    for n in arr:
        if n % 2 == 1:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False