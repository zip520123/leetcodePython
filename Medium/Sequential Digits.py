# Sequential Digits
# O(n log n), O(n)
def sequentialDigits(self, low: int, high: int) -> List[int]:
    res = []
    for n in range(1,9):
        curr = n
        digit = n+1
        while curr * 10 + digit <= high:
            curr = curr*10+digit
            if curr >= low:
                res.append(curr)
            digit += 1
            if digit == 10:
                break
    return sorted(res)