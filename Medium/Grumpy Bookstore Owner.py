# Grumpy Bookstore Owner
# O(n), O(1)
def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
    base = 0
    n = len(customers)
    for i in range(n):
        if grumpy[i] == 0:
            base += customers[i]
    curr_window = 0
    res = 0
    for i in range(n):
        if grumpy[i] == 1:
            curr_window += customers[i]
        index = i - minutes 
        if 0 <= index < n:
            if grumpy[index] == 1:
                curr_window -= customers[index]
        res = max(res, base + curr_window)
    return res