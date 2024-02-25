# Greatest Common Divisor Traversal
# O(n^2), O(n), TLE
def canTraverseAllPairs(self, nums: List[int]) -> bool:
    memo = {}
    if len(nums) == 1: return True
    def find(node: int) -> int:
        if node not in memo:
            memo[node] = node
            return memo[node]
        if memo[node] != node:
            memo[node] = find(memo[node])
        return memo[node]
    def union(node1: int, node2: int):
        root1, root2 = find(node1), find(node2)
        memo[root2] = root1
    
    for n in nums:
        if n == 1: return False
        arr = []
        for k in range(2, n+1):
            if n % k == 0:
                arr.append(k)
        for i in range(len(arr)-1):
            union(arr[i], arr[i+1])
    for i in range(1, len(nums)):
        root1, root2 = find(nums[i-1]), find(nums[i])
        if root1 != root2: return False
    return True

# O(n log n), O(n)
def canTraverseAllPairs(self, nums: List[int]) -> bool:
    if len(nums) == 1: return True

    memo = {}
    
    def find(node: int) -> int:
        if node not in memo:
            memo[node] = node
            return memo[node]
        if memo[node] != node:
            memo[node] = find(memo[node])
        return memo[node]

    def union(node1: int, node2: int):
        root1, root2 = find(node1), find(node2)
        memo[root2] = root1

    def get_primes(n: int) -> List[int]:
        s = set()
        while n % 2 == 0:
            s.add(2)
            n //= 2
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                s.add(i)
                n //= i
        if n > 2: s.add(n)
        
        return list(s)
    
    for n in nums:
        if n == 1: return False
        primes = get_primes(n)
        for p in primes:
            union(p, n)

    for i in range(1, len(nums)):
        root1, root2 = find(nums[i-1]), find(nums[i])
        if root1 != root2: return False
    return True