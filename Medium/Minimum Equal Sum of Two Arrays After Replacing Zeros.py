# Minimum Equal Sum of Two Arrays After Replacing Zeros
# O(n), O(1)
def minSum(self, nums1: List[int], nums2: List[int]) -> int:
    sum1, sum2 = 0, 0
    flag1, flag2 = False, False
    for n in nums1:
        if n == 0:
            sum1 += 1
            flag1 = True
        else:
            sum1 += n
    for n in nums2:
        if n == 0:
            sum2 += 1
            flag2 = True
        else:
            sum2 += n
    if sum1 > sum2 and flag2 == True:
        return sum1
    if sum2 > sum1 and flag1 == True:
        return sum2
    if sum1 == sum2:
        return sum1
    return -1