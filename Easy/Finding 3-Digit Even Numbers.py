# Finding 3-Digit Even Numbers
# O(n^3), O(n)
def findEvenNumbers(self, digits: List[int]) -> List[int]:
    
    digits.sort()
    n = len(digits)
    nums = set()
    for i in range(n):
        if digits[i] == 0:
            continue
        for j in range(n):
            for k in range(n):
                if i != j and j != k and k != i and digits[k] % 2 == 0:
                    curr = digits[i] * 100 + digits[j] * 10 + digits[k]
                    nums.add(curr)
                        
    return sorted(list(nums))