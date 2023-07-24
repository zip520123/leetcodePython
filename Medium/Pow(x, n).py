# Pow(x, n)
# O(log n), O(log n)
def myPow(self, x: float, n: int) -> float:
    if n == 0: return 1

    if n < 0: return 1/self.myPow(x, -n)
    if n%2==0: return self.myPow(x*x, n/2)
    return self.myPow(x,n-1) * x

# O(log n), O(1)
def myPow(self, x: float, n: int) -> float:
    if n == 0: return 1
    if n < 0:
        n = -1 * n
        x = 1/x
    res = 1
    while n != 0:
        if n%2==1:
            n-=1
            res *= x
        x *= x
        n //= 2
    return res        

# O(log n), O(1)
def myPow(self, x: float, n: int) -> float:
    if n == 0: return 1
    if n < 0:
        n = -1 * n
        x = 1/x
    res = 1
    while n != 0:
        if n%2==0:
            x *= x
            n //= 2
        n-=1
        res *= x
        
    return res    