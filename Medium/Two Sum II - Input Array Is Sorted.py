# Two Sum II - Input Array Is Sorted
# O(nlogn), O(1)
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        curr = target - numbers[i]
        l, r = i+1, n
        while l<r:
            mid = l + (r-l) // 2
            if numbers[mid] < curr:
                l = mid + 1
            else:
                r = mid
        if l<n and numbers[l] == curr:
            return [i+1, l+1]
    return []

# O(n), O(1)
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l<r:
        curr = numbers[l] + numbers[r]
        if curr == target:
            return [l+1, r+1]
        elif curr < target:
            l += 1
        else:
            r -= 1
    return []