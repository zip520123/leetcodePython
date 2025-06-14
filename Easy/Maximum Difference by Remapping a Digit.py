# Maximum Difference by Remapping a Digit
# O(n), O(n)
def minMaxDifference(self, num: int) -> int:
    s = str(num)
    curr_max = 0
    curr_min = 0
    replace_num = s[0]
    for char in s:
        find = False
        for n in "876543210":
            if char == n:
                replace_num = char
                find = True
                break
        if find:
            break

    
    for char in s:
        curr_max *= 10
        if char == replace_num:
            curr_max += 9
        else:
            curr_max += int(char)
    
    replace_num = s[0]
    for char in s:
        curr_min *= 10
        if char == replace_num:
            curr_min += 0
        else:
            curr_min += int(char)
    
    return curr_max - curr_min