# Check if Array Is Sorted and Rotated
# O(n^2), O(n)
def check(self, nums: List[int]) -> bool:
    sorted_arr = sorted(nums)
    n = len(nums)
    for i in range(n):
        if nums[i] == sorted_arr[0]:
            find = True
            for j in range(n):
                if nums[(i+j) % n] != sorted_arr[j]:
                    find = False
                    break
            if find:
                return True
    return False

# O(n), O(1)
def check(self, nums: List[int]) -> bool:
    inversted = False
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            if inversted:
                return False
            inversted = True
    if nums[len(nums)-1] > nums[0]:
        if inversted:
            return False
    return True

# O(n), O(1)
def check(self, nums: List[int]) -> bool:
    inverstion_count = 0
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            inverstion_count += 1
    if nums[len(nums)-1] > nums[0]:
        inverstion_count += 1
    return inverstion_count <= 1