# Find the Pivot Integer
# O(n^2), O(1)
def pivotInteger(self, n: int) -> int:
    for i in range(1, n+1):
        curr = 0
        for j in range(i+1):
            curr += j
        end = 0
        for k in range(i,n+1):
            end += k
        if curr == end:
            return i
    return -1

# O(n), O(n)
def pivotInteger(self, n: int) -> int:
    arr = [0] * (n+1)
    for i in range(1, n+1):
        arr[i] = arr[i-1] + i
    for i in range(1, n+1):
        if arr[n] - arr[i] == arr[i-1]:
            return i
    return -1

# O(1), O(1)
def pivotInteger(self, n: int) -> int:
    sum = (1+n)*n // 2
    pivot = int(math.sqrt(sum))
    if pivot ** 2 == sum:
        return pivot
    return -1