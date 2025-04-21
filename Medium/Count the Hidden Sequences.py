# Count the Hidden Sequences
# O(n), O(1)
def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
    min_n = 0
    max_n = 0
    curr = 0
    for d in differences:
        curr += d
        min_n = min(min_n, curr)
        max_n = max(max_n, curr)
    min_start = lower - min_n
    max_start = upper - max_n
    if min_start > max_start:
        return 0
    return max_start - min_start + 1