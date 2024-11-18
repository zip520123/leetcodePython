# Number of Unique Flavors After Sharing K Candies
# O(n*k), O(n) TLE
def shareCandies(self, candies: List[int], k: int) -> int:
    memo = defaultdict(int)
    n = len(candies)
    for c in candies:
        memo[c] += 1
    
    if k == 0:
        return len(memo.keys())
    flavors = len(memo.keys())
    res = 0
    curr_flavors = defaultdict(int)
    l, r = 0, 0
    while r<n:
        curr_flavors[candies[r]] += 1
        if r >= k-1:
            curr = flavors
            for key, val in curr_flavors.items():
                if memo[key] - val == 0:
                    curr -= 1
            res = max(res, curr)
            curr_flavors[candies[l]] -= 1
            if curr_flavors[candies[l]] == 0:
                del curr_flavors[candies[l]]
            l += 1
            
        r += 1
    return res

# O(n), O(n)
def shareCandies(self, candies: List[int], k: int) -> int:
    memo = defaultdict(int)
    n = len(candies)
    for c in candies:
        memo[c] += 1
    all_flavors = len(memo.keys())

    if k == 0:
        return all_flavors

    max_group_flavors = 0
    
    curr_flavors_count = defaultdict(int)
    curr_flavors_set = set()
    l, r = 0, 0
    while r<n:
        curr_flavors_count[candies[r]] += 1
        if curr_flavors_count[candies[r]] == memo[candies[r]]:
            curr_flavors_set.add(candies[r])
        
        if r >= k-1:
            max_group_flavors = max(max_group_flavors, all_flavors - len(curr_flavors_set))

            if curr_flavors_count[candies[l]] == memo[candies[l]]:
                curr_flavors_set.remove(candies[l])
            curr_flavors_count[candies[l]] -= 1

            l += 1
        r += 1
    return max_group_flavors