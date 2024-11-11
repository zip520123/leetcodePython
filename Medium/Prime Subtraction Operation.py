# Prime Subtraction Operation
# O(n * sqrt m), O(1)
class Solution:
    def is_prime(self, n) -> bool:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
            
    def primeSubOperation(self, nums: List[int]) -> bool:
        max_prime = 0
        for i in range(nums[0]-1, 1, -1):
            if self.is_prime(i):
                max_prime = i
                break

        nums[0] -= max_prime
        
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff <= 0:
                return False
            curr_prime = 0
            for d in range(diff-1, 1, -1):
                 if self.is_prime(d):
                    curr_prime = d
                    break
            nums[i] -= curr_prime
        return True