# Minimum Penalty for a Shop
# O(n), O(1)
def bestClosingTime(self, customers: str) -> int:
    customers += "N"
    index = 0
    n = len(customers)
    p = 0
    for char in customers:
        if char == "Y":
            p += 1
    minP = p
    for i in range(1,n):
        if customers[i-1] == "Y":
            p -= 1
        else:
            p += 1
        if minP > p:
            index = i
            minP = p
    return index