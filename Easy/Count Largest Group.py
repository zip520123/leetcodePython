# Count Largest Group
# O(n), O(n)
def countLargestGroup(self, n: int) -> int:
    memo = defaultdict(int)
    max_n = 0
    for i in range(1, n+1):
        curr = i
        group_num = 0
        while curr:
            group_num += curr % 10
            curr //= 10
        memo[group_num] += 1
        max_n = max(max_n, memo[group_num])
    
    res = 0
    for val in memo.values():
        if val == max_n:
            res += 1
    return res