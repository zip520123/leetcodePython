# Minimized Maximum of Products Distributed to Any Store
# O(m*n), O(1), TLE
def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
    product_sum = sum(quantities)
    for i in range(1, product_sum+1):
        require_stores = 0 
        for q in quantities:
            require_stores += q//i
            if q % i > 0:
                require_stores += 1
        if require_stores <= n:
            return i
    return product_sum

# O(n log n), O(1)
def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
    product_sum = sum(quantities)
    l, r = 1, product_sum+1
    while l<=r :
        mid = l+((r-l)>>1)
        require_stores = 0
        for q in quantities:
            require_stores += q//mid
            if q % mid > 0:
                require_stores += 1
        if require_stores > n:
            l = mid + 1
        else:
            r = mid - 1
    return l