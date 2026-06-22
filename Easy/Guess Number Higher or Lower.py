# Guess Number Higher or Lower
# O(log n) time | O(1) space
def guessNumber(self, n: int) -> int:
    l, r = 1, n
    while l<r:
        mid = l+((r-l)//2)
        curr = guess(mid)
        if curr == 1:
            l = mid+1
        elif curr == -1:
            r = mid
        else:
            return mid
    return l