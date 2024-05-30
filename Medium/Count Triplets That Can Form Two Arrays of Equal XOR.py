# Count Triplets That Can Form Two Arrays of Equal XOR
# O(n^3), O(1)
def countTriplets(self, arr: List[int]) -> int:
    res = 0
    n = len(arr)
    
    for i in range(n-1):
        a = 0
        for j in range(i+1, n):
            a ^= arr[j-1]
            b = 0
            for k in range(j, n):
                b ^= arr[k]
                if a == b: res += 1

    return res


# O(n^2), O(n)
def countTriplets(self, arr: List[int]) -> int:
    memo = [0] + arr[:]
    n = len(arr) + 1
    
    for i in range(1, n):
        memo[i] ^= memo[i-1]
    res = 0

    for j in range(n):
        for k in range(j+1, n):
            if memo[j] == memo[k]:
                res += k-j-1

    return res

def countTriplets(self, arr: List[int]) -> int:
    memo = { 0: 0 }
    n = len(arr) + 1
    
    for i in range(1, n):
        memo[i] = arr[i-1] ^ memo[i-1]
    res = 0

    for j in range(n):
        for k in range(j+1, n):
            if memo[j] == memo[k]:
                res += k-j-1

    return res