# Climbing Stairs
# O(n), O(n)
def climbStairs(self, n: int) -> int:
    arr = [1,1]
    for i in range(2,n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]

# O(n), O(1)
def climbStairs(self, n: int) -> int:
    a, b = 1, 1
    for i in range(2,n+1):
        t = a + b
        a = b
        b = t
    return b