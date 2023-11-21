# Count Nice Pairs in an Array
# O(n), O(n)
def countNicePairs(self, nums: List[int]) -> int:
    def rev(n):
        res = 0
        while n:
            res = res*10 + n%10
            n //= 10
        return res
    
    arr = []
    for n in nums:
        arr.append(n-rev(n))
    res = 0
    dic = defaultdict(int)
    for n in arr:
        res = (res + dic[n]) % (10 ** 9 + 7)
        dic[n] += 1
    return res
