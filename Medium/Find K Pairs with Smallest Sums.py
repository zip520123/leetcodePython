# Find K Pairs with Smallest Sums
# O(min(k log k, (n1 * n2) log (n1 * n2))), O(n1*n2)
def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    from heapq import heappush, heappop
    n1 = len(nums1); n2 = len(nums2)
    res = []
    seen = set()
    heap = [(nums1[0]+nums2[0], (0,0))]
    while len(res) < k and heap:
        curr, (i,j) = heappop(heap)
        res.append([nums1[i],nums2[j]])
        if i+1<n1 and (i+1,j) not in seen:
            seen.add((i+1,j))
            heappush(heap, (nums1[i+1]+nums2[j],(i+1,j)))
        if j+1<n2 and (i,j+1) not in seen:
            seen.add((i,j+1))
            heappush(heap, (nums1[i]+nums2[j+1], (i,j+1)))
    return res
