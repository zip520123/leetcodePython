# XOR Queries of a Subarray
# O(n), O(n)
def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    prefix_sum = [arr[0]]
    for i in range(1, len(arr)):
        prefix_sum.append(prefix_sum[i-1] ^ arr[i])
    res = []
    for l, r in queries:
        if l == 0:
            res.append(prefix_sum[r])
        else:
            res.append(prefix_sum[r] ^ prefix_sum[l-1])
    return res