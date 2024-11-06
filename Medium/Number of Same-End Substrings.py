# Number of Same-End Substrings
# O(n log n), O(n)
class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        char_positions = defaultdict(list)
        for i in range(len(s)):
            char = s[i]
            char_positions[char].append(i)
        
        res = []
        for l, r in queries:
            same_end_substrings = 0

            for positions in char_positions.values():
                left_bound = bisect_left(positions, l)
                right_bound = bisect_right(positions, r)
                nums = right_bound - left_bound
                same_end_substrings += nums * (nums + 1) // 2
            res.append(same_end_substrings)
        return res

# O(n log n), O(n)
def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
    char_positions = defaultdict(list)
    for i in range(len(s)):
        char = s[i]
        char_positions[char].append(i)
    
    res = []
    for l, r in queries:
        same_end_substrings = 0

        for positions in char_positions.values():
            left, right = 0, len(positions)
            while left<right:
                mid = (left+right)//2
                if positions[mid] < l:
                    left = mid + 1
                else:
                    right = mid
            
            left_bound = left
            left, right = 0, len(positions)
            while left<right:
                mid = (left+right)//2
                if positions[mid] <= r:
                    left = mid + 1
                else:
                    right = mid
            right_bound = left
            nums = right_bound - left_bound
            same_end_substrings += nums * (nums + 1) // 2
        res.append(same_end_substrings)
    return res

# O(n), O(n)
def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
    prefix = [[0]*26 for _ in range(len(s)+1)]
    for i in range(1,len(s)+1):
        char = s[i-1]
        prefix[i][ord("a")-ord(char)] += 1
        for j in range(26):
            prefix[i][j] += prefix[i-1][j]
    
    res = []
    for l, r in queries:
        same_end = 0
        for i in range(26):
            nums_occurences = prefix[r+1][i] - prefix[l][i]
            same_end += nums_occurences * (nums_occurences+1) // 2
        res.append(same_end)
    return res