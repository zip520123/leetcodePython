from typing import List
import math
# brute force
# def numberOfwarehouse(centers: List[int], d: int) -> int:
#     min_point = math.inf
#     max_point = -math.inf
#     for center in centers:
#         min_point = min(min_point-d, center)
#         max_point = max(max_point+d, center)
    
#     res = 0
#     for n in range(min_point, max_point):
#         if distance(centers, n) <= d:
#             res += 1
    
#     return res

def numberOfwarehouse(centers: List[int], d: int) -> int:
    mid_point = sum(centers) // len(centers)
    l, r = -1e9, mid_point
    while l<r:
        mid = int(l+r)//2
        if distance(centers, mid) <= d:
            r = mid
        else:
            l = mid + 1
    left_point = l
    l, r = mid_point, 1e9
    while l<r:
        mid = int(l+r)//2
        if distance(centers, mid) <= d:
            l = mid
        else:
            r = mid - 1
    right_point = l

    return right_point - left_point + 1

def distance(centers: List[int], x: int) -> int:
    total = 0
    for center in centers:
        total += 2 * abs(center - x)
    return total

print(numberOfwarehouse([-2, 0, 1], 8))
assert numberOfwarehouse([-2, 0, 1], 8) == 3

print(numberOfwarehouse([2, 0, 3, -4], 22))
assert numberOfwarehouse([2, 0, 3, -4], 22) == 5
