# Check If Array Pairs Are Divisible by k
# O(n), O(n)

def canArrange(self, arr: List[int], k: int) -> bool:
    memo = defaultdict(int)
    for n in arr:
        memo[ (( n % k ) + k) % k] += 1
    for key in memo.keys():
        if key == 0:
            if memo[key] % 2 != 0:
                return False
        elif memo[key] != memo[k - key]:
            return False
    return True