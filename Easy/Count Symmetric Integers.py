# Count Symmetric Integers
# O(n), O(1)
def countSymmetricIntegers(self, low: int, high: int) -> int:
    res = 0
    for i in range(low, high+1):
        curr_str = str(i)
        if len(curr_str) % 2 == 0:
            curr_sum = 0
            for j in range(len(curr_str) // 2):
                curr_sum += int(curr_str[j])
            for k in range(len(curr_str) // 2, len(curr_str)):
                curr_sum -= int(curr_str[k])
            if curr_sum == 0:
                res += 1
    return res