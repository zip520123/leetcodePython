# Lemonade Change
# O(n), O(1)
def lemonadeChange(self, bills: List[int]) -> bool:
    memo = defaultdict(int)
    for bill in bills:
        if bill == 5:
            memo[5] += 1
        elif bill == 10:
            if memo[5] == 0:
                return False
            memo[5] -= 1
            memo[10] += 1
        elif bill == 20:
            if memo[10] >= 1 and memo[5] >= 1:
                memo[10] -= 1
                memo[5] -= 1
            elif memo[5] >= 3:
                memo[5] -= 3
            else:
                return False
    return True