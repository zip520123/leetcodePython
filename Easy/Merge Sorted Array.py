# Merge Sorted Array
# O(n), O(n)
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    arr = []
    l, r = 0, 0
    while l<m and r<n:
        if nums1[l] < nums2[r]:
            arr.append(nums1[l])
            l += 1
        else:
            arr.append(nums2[r])
            r += 1
    while l<m:
        arr.append(nums1[l])
        l += 1
    while r<n:
        arr.append(nums2[r])
        r += 1
    for i in range(m+n):
        nums1[i] = arr[i]