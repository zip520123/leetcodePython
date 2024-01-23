# Maximum Length of a Concatenated String with Unique Characters
# O(2^n), O(n!)
def maxLength(self, arr: List[str]) -> int:
    dp = [set()]
    for s in arr:
        if len(set(s)) < len(s):
            continue
        curr = set(s)
        for group in dp:
            if curr & group: continue
            dp.append(curr | group)
    return max(map(lambda s: len(s), dp))

def maxLength(self, arr: List[str]) -> int:
    dp = [set()]
    for s in arr:
        curr_set = set(s)
        if len(curr_set) < len(s): continue
        for group in dp:
            if group & curr_set: continue
            dp.append(group | curr_set)
    return max([len(x) for x in dp])