# Calculate Money in Leetcode Bank
# O(1), O(1)
def totalMoney(self, n: int) -> int:
    weeks = n//7
    lastDays = n%7
    return 28*weeks + (0+7*(weeks-1))*weeks//2 + (1+weeks + lastDays+weeks) * lastDays // 2
